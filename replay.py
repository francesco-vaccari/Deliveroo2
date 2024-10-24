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


running = True
frame_counter = 0
framerate = 60
info = {}

def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

import os
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea, QApplication

# class RealTimeVisualizer(QWidget):
#     def __init__(self, perception, control, prompting, folder):
#         super().__init__()
#         self.perception = perception
#         self.control = control
#         self.prompting = prompting

#         self.folder = folder

#         self.desire_steps = []
#         self.intention_steps = []
#         self.number_api_calls = []
#         self.number_desires_working = []
#         self.number_desires_not_working = []
#         self.number_intentions_working = []
#         self.number_intentions_not_working = []
#         self.number_perception_functions = []

#         self.self_close = False

#         self.initUI()
        
#     def initUI(self):
#         self.layout = QVBoxLayout()

#         self.API_calls = QScrollArea()
#         self.API_calls_label = QLabel("API Calls:")
#         self.API_calls.setWidget(self.API_calls_label)
#         self.API_calls.setWidgetResizable(True)
#         self.API_calls.setMaximumHeight(30)
#         self.API_calls_label.setWordWrap(True)

#         self.perception_status = QScrollArea()
#         self.control_status = QScrollArea()
#         perception_status_label = QLabel("Perception Status:")
#         control_status_label = QLabel("Control Status:")
#         self.perception_status.setWidget(perception_status_label)
#         self.control_status.setWidget(control_status_label)
#         self.perception_status.setWidgetResizable(True)
#         self.control_status.setWidgetResizable(True)
#         self.perception_status.setMaximumHeight(50)
#         self.control_status.setMaximumHeight(50)
#         self.perception_status.setVisible(True)
#         self.control_status.setVisible(True)
#         perception_status_label.setWordWrap(True)
#         control_status_label.setWordWrap(True)

#         self.buttons_layout = QVBoxLayout()
#         self.button1 = QPushButton("Show Belief Set")
#         self.button2 = QPushButton("Show Perception Functions")
#         self.button3 = QPushButton("Show Intentions")
#         self.button4 = QPushButton("Show Desires")
#         self.button5 = QPushButton("Show Intentions Graph")
#         self.button6 = QPushButton("Show Memory")
        
#         self.button1.clicked.connect(lambda: self.show_widget(self.scroll1))
#         self.button2.clicked.connect(lambda: self.show_widget(self.scroll2))
#         self.button3.clicked.connect(lambda: self.show_widget(self.scroll3))
#         self.button4.clicked.connect(lambda: self.show_widget(self.scroll4))
#         self.button5.clicked.connect(lambda: self.show_widget(self.scroll5))
#         self.button6.clicked.connect(lambda: self.show_widget(self.scroll6))
        
#         self.buttons_layout.addWidget(self.button1)
#         self.buttons_layout.addWidget(self.button2)
#         self.buttons_layout.addWidget(self.button3)
#         self.buttons_layout.addWidget(self.button4)
#         self.buttons_layout.addWidget(self.button5)
#         self.buttons_layout.addWidget(self.button6)
        
#         self.layout.addLayout(self.buttons_layout)

#         self.scroll1 = self.create_scrollable_label("Belief Set")
#         self.scroll2 = self.create_scrollable_label("Perception Functions")
#         self.scroll3 = self.create_scrollable_label("Intentions")
#         self.scroll4 = self.create_scrollable_label("Desires")
#         self.scroll5 = self.create_scrollable_label("Intentions Graph")
#         self.scroll6 = self.create_scrollable_label("Memory")

#         self.layout.addWidget(self.API_calls)
#         self.layout.addWidget(self.perception_status)
#         self.layout.addWidget(self.control_status)
#         self.layout.addWidget(self.scroll1)
#         self.layout.addWidget(self.scroll2)
#         self.layout.addWidget(self.scroll3)
#         self.layout.addWidget(self.scroll4)
#         self.layout.addWidget(self.scroll5)
#         self.layout.addWidget(self.scroll6)
        
#         self.setLayout(self.layout)

#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_labels)
#         self.timer.start(1000)

#         self.setWindowTitle(self.folder.split("/")[-1])
#         self.show()
        
#         self.show_widget(self.scroll1)  # Show the first widget by default

