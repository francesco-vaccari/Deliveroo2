import pygame
import signal
import argparse

from utils.Logger import ExperimentLogger
from utils.Communication import Communication

from server_dir.game_classes import Game
from server_dir.Graphics import Graphics


running = True

def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def send_events(communication, logger, events, agents_ports_to_ids):
    for event in events:
        for port, id in agents_ports_to_ids.items():
            communication.send_to_agent(event, port, id)
            logger.log_info(f"Sent event to agent (ID:{id}): {event}")

def send_state(communication, logger, state, agents_ports_to_ids, id):
    for port, agent_id in agents_ports_to_ids.items():
        if agent_id == id:
            for event in state:
                communication.send_to_agent(event, port, agent_id)
                logger.log_info(f"Sent event to agent (ID:{id}): {event}")
        break

def handle_messages(communication, logger, agents_ports_to_ids):
    actions = []

    while len(communication.buffer) > 0:
        msg, addr = communication.buffer.pop(0)
        agent_port = addr[1]

        if msg.split()[0] == 'connect':
            if agent_port not in agents_ports_to_ids:
                id = game.new_agent()
                agents_ports_to_ids[agent_port] = id
                communication.send_to_agent("connected " + str(id), agent_port, id)
                logger.log_info(f"Agent connected with ID {id} and address {addr}")
                send_state(communication, logger, game.get_state(), agents_ports_to_ids, id)
        
        elif msg.split()[0] == 'disconnect':
            id = agents_ports_to_ids[agent_port]
            del agents_ports_to_ids[agent_port]
            game.remove_agent(id)
            logger.log_info(f"Agent disconnected with ID:{id} and address {addr}")
        
        else:
            actions.append((msg, agent_port))
        
    return actions

def handle_actions(communication, logger, agents_ports_to_ids, actions):
    for action in actions:
        msg, agent_port = action
        msg = msg.split()
        
        if msg[0] == 'moveleft':
            id = agents_ports_to_ids[agent_port]
            res = game.agent_move_left(id)
            logger.log_info(f"Agent {id} moved left: {res}")
        
        if msg[0] == 'moveright':
            id = agents_ports_to_ids[agent_port]
            res = game.agent_move_right(id)
            logger.log_info(f"Agent {id} moved right: {res}")
        
        if msg[0] == 'moveup':
            id = agents_ports_to_ids[agent_port]
            res = game.agent_move_up(id)
            logger.log_info(f"Agent {id} moved up: {res}")
        
        if msg[0] == 'movedown':
            id = agents_ports_to_ids[agent_port]
            res = game.agent_move_down(id)
            logger.log_info(f"Agent {id} moved down: {res}")
        
        if msg[0] == 'pickup':
            id = agents_ports_to_ids[agent_port]
            res = game.agent_pick_up(id)
            logger.log_info(f"Agent {id} picked up: {res}")
        
        if msg[0] == 'putdown':
            id = agents_ports_to_ids[agent_port]
            res = game.agent_put_down(id)
            logger.log_info(f"Agent {id} put down: {res}")

def game_loop(communication, game, graphics, clock, logger):
    global running
    agents_ports_to_ids = {}
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
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
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.agent_move_left(0)
                    game.agent_move_left(1)
                    game.agent_move_left(2)
                if event.key == pygame.K_RIGHT:
                    game.agent_move_right(0)
                    game.agent_move_right(1)
                    game.agent_move_right(2)
                if event.key == pygame.K_UP:
                    game.agent_move_up(0)
                    game.agent_move_up(1)
                    game.agent_move_up(2)
                if event.key == pygame.K_DOWN:
                    game.agent_move_down(0)
                    game.agent_move_down(1)
                    game.agent_move_down(2)
                if event.key == pygame.K_SPACE:
                    game.agent_pick_up(0)
                    game.agent_pick_up(1)
                    game.agent_pick_up(2)
                if event.key == pygame.K_RETURN:
                    game.agent_put_down(0)
                    game.agent_put_down(1)
                    game.agent_put_down(2)
                    
        
        actions = handle_messages(communication, logger, agents_ports_to_ids)
        handle_actions(communication, logger, agents_ports_to_ids, actions)

        graphics.draw_environment()
        graphics.display_info()

        game.decay_parcels()
        game.spawn_parcels()
        
        game.set_new_state()
        game.create_events()
        events = game.get_events()

        send_events(communication, logger, events, agents_ports_to_ids)

        pygame.display.update()
        clock.tick(60)

    communication.close()
    logger.log_debug("Server terminated")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deliveroo2 Server")
    parser.add_argument('--map', type=str, required=True, help="Path to the map config file")
    parser.add_argument('--parcels', type=str, required=True, help="Path to the parcels config file")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help="Host address of the server")
    parser.add_argument('--port', type=int, required=False, default=8080, help="Port number of the server")
    args = parser.parse_args()


    logger = ExperimentLogger(args.folder, 'server.log')
    logger.log_debug("Server started")

    communication = Communication(args.folder, args.host, args.port)
    game = Game(args.map, args.parcels)
    
    pygame.init()
    
    graphics = Graphics(game)
    
    pygame.display.set_caption("Deliveroo2")
    clock = pygame.time.Clock()

    game_loop(communication, game, graphics, clock, logger)




