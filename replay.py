import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import signal
import argparse
import json

from server_dir.Graphics import Graphics


running = True

def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

class Map:
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid

class Agent:
    def __init__(self, id, x, y, parcels_carried, score):
        self.id = id
        self.x = x
        self.y = y
        self.parcels_carried = parcels_carried
        self.score = score
    
    def print_agent(self):
        text = "Agent id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " score: " + str(self.score) + " carrying: " + str(self.parcels_carried)
        return text

class Parcel:
    def __init__(self, id, x, y, score, carried_by_id, to_draw, to_draw_on_agent):
        self.id = id
        self.x = x
        self.y = y
        self.score = score
        self.carried_by = carried_by_id
        self.to_draw = to_draw
        self.to_draw_on_agent = to_draw_on_agent
    
    def print_parcel(self):
        text = "Parcel id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " score: " + str(self.score) + " carried by: " + str(self.carried_by)
        return text

class Game:
    def __init__(self, folder):
        self.replay_file = "experiments/" + folder + "/replay.json"
        self.replay = json.load(open(self.replay_file, 'r'))
        self.frame_counter = 0
        self.map = None
        self.parcels = []
        self.agents = []
    
    def update_state(self):
        if str(self.frame_counter) in self.replay.keys():
            if "map" in self.replay[str(self.frame_counter)].keys():
                width = int(self.replay[str(self.frame_counter)]["map"]["width"])
                height = int(self.replay[str(self.frame_counter)]["map"]["height"])
                grid = list(self.replay[str(self.frame_counter)]["map"]["grid"])
                self.map = Map(width, height, grid)

            if "parcels" in self.replay[str(self.frame_counter)].keys():
                self.parcels = []
                for parcel in list(self.replay[str(self.frame_counter)]["parcels"]):
                    id = int(parcel["id"])
                    x = int(parcel["x"])
                    y = int(parcel["y"])
                    score = int(parcel["score"])
                    carried_by_id = int(parcel["carried_by_id"])
                    to_draw = bool(parcel["to_draw"])
                    to_draw_on_agent = bool(parcel["to_draw_on_agent"])
                    self.parcels.append(Parcel(id, x, y, score, carried_by_id, to_draw, to_draw_on_agent))
            
            if "agents" in self.replay[str(self.frame_counter)].keys():
                self.agents = []
                for agent in list(self.replay[str(self.frame_counter)]["agents"]):
                    id = int(agent["id"])
                    x = int(agent["x"])
                    y = int(agent["y"])
                    parcels_carried = list(agent["parcels_carried"])
                    score = int(agent["score"])
                    self.agents.append(Agent(id, x, y, parcels_carried, score))
        else:
            print("End of replay file")
            self.frame_counter = -1
        
        self.frame_counter += 1


def game_loop(game, graphics, clock):
    global running
    
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
                    

        game.update_state()

        graphics.draw_environment()
        graphics.display_info()

        graphics.display_fps(clock.get_fps())
        
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deliveroo2 Replay System")
    parser.add_argument('--folder', type=str, required=True, help="Path to the log folder")
    args = parser.parse_args()


    pygame.init()

    game = Game(args.folder)

    graphics = Graphics(game)
    
    pygame.display.set_caption("Deliveroo2")
    clock = pygame.time.Clock()

    game_loop(game, graphics, clock)