#     def create_scrollable_label(self, text):
#         scroll = QScrollArea()
#         label = QLabel(text)
#         label.setWordWrap(True)
#         scroll.setWidget(label)
#         scroll.setWidgetResizable(True)
#         scroll.setVisible(False)
#         return scroll

#     def show_widget(self, widget):
#         self.scroll1.setVisible(False)
#         self.scroll2.setVisible(False)
#         self.scroll3.setVisible(False)
#         self.scroll4.setVisible(False)
#         self.scroll5.setVisible(False)
#         self.scroll6.setVisible(False)
#         widget.setVisible(True)

#     def update_labels(self):
#         api_calls = self.prompting.get_printable_estimate()
#         perception_status = self.perception.status
#         control_status = self.control.status

#         self.API_calls_label.setText(f"API Calls: {api_calls}")
#         self.perception_status.widget().setText(f"Perception Status: {perception_status}")
#         self.control_status.widget().setText(f"Control Status: {control_status}")

#         var1_value = self.perception.get_printable_belief_set()
#         var2_value = self.perception.manager.get_printable_functions()
#         var3_value = self.control.manager.get_printable_intentions()
#         var4_value = self.control.manager.get_printable_desires()
#         var5_value = self.control.manager.get_printable_intentions_graph()
#         var6_value = self.control.get_printable_memory()

#         self.scroll1.widget().setText(f"{var1_value}")
#         self.scroll2.widget().setText(f"{var2_value}")
#         self.scroll3.widget().setText(f"{var3_value}")
#         self.scroll4.widget().setText(f"{var4_value}")
#         self.scroll5.widget().setText(f"{var5_value}")
#         self.scroll6.widget().setText(f"{var6_value}")

#         self.desire_steps.append(self.control.desire_steps)
#         self.intention_steps.append(self.control.intention_steps)
#         self.number_api_calls.append(self.prompting.get_requests_made())
#         working, not_working = self.control.manager.get_number_desires()
#         self.number_desires_working.append(working)
#         self.number_desires_not_working.append(not_working)
#         working, not_working = self.control.manager.get_number_intentions()
#         self.number_intentions_working.append(working)
#         self.number_intentions_not_working.append(not_working)
#         self.number_perception_functions.append(self.perception.manager.get_number_perception_functions())

#         if self.self_close:
#             os.makedirs(f"{self.folder}/result", exist_ok=True)
#             with open(f"{self.folder}/result/api_calls.txt", "w") as f:
#                 f.write(str(api_calls))
#                 f.close()
#             with open(f"{self.folder}/result/belief_set.txt", "w") as f:
#                 f.write(var1_value)
#                 f.close()
#             with open(f"{self.folder}/result/perception_functions.txt", "w") as f:
#                 f.write(var2_value)
#                 f.close()
#             with open(f"{self.folder}/result/intentions.txt", "w") as f:
#                 f.write(var3_value)
#                 f.close()
#             with open(f"{self.folder}/result/desires.txt", "w") as f:
#                 f.write(var4_value)
#                 f.close()
#             with open(f"{self.folder}/result/intentions_graph.txt", "w") as f:
#                 f.write(var5_value)
#                 f.close()
#             with open(f"{self.folder}/result/memory.txt", "w") as f:
#                 f.write(var6_value)
#                 f.close()
                
#             all, all_working, all_not_working, intentions, working_intentions, not_working_intentions = self.control.manager.get_analyzable_intentions_functions()
#             with open(f"{self.folder}/result/analyzable_IF.py", "w") as f:
#                 f.write(all)
#                 f.close()
#             with open(f"{self.folder}/result/analyzable_IF_W.py", "w") as f:
#                 f.write(all_working)
#                 f.close()
#             with open(f"{self.folder}/result/analyzable_IF_NW.py", "w") as f:
#                 f.write(all_not_working)
#                 f.close()
#             os.makedirs(f"{self.folder}/result/analyzable_IF_S", exist_ok=True)
#             for key, value in intentions.items():
#                 with open(f"{self.folder}/result/analyzable_IF_S/{key}.py", "w") as f:
#                     f.write(value)
#                     f.close()
#             os.makedirs(f"{self.folder}/result/analyzable_IF_W_S", exist_ok=True)
#             for key, value in working_intentions.items():
#                 with open(f"{self.folder}/result/analyzable_IF_W_S/{key}.py", "w") as f:
#                     f.write(value)
#                     f.close()
#             os.makedirs(f"{self.folder}/result/analyzable_IF_NW_S", exist_ok=True)
#             for key, value in not_working_intentions.items():
#                 with open(f"{self.folder}/result/analyzable_IF_NW_S/{key}.py", "w") as f:
#                     f.write(value)
#                     f.close()
            
