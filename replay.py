from datetime import datetime
import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import signal
import argparse
import json
from server_dir.Graphics import Graphics

import os
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea, QApplication
import sys


running = True
frame_counter = 0
framerate = 60
frame_offset = 180

evolution_steps = {}
belief_sets = {}
memories = {}

def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


class RealTimeVisualizer(QWidget):
    def __init__(self):
        super().__init__()

        self.last_evolution_step = "Empty"
        self.last_belief_set = {}
        self.last_memory = "Empty"

        self.self_close = False
        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()

        self.buttons_layout = QVBoxLayout()
        self.button1 = QPushButton("Show Current Evolution Step")
        self.button2 = QPushButton("Show Current Belief Set")
        self.button3 = QPushButton("Show Last Memory")
        
        self.button1.clicked.connect(lambda: self.show_widget(self.scroll1))
        self.button2.clicked.connect(lambda: self.show_widget(self.scroll2))
        self.button3.clicked.connect(lambda: self.show_widget(self.scroll3))
        
        self.buttons_layout.addWidget(self.button1)
        self.buttons_layout.addWidget(self.button2)
        self.buttons_layout.addWidget(self.button3)
        
        self.layout.addLayout(self.buttons_layout)

        self.scroll1 = self.create_scrollable_label("Evolution Step")
        self.scroll2 = self.create_scrollable_label("Belief set")
        self.scroll3 = self.create_scrollable_label("Last Memory")

        self.layout.addWidget(self.scroll1)
        self.layout.addWidget(self.scroll2)
        self.layout.addWidget(self.scroll3)
        
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(17)

        self.setWindowTitle("Replay System")
        self.show()
        
        self.show_widget(self.scroll1)

    def create_scrollable_label(self, text):
        scroll = QScrollArea()
        label = QLabel(text)
        label.setWordWrap(True)
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        scroll.setVisible(False)
        return scroll

    def show_widget(self, widget):
        self.scroll1.setVisible(False)
        self.scroll2.setVisible(False)
        self.scroll3.setVisible(False)
        widget.setVisible(True)

    def update_labels(self):
        global frame_counter
        global frame_offset
        global evolution_steps
        global belief_sets
        global memories

        key = frame_counter + frame_offset

        string = ""
        self.last_evolution_step = evolution_steps[key] if key in evolution_steps.keys() else self.last_evolution_step
        string += f"Desire ID: {self.last_evolution_step['desire_id']}\n\n"
        string += f"Intentions IDs: {self.last_evolution_step['intentions_ids']}\n\n"
        string += f"Actions: {self.last_evolution_step['actions']}\n\n"
        string += f"Error: {self.last_evolution_step['error']}"
        self.scroll1.widget().setText(string)

        self.last_belief_set = belief_sets[key] if key in belief_sets.keys() else self.last_belief_set
        self.scroll2.widget().setText(self.last_belief_set)

        self.last_memory = memories[key] if key in memories.keys() else self.last_memory
        self.scroll3.widget().setText(self.last_memory)

        if self.self_close:
            self.timer.stop()
            self.close()


def extract_from_string(start, end, string):
    if end == "":
        return string[string.find(start) + len(start):]
    return string[string.find(start) + len(start):string.find(end, string.find(start) + len(start))]

def get_time(string):
    try:
        string = string.split()[1].split(":")
        hour = string[0]
        minute = string[1]
        second = string[2].split(",")[0]
        millisecond = string[2].split(",")[1]
        return hour, minute, second, millisecond
    except:
        return None, None, None, None

def get_n_frame(start_time, end_time, frame_rate=60):
    start_hour, start_minute, start_second, start_millisecond = start_time
    end_hour, end_minute, end_second, end_millisecond = end_time

    start_str = f"{start_hour:02}:{start_minute:02}:{start_second:02}.{start_millisecond:03}"
    end_str = f"{end_hour:02}:{end_minute:02}:{end_second:02}.{end_millisecond:03}"

    time_format = '%H:%M:%S.%f'

    start_dt = datetime.strptime(start_str, time_format)
    end_dt = datetime.strptime(end_str, time_format)

    time_diff = end_dt - start_dt

    total_seconds = time_diff.total_seconds()

    n_frames = total_seconds * frame_rate

    return int(n_frames)

def load_belief_sets(folder, agent='agent_1'):
    global belief_sets
    server_log_file = os.path.join("experiments", folder, "server.log")
    with open(server_log_file, 'r') as file:
        start_time = get_time(file.readline())
        file.close()
    
    perception_log_file = os.path.join("experiments", folder, agent, "perception_manager.log")
    with open(perception_log_file, 'r') as file:
        lines = file.readlines()
        file.close()
    
    last_belief_set = ""
    temp_belief_sets = {}
    belief_set = "{}"
    for i, line in enumerate(lines):
        time = get_time(line)
        
        if "Function ran successfully. Result:" in line:
            belief_set = lines[i+1]
        
        if belief_set != last_belief_set:
            last_belief_set = belief_set
            temp_belief_sets[get_n_frame(start_time, time)] = belief_set
    
    last_belief_set = ""
    try:
        for frame in range(max(temp_belief_sets.keys()) + 1):
            if frame in temp_belief_sets.keys():
                last_belief_set = temp_belief_sets[frame]
            belief_sets[frame] = last_belief_set
    except:
        pass

