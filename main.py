import pygame
import signal
from classes import Game
from communication import Communication
from graphics import Graphics


#########################
###### VARIABLES ########
#########################
screen_width = 1000
screen_height = 600
HOST = '127.0.0.1'
PORT = 8080
map_confing_path = 'conf/maps/cross11.txt'
parcels_config_path = 'conf/parcels/test_parcels.txt'
framerate = 60


server = Communication(HOST, PORT)
game = Game(map_confing_path, parcels_config_path, server)
pygame.init()
graphics = Graphics(screen_width, screen_height, game)
pygame.display.set_caption("deliveroo")
clock = pygame.time.Clock()



#########################
#### HANDLE ACTIONS #####
#########################

def handle_actions():
    if len(server.buffer) > 0:
        msg, addr = server.buffer.pop(0)
        CLIENT_PORT = addr[1]
        msg = msg.split()

        if msg[0] == 'connect':
            id = game.new_agent()
            if id == 0:
                server.send("error", (HOST, CLIENT_PORT))
                print("An error occured while creating an agent.")
            else:
                game.agents_port_to_id[str(CLIENT_PORT)] = id
                server.send("connected " + str(id), (HOST, CLIENT_PORT))
                game.send_entire_state(CLIENT_PORT)
                print("Agent ", str(id), " with port ", str(CLIENT_PORT), " has connected.")
        
        if msg[0] == 'disconnect':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            del game.agents_port_to_id[str(CLIENT_PORT)]
            game.remove_agent(id)
            print("Agent ", id, " with port ", str(CLIENT_PORT), " has disconnected.")
        
        if msg[0] == 'moveleft':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            res = game.agent_move_left(id)
            print("Agent ", id, " move left: ", res)
        
        if msg[0] == 'moveright':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            res = game.agent_move_right(id)
            print("Agent ", id, " move right: ", res)
        
        if msg[0] == 'moveup':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            res = game.agent_move_up(id)
            print("Agent ", id, " move up: ", res)
        
        if msg[0] == 'movedown':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            res = game.agent_move_down(id)
            print("Agent ", id, " move down: ", res)
        
        if msg[0] == 'pickup':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            res = game.agent_pick_up(id)
            print("Agent ", id, " pick up: ", res)
        
        if msg[0] == 'putdown':
            id = game.agents_port_to_id[str(CLIENT_PORT)]
            res = game.agent_put_down(id)
            print("Agent ", id, " put down: ", res)



#########################
##### SIGINT HANDLER ####
#########################

def signal_handler(sig, frame):
    for port in game.agents_port_to_id.keys():
        server.send("exit", (HOST, int(port)))
    server.send("exit", (HOST, PORT))
    server.server_thread.join()
    print("Exited correctly.")
    exit()

signal.signal(signal.SIGINT, signal_handler)



#########################
##### MAIN GAME LOOP ####
#########################

while game.server.is_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            signal_handler(signal.SIGINT, None)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                graphics.lmb_pressed()
            if event.button == 3:
                graphics.show_cell_info()
        
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                graphics.move_screen()
        
        if event.type == pygame.MOUSEWHEEL:
            graphics.scale_sizes(event.y)
    

    handle_actions()

    graphics.draw_environment()

    graphics.display_info()

    game.decay_parcels()
    game.spawn_parcels()
    
    game.set_new_state()
    game.create_events()
    game.send_events()


    pygame.display.update()
    clock.tick(framerate)