#             string, dictionary = self.control.manager.get_analyzable_desires_trigger_functions()
#             with open(f"{self.folder}/result/analyzable_DTF.py", "w") as f:
#                 f.write(string)
#                 f.close()
#             os.makedirs(f"{self.folder}/result/analyzable_DTF_S", exist_ok=True)
#             for key, value in dictionary.items():
#                 with open(f"{self.folder}/result/analyzable_DTF_S/{key}.py", "w") as f:
#                     f.write(value)
#                     f.close()
            
#             string, dictionary = self.perception.manager.get_analyzable_perception_functions()
#             with open(f"{self.folder}/result/analyzable_PF.py", "w") as f:
#                 f.write(string)
#                 f.close()
#             os.makedirs(f"{self.folder}/result/analyzable_PF_S", exist_ok=True)
#             for key, value in dictionary.items():
#                 with open(f"{self.folder}/result/analyzable_PF_S/{key}.py", "w") as f:
#                     f.write(value)
#                     f.close()

#             with open(f"{self.folder}/result/evolution_steps.txt", "w") as f:
#                 f.write(str(self.desire_steps) + "\n")
#                 f.write(str(self.intention_steps) + "\n")
#                 f.write(str(self.number_api_calls) + "\n")
#                 f.write(str(self.number_desires_working) + "\n")
#                 f.write(str(self.number_desires_not_working) + "\n")
#                 f.write(str(self.number_intentions_working) + "\n")
#                 f.write(str(self.number_intentions_not_working) + "\n")
#                 f.write(str(self.number_perception_functions) + "\n")
#                 f.close()
            
#             self.timer.stop()
#             self.close()


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

def load_info(folder, agent='agent_1'):
    global info
    server_log_file = os.path.join("experiments", args.folder, "server.log")
    with open(server_log_file, 'r') as file:
        start_time = get_time(file.readline())
        file.close()

    control_log_file = os.path.join("experiments", args.folder, agent, "control_manager.log")
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

    info = {}

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
            error = extract_from_string("Error during intention ", "", line)
            last_error = error
        
        if str(last_desire) != last_desire_str or str(last_intentions) != last_intentions_str or str(last_actions) != last_actions_str or str(last_error) != last_error_str:
            info[time] = {"desire": last_desire, "intentions": last_intentions, "actions": last_actions, "error": last_error}
            last_desire_str = str(last_desire)
            last_intentions_str = str(last_intentions)
            last_actions_str = str(last_actions)
            last_error_str = str(last_error)

            info[get_n_frame(start_time, time)] = {"desire": last_desire, "intentions": last_intentions, "actions": last_actions, "error": last_error}

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
    global info
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

        print(f"Framerate: {framerate:4d} \t Frame: {frame_counter:4d} / {n_frames:4d}")
        if frame_counter in info.keys():
            print(info[frame_counter])


        clock.tick(framerate)
        frame_counter += 1
        if frame_counter >= n_frames:
            frame_counter = 0
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deliveroo2 Replay System")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    args = parser.parse_args()

    load_info(args.folder, agent='agent_1')

    pygame.init()

    game = Game(args.folder)

    graphics = Graphics(game)
    
    pygame.display.set_caption("Deliveroo2")
    clock = pygame.time.Clock()

    game_loop(game, graphics, clock)




# def receive_events(visualizer):
#     global running
#     while running:
#         do stuff
        
#         if exit:
#             running = False
    
#     visualizer.self_close = True


# app = QApplication(sys.argv)
# visualizer = RealTimeVisualizer(info)

# listener = threading.Thread(target=receive_events, args=(visualizer))
# listener.start()
    
# app.exec_()

# listener.join()

