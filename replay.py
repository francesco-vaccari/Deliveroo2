import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import signal
import argparse
import json

from server_dir.Graphics import Graphics


running = True
frame_counter = 0
framerate = 60

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
    def __init__(self, id, x, y, parcels_carried, has_key, score, energy):
        self.id = id
        self.x = x
        self.y = y
        self.parcels_carried = parcels_carried
        self.has_key = has_key
        self.score = score
        self.energy = energy
    
    def print_agent(self):
        text = "Agent id: " +    str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " parcels carried: " + str(self.parcels_carried) + " has key: " + str(self.has_key) + " score: " + str(self.score) + " energy: " + str(self.energy)
        return text

class Parcel:
    def __init__(self, id, x, y, score, carried_by, to_draw, to_draw_on_agent):
        self.id = id
        self.x = x
        self.y = y
        self.score = score
        self.carried_by = carried_by
        self.to_draw = to_draw
        self.to_draw_on_agent = to_draw_on_agent
    
    def print_parcel(self):
        text = "Parcel id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " score: " + str(self.score) + " carried by: " + str(self.carried_by)
        return text

class Battery:
    def __init__(self, id, x, y, to_draw, to_draw_on_agent):
        self.id = id
        self.x = x
        self.y = y
        self.to_draw = to_draw
        self.to_draw_on_agent = to_draw_on_agent
    
    def print_battery(self):
        text = "Battery id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y)
        return text

class Key:
    def __init__(self, id, x, y, carried_by, to_draw, to_draw_on_agent):
        self.id = id
        self.x = x
        self.y = y
        self.carried_by = carried_by
        self.to_draw = to_draw
        self.to_draw_on_agent = to_draw_on_agent

    def print_key(self):
        text = "Key id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " carried by: " + str(self.carried_by)
        return text

class Door:
    def __init__(self, id, x, y, to_draw, to_draw_on_agent):
        self.id = id
        self.x = x
        self.y = y
        self.to_draw = to_draw
        self.to_draw_on_agent = to_draw_on_agent
    
    def print_door(self):
        text = "Door id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y)
        return text

class Game:
    def __init__(self, folder):
        self.replay_file = os.path.join("experiments", folder, "replay.json")
        self.replay = json.load(open(self.replay_file, 'r'))
        self.map = None
        self.parcels = []
        self.agents = []
    
    def get_n_frames(self):
        return len(self.replay.keys())
    
    def update_state(self, frame_counter):
        if str(frame_counter) in self.replay.keys():

            if "map" in self.replay[str(frame_counter)].keys():
                width = int(self.replay[str(frame_counter)]["map"]["width"])
                height = int(self.replay[str(frame_counter)]["map"]["height"])
                grid = list(self.replay[str(frame_counter)]["map"]["grid"])
                self.map = Map(width, height, grid)

            if "parcels" in self.replay[str(frame_counter)].keys():
                self.parcels = []
                for parcel in list(self.replay[str(frame_counter)]["parcels"]):
                    id = int(parcel["id"])
                    x = int(parcel["x"])
                    y = int(parcel["y"])
                    score = int(parcel["score"])
                    carried_by_id = int(parcel["carried_by_id"])
                    to_draw = bool(parcel["to_draw"])
                    to_draw_on_agent = bool(parcel["to_draw_on_agent"])
                    self.parcels.append(Parcel(id, x, y, score, carried_by_id, to_draw, to_draw_on_agent))
            
            if "agents" in self.replay[str(frame_counter)].keys():
                self.agents = []
                for agent in list(self.replay[str(frame_counter)]["agents"]):
                    id = int(agent["id"])
                    x = int(agent["x"])
                    y = int(agent["y"])
                    parcels_carried = list(agent["parcels_carried"])
                    has_key = bool(agent["has_key"])
                    score = int(agent["score"])
                    energy = int(agent["energy"])
                    self.agents.append(Agent(id, x, y, parcels_carried, has_key, score, energy))
            
            if "batteries" in self.replay[str(frame_counter)].keys():
                self.batteries = []
                for battery in list(self.replay[str(frame_counter)]["batteries"]):
                    id = int(battery["id"])
                    x = int(battery["x"])
                    y = int(battery["y"])
                    to_draw = bool(battery["to_draw"])
                    to_draw_on_agent = bool(battery["to_draw_on_agent"])
                    self.batteries.append(Battery(id, x, y, to_draw, to_draw_on_agent))
            
            if "keys" in self.replay[str(frame_counter)].keys():
                self.keys = []
                for key in list(self.replay[str(frame_counter)]["keys"]):
                    id = int(key["id"])
                    x = int(key["x"])
                    y = int(key["y"])
                    carried_by_id = int(key["carried_by_id"])
                    to_draw = bool(key["to_draw"])
                    to_draw_on_agent = bool(key["to_draw_on_agent"])
                    self.keys.append(Key(id, x, y, carried_by_id, to_draw, to_draw_on_agent))
            
            if "doors" in self.replay[str(frame_counter)].keys():
                self.doors = []
                for door in list(self.replay[str(frame_counter)]["doors"]):
                    id = int(door["id"])
                    x = int(door["x"])
                    y = int(door["y"])
                    to_draw = bool(door["to_draw"])
                    to_draw_on_agent = bool(door["to_draw_on_agent"])
                    self.doors.append(Door(id, x, y, to_draw, to_draw_on_agent))

def game_loop(game, graphics, clock):
    global running
    global frame_counter
    global framerate
    n_frames = game.get_n_frames()
    
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
                    framerate -= 20
                    if framerate == 0:
                        framerate = 20
                if event.key == pygame.K_RIGHT:
                    framerate += 20
                    

        game.update_state(frame_counter)

        graphics.draw_environment()
        graphics.display_info()

        graphics.display_fps(clock.get_fps())
        
        pygame.display.update()

        print(f"Framerate: {framerate:4d} \t Frame: {frame_counter:4d} / {n_frames:4d}", end="\r")

        clock.tick(framerate)
        frame_counter += 1
        if frame_counter >= n_frames:
            frame_counter = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deliveroo2 Replay System")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    args = parser.parse_args()


    pygame.init()

    game = Game(args.folder)

    graphics = Graphics(game)
    
    pygame.display.set_caption("Deliveroo2")
    clock = pygame.time.Clock()

    game_loop(game, graphics, clock)