def load_memories(folder, agent='agent_1'):
    global evolution_steps
    server_log_file = os.path.join("experiments", folder, "server.log")
    with open(server_log_file, 'r') as file:
        start_time = get_time(file.readline())
        file.close()
    
    perception_log_file = os.path.join("experiments", folder, agent, "control.log")
    with open(perception_log_file, 'r') as file:
        lines = file.readlines()
        file.close()

    last_memory = ""
    temp_memories = {}
    for line in lines:
        time = get_time(line)
        
        if " - INFO - [LOOP] Memory updated: " in line and time != (None, None, None, None):
            memory = extract_from_string("[LOOP] Memory updated: ", "", line)
            last_memory = memory

        if last_memory != "" and time != (None, None, None, None):
            temp_memories[get_n_frame(start_time, time)] = last_memory

    last_memory = ""
    try:
        for frame in range(max(temp_memories.keys()) + 1):
            if frame in temp_memories.keys():
                last_memory = temp_memories[frame]
            memories[frame] = last_memory
    except:
        pass

def load_evolution_steps(folder, agent='agent_1'):
    global evolution_steps
    server_log_file = os.path.join("experiments", folder, "server.log")
    with open(server_log_file, 'r') as file:
        start_time = get_time(file.readline())
        file.close()

    control_log_file = os.path.join("experiments", folder, agent, "control_manager.log")
    with open(control_log_file, 'r') as file:
        lines = file.readlines()
        file.close()
    
    last_desire = 0
    last_intentions = []
    last_actions = []
    last_error = ""

    last_desire_str = str(last_desire)
    last_intentions_str = str(last_intentions)
    last_actions_str = str(last_actions)
    last_error_str = str(last_error)

    temp_evolution_steps = {}

    for line in lines:
        time = get_time(line)

        if "Desire added:" in line:
            desire_id = extract_from_string("Desire added: ", ". Desires:", line)
            last_desire = desire_id
            last_intentions = []
            last_actions = []
            last_error = ""
        
        if "Running intention" in line:
            intention_id = extract_from_string("Running intention ", " ...", line)
            last_intentions.append(intention_id)
            last_actions = []
            last_error = ""
        
        if "Executing action" in line:
            action = extract_from_string("Executing action ", " ...", line)
            last_actions.append(action)
        
        if "Error during intention" in line:
            error = extract_from_string(" Error: ", "", line)
            last_error = error
        
        if str(last_desire) != last_desire_str or str(last_intentions) != last_intentions_str or str(last_actions) != last_actions_str or str(last_error) != last_error_str:
            last_desire_str = str(last_desire)
            last_intentions_str = str(last_intentions)
            last_actions_str = str(last_actions)
            last_error_str = str(last_error)

            temp_evolution_steps[get_n_frame(start_time, time)] = {"desire_id": last_desire_str, "intentions_ids": last_intentions_str, "actions": last_actions_str, "error": last_error_str}
    
    last_evolution_step = {"desire_id": None, "intentions_ids": None, "actions": None, "error": None}
    try:
        for frame in range(max(temp_evolution_steps.keys()) + 1):
            if frame in temp_evolution_steps.keys():
                last_evolution_step = temp_evolution_steps[frame]
            evolution_steps[frame] = last_evolution_step
    except:
        pass

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
        self.map = None
        self.parcels = []
        self.agents = []
        self.batteries = []
        self.keys = []
        self.doors = []

        self.states = {}

        self.load_replay(folder)
    
    def get_n_frames(self):
        return len(self.replay.keys())

    def load_replay(self, folder):
        self.replay_file = os.path.join("experiments", folder, "replay.json")
        self.replay = json.load(open(self.replay_file, 'r'))

        last_map = None
        last_parcels = []
        last_agents = []
        last_batteries = []
        last_keys = []
        last_doors = []

        for frame in range(self.get_n_frames()):

            if "map" in self.replay[str(frame)].keys():
                width = int(self.replay[str(frame)]["map"]["width"])
                height = int(self.replay[str(frame)]["map"]["height"])
                grid = list(self.replay[str(frame)]["map"]["grid"])
                self.map = Map(width, height, grid)
                last_map = self.map
            else:
                self.map = last_map
            
            if "parcels" in self.replay[str(frame)].keys():
                self.parcels = []
                for parcel in list(self.replay[str(frame)]["parcels"]):
                    id = int(parcel["id"])
                    x = int(parcel["x"])
                    y = int(parcel["y"])
                    score = int(parcel["score"])
                    carried_by_id = int(parcel["carried_by_id"])
                    to_draw = bool(parcel["to_draw"])
                    to_draw_on_agent = bool(parcel["to_draw_on_agent"])
                    self.parcels.append(Parcel(id, x, y, score, carried_by_id, to_draw, to_draw_on_agent))
                last_parcels = self.parcels
            else:
                self.parcels = last_parcels
            
            if "agents" in self.replay[str(frame)].keys():
                self.agents = []
                for agent in list(self.replay[str(frame)]["agents"]):
                    id = int(agent["id"])
                    x = int(agent["x"])
                    y = int(agent["y"])
                    parcels_carried = list(agent["parcels_carried"])
                    has_key = bool(agent["has_key"])
                    score = int(agent["score"])
                    energy = int(agent["energy"])
                    self.agents.append(Agent(id, x, y, parcels_carried, has_key, score, energy))
                last_agents = self.agents
            else:
                self.agents = last_agents

            if "batteries" in self.replay[str(frame)].keys():
                self.batteries = []
                for battery in list(self.replay[str(frame)]["batteries"]):
                    id = int(battery["id"])
                    x = int(battery["x"])
                    y = int(battery["y"])
                    to_draw = bool(battery["to_draw"])
                    to_draw_on_agent = bool(battery["to_draw_on_agent"])
                    self.batteries.append(Battery(id, x, y, to_draw, to_draw_on_agent))
                last_batteries = self.batteries
            else:
                self.batteries = last_batteries

            if "keys" in self.replay[str(frame)].keys():
                self.keys = []
                for key in list(self.replay[str(frame)]["keys"]):
                    id = int(key["id"])
                    x = int(key["x"])
                    y = int(key["y"])
                    carried_by_id = int(key["carried_by_id"])
                    to_draw = bool(key["to_draw"])
                    to_draw_on_agent = bool(key["to_draw_on_agent"])
                    self.keys.append(Key(id, x, y, carried_by_id, to_draw, to_draw_on_agent))
                last_keys = self.keys
            else:
                self.keys = last_keys

            if "doors" in self.replay[str(frame)].keys():
                self.doors = []
                for door in list(self.replay[str(frame)]["doors"]):
                    id = int(door["id"])
                    x = int(door["x"])
                    y = int(door["y"])
                    to_draw = bool(door["to_draw"])
                    to_draw_on_agent = bool(door["to_draw_on_agent"])
                    self.doors.append(Door(id, x, y, to_draw, to_draw_on_agent))
                last_doors = self.doors
            else:
                self.doors = last_doors

            self.states[frame] = {"map": self.map, "parcels": self.parcels, "agents": self.agents, "batteries": self.batteries, "keys": self.keys, "doors": self.doors}

    def load_state(self, frame_counter):
        self.map = self.states[frame_counter]["map"]
        self.parcels = self.states[frame_counter]["parcels"]
        self.agents = self.states[frame_counter]["agents"]
        self.batteries = self.states[frame_counter]["batteries"]
        self.keys = self.states[frame_counter]["keys"]
        self.doors = self.states[frame_counter]["doors"]

