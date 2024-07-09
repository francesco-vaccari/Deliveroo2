import argparse
import pygame
import signal
from server_dir.classes import Game
from communication import Communication
from server_dir.graphics import Graphics

class Server:
    def __init__(self, address, server_port, map_config_path, parcels_config_path, framerate, screen_width, screen_height):
        self.HOST = address
        self.PORT = server_port
        self.map_confing_path = map_config_path
        self.parcels_config_path = parcels_config_path
        self.framerate = framerate
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.server = Communication(self.HOST, self.PORT)
        self.game = Game(self.map_confing_path, parcels_config_path, self.server)
        pygame.init()
        self.graphics = Graphics(screen_width, screen_height, self.game)
        pygame.display.set_caption("Deliveroo2")
        self.clock = pygame.time.Clock()

        signal.signal(signal.SIGINT, self.signal_handler)

        self.main_loop()

    def handle_actions(self):
        # maybe change this to while so that it can handle multiple actions in one frame
        # also I should add a timer for game actions from the same agent
        if len(self.server.buffer) > 0:
            msg, addr = self.server.buffer.pop(0)
            CLIENT_PORT = addr[1]
            msg = msg.split()

            if msg[0] == 'connect':
                id = self.game.new_agent()
                if id == 0:
                    self.server.send("error", (self.HOST, CLIENT_PORT))
                    print("An error occured while creating an agent.")
                else:
                    self.game.agents_port_to_id[str(CLIENT_PORT)] = id
                    self.server.send("connected " + str(id), (self.HOST, CLIENT_PORT))
                    self.game.send_entire_state(CLIENT_PORT)
                    print("Agent ", str(id), " with port ", str(CLIENT_PORT), " has connected.")
            
            if msg[0] == 'disconnect':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                del self.game.agents_port_to_id[str(CLIENT_PORT)]
                self.game.remove_agent(id)
                print("Agent ", id, " with port ", str(CLIENT_PORT), " has disconnected.")
            
            ### GAME ACTIONS ###
            if msg[0] == 'moveleft':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                res = self.game.agent_move_left(id)
                print("Agent ", id, " move left: ", res)
            
            if msg[0] == 'moveright':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                res = self.game.agent_move_right(id)
                print("Agent ", id, " move right: ", res)
            
            if msg[0] == 'moveup':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                res = self.game.agent_move_up(id)
                print("Agent ", id, " move up: ", res)
            
            if msg[0] == 'movedown':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                res = self.game.agent_move_down(id)
                print("Agent ", id, " move down: ", res)
            
            if msg[0] == 'pickup':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                res = self.game.agent_pick_up(id)
                print("Agent ", id, " pick up: ", res)
            
            if msg[0] == 'putdown':
                id = self.game.agents_port_to_id[str(CLIENT_PORT)]
                res = self.game.agent_put_down(id)
                print("Agent ", id, " put down: ", res)

    def signal_handler(self, sig, frame):
        for port in self.game.agents_port_to_id.keys():
            self.server.send("exit", (self.HOST, int(port)))
        self.server.send("exit", (self.HOST, self.PORT))
        self.server.server_thread.join()
        print("Exited correctly.")
        exit()
    
    def main_loop(self):
        while self.game.server.is_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.signal_handler(signal.SIGINT, None)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.graphics.lmb_pressed()
                    if event.button == 3:
                        self.graphics.show_cell_info()
                
                if event.type == pygame.MOUSEMOTION:
                    if event.buttons[0]:
                        self.graphics.move_screen()
                
                if event.type == pygame.MOUSEWHEEL:
                    self.graphics.scale_sizes(event.y)
            

            self.handle_actions()

            self.graphics.draw_environment()
            # graphics.display_info()

            self.game.decay_parcels()
            self.game.spawn_parcels()
            
            self.game.set_new_state()
            self.game.create_events()
            self.game.send_events()


            pygame.display.update()
            self.clock.tick(self.framerate)


if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Deliveroo2 Experiment Manager")
    parser.add_argument('--port', type=int, required=False, help="Port for the server", default=8080)
    parser.add_argument('--map', type=str, required=True, help="Map configuration file")
    parser.add_argument('--parcels', type=str, required=True, help="Parcels configuration file")
    parser.add_argument('--framerate', type=int, required=False, help="Framerate of the game", default=60)
    parser.add_argument('--width', type=int, required=False, help="Width of the game window", default=600)
    parser.add_argument('--height', type=int, required=False, help="Height of the game window", default=600)
    args = parser.parse_args()

    server = Server('127.0.0.1', args.port, 'server_dir/conf/maps/' + args.map, 'server_dir/conf/parcels/' + args.parcels, args.framerate, args.width, args.height)