def game_loop(game, graphics, clock, visualizer):
    global running
    global frame_counter
    global framerate
    global frame_offset
    n_frames = game.get_n_frames()
    paused = False
    
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
                if event.key == pygame.K_MINUS:
                    framerate -= 20
                    if framerate == 0:
                        framerate = 20
                if event.key == pygame.K_PLUS:
                    framerate += 20
                if event.key == pygame.K_DOWN:
                    frame_offset -= 5
                    if frame_offset == 0:
                        frame_offset = 5
                if event.key == pygame.K_UP:
                    frame_offset += 5
                if event.key == pygame.K_LEFT:
                    frame_counter -= 300
                    if frame_counter < 0:
                        frame_counter = 0
                if event.key == pygame.K_RIGHT:
                    frame_counter += 300
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_q:
                    running = False

        game.load_state(frame_counter)

        graphics.draw_environment()
        graphics.display_info()

        graphics.display_fps(clock.get_fps())
        
        pygame.display.update()

        print(f"Framerate: {framerate:6d} \t Frame: {frame_counter:6d} / {n_frames:6d}\t Frame Offset: {frame_offset:6d}", end='\r')

        if not paused:
            clock.tick(framerate)
            frame_counter += 1
            if frame_counter >= n_frames:
                frame_counter = 0
    
    visualizer.self_close = True
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deliveroo2 Replay System")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    args = parser.parse_args()

    agent = 'agent_1'
    load_belief_sets(args.folder, agent=agent)
    load_memories(args.folder, agent=agent)
    load_evolution_steps(args.folder, agent=agent)

    pygame.init()

    game = Game(args.folder)

    graphics = Graphics(game)
    
    pygame.display.set_caption("Deliveroo2")
    clock = pygame.time.Clock()

    app = QApplication(sys.argv)
    visualizer = RealTimeVisualizer()

    game_loop(game, graphics, clock, visualizer)