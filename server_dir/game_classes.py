import random
import json
import copy

class Game:
    def __init__(self, map_conf_path, parcels_conf_path, folder):
        self.replay = {}
        self.replay_frame = 0
        self.replay_file = folder + '/replay.json'
        self.last_entities_string_values = ["", "", ""]

        self.map = Map(map_conf_path)
        self.parcels = []
        self.agents = []
        
        with open(parcels_conf_path) as f:
            self.spawning_rate = int(f.readline())
            self.score_range = f.readline().split()
            self.decay_rate = int(f.readline())
        
        
        self.agents_ids = 1
        self.parcels_ids = 1

        self.decay_timer = 0
        self.spawn_timer = 0

        self.entities_to_track = [self.map, self.parcels, self.agents]
        self.entities_labels = ["map", "parcels", "agents"]
        self.environment_state = []
        self.set_initial_state()
    
    def log_state(self):
        self.replay[str(self.replay_frame)] = {}

        if str(self.map.dump()) != self.last_entities_string_values[0]:
            self.replay[str(self.replay_frame)]['map'] = self.map.dump()
            self.last_entities_string_values[0] = str(self.map.dump())
            
        if str([parcel.dump() for parcel in self.parcels]) != self.last_entities_string_values[1]:
            self.replay[str(self.replay_frame)]['parcels'] = [parcel.dump() for parcel in self.parcels]
            self.last_entities_string_values[1] = str([parcel.dump() for parcel in self.parcels])
        
        if str([agent.dump() for agent in self.agents]) != self.last_entities_string_values[2]:
            self.replay[str(self.replay_frame)]['agents'] = [agent.dump() for agent in self.agents]
            self.last_entities_string_values[2] = str([agent.dump() for agent in self.agents])
        
        self.replay_frame += 1

    def write_replay_file(self):
        with open(self.replay_file, 'w') as f:
            json.dump(self.replay, f)
            f.close()
    
    def new_agent(self):
        agent = Agent(self.agents_ids)
        self.agents_ids += 1
        count = 0
        for row in self.map.grid:
            for cell in row:
                if cell == 1 or cell == 2:
                    count += 1
        if count == 0:
            return 0
        rand = random.randint(0, count-1)
        count = 0
        for x, row in enumerate(self.map.grid):
            for y, cell in enumerate(row):
                if cell == 1 or cell == 2:
                    if count == rand:
                        agent.x = x
                        agent.y = y
                        self.agents.append(agent)
                        return agent.id
                    count += 1
    
    def new_parcel(self):
        parcel = Parcel(self.parcels_ids, 0, 0, random.randint(int(self.score_range[0]), int(self.score_range[1])))
        self.parcels_ids += 1
        count = 0
        for row in self.map.grid:
            for cell in row:
                if cell == 1:
                    count += 1
        if count == 0:
            return 0
        rand = random.randint(0, count-1)
        count = 0
        for x, row in enumerate(self.map.grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    if count == rand:
                        parcel.x = x
                        parcel.y = y
                        self.parcels.append(parcel)
                        return parcel.id
                    count += 1
    
    def remove_agent(self, id):
        for agent in self.agents:
            if agent.id == id:
                self.agents.remove(agent)
                return

    def agent_move_left(self, id):
        for agent in self.agents:
                if agent.id == id:
                    if agent.y - 1 >= 0:
                        if self.map.grid [agent.x][agent.y - 1] != 0:
                            for someone_else in self.agents:
                                if someone_else.x == agent.x and someone_else.y == agent.y - 1:
                                    return False
                            agent.y -= 1
                            for parcel in self.parcels:
                                if parcel.carried_by == agent.id:
                                    parcel.y -= 1
                            return True
        return False
    
    def agent_move_right(self, id):
        for agent in self.agents:
                if agent.id == id:
                    if agent.y + 1 < self.map.width:
                        if self.map.grid [agent.x][agent.y + 1] != 0:
                            for someone_else in self.agents:
                                if someone_else.x == agent.x and someone_else.y == agent.y + 1:
                                    return False
                            agent.y += 1
                            for parcel in self.parcels:
                                if parcel.carried_by == agent.id:
                                    parcel.y += 1
                            return True
        return False

    def agent_move_up(self, id):
        for agent in self.agents:
                if agent.id == id:
                    if agent.x - 1 >= 0:
                        if self.map.grid [agent.x - 1][agent.y] != 0:
                            for someone_else in self.agents:
                                if someone_else.x == agent.x - 1 and someone_else.y == agent.y:
                                    return False
                            agent.x -= 1
                            for parcel in self.parcels:
                                if parcel.carried_by == agent.id:
                                    parcel.x -= 1
                            return True
        return False
    
    def agent_move_down(self, id):
        for agent in self.agents:
                if agent.id == id:
                    if agent.x + 1 < self.map.height:
                        if self.map.grid [agent.x + 1][agent.y] != 0:
                            for someone_else in self.agents:
                                if someone_else.x == agent.x + 1 and someone_else.y == agent.y:
                                    return False
                            agent.x += 1
                            for parcel in self.parcels:
                                if parcel.carried_by == agent.id:
                                    parcel.x += 1
                            return True
        return False

    def agent_pick_up(self, agent_id):
        res = False
        for agent in self.agents:
            if agent.id == agent_id:
                for parcel in self.parcels:
                    if parcel.x == agent.x and parcel.y == agent.y and parcel.carried_by == None:
                        parcel.carried_by = agent.id
                        parcel.to_draw = False
                        parcel.to_draw_on_agent = True
                        agent.parcels_carried.append(parcel.id)
                        res = True
        return res # True if at least one parcel was picked up

    def agent_put_down(self, agent_id):
        res = False
        for agent in self.agents:
            if agent.id == agent_id:
                for parcel_id in agent.parcels_carried:
                    for parcel in self.parcels:
                        if parcel.id == parcel_id:
                            if self.map.grid[agent.x][agent.y] == 2:
                                agent.score += parcel.score
                                self.parcels.remove(parcel)
                                res = True
                            else:
                                parcel.x = agent.x
                                parcel.y = agent.y
                                parcel.carried_by = None
                                parcel.to_draw = True
                                parcel.to_draw_on_agent = False
                                res = True
                agent.parcels_carried = []
        return res # True if at least one parcel was put down

    def print_map(self):
        self.map.print_map()
    
    def print_parcels(self):
        for parcel in self.parcels:
            parcel.print_parcel()
    
    def print_agents(self):
        for agent in self.agents:
            agent.print_agent()
    
    def decay_parcels(self):
        if self.decay_rate != 0:
            self.decay_timer += 1
            if self.decay_timer == self.decay_rate:
                for parcel in self.parcels:
                    parcel.score -= 1
                    if parcel.score == 0:
                        self.parcels.remove(parcel)
                        for agent in self.agents:
                            for p_id in agent.parcels_carried:
                                if p_id == parcel.id:
                                    agent.parcels_carried.remove(p_id)
                self.decay_timer = 0

    def spawn_parcels(self):
        self.spawn_timer += 1
        if self.spawn_timer == self.spawning_rate:
            self.new_parcel()
            self.spawn_timer = 0

    def set_initial_state(self):
        for element in self.entities_to_track:
            if type(element) is list:
                self.environment_state.append([copy.deepcopy(object) for object in element])
            else:
                self.environment_state.append(copy.deepcopy(element))

    def set_new_state(self):
        self.log_state()
        new_state = []
        for element in self.entities_to_track:
            if type(element) is list:
                new_state.append([copy.deepcopy(object) for object in element])
            else:
                new_state.append(copy.deepcopy(element))
        
        self.diff_state = []
        self.diff_types = []

        for i, element in enumerate(new_state):
            if type(element) is list:
                for object in element:
                    index = object.is_in_list(self.environment_state[i])
                    if index != -1:
                        if not object.is_equal(self.environment_state[i][index]):
                            self.diff_state.append(object)
                            self.diff_types.append('object changed')
                    else:
                        self.diff_state.append(object)
                        self.diff_types.append('object added')
            else:
                if not element.is_equal(self.environment_state[i]):
                    self.diff_state.append(element)
                    self.diff_types.append('object changed')
        
        for i, element in enumerate(self.environment_state):
            if type(element) is list:
                for object in element:
                    if object.is_in_list(new_state[i]) == -1:
                        self.diff_state.append(object)
                        self.diff_types.append('object removed')
        
        self.environment_state = new_state
    
    def create_events(self):
        self.events = []
        for i, object in enumerate(self.diff_state):
            event = object.get_event(self.diff_types[i])
            self.events.append(json.dumps(event))

    def get_events(self):
        events = self.events
        self.events = []
        return events
    
    def get_state(self):
        state = []
        for i, element in enumerate(self.environment_state):
            if type(element) is list:
                for object in element:
                    state.append(json.dumps(object.get_event('object added')))
            else:
                state.append(json.dumps(element.get_event('object added')))
        return state
    

class Map:
    def __init__(self, map_conf_path=None):
        self.width = 0
        self.height = 0
        self.grid = []
        if map_conf_path:
            with open(map_conf_path) as f:
                self.width = int(f.readline())
                self.height = int(f.readline())
                for line in f:
                    self.grid.append([int(cell) for cell in line.split()])
    
    def print_map(self):
        print("Map size: ", self.width, self.height)
        for row in self.grid:
            print(' '.join(str(cell) for cell in row)
        )

    def is_equal(self, map):
        if self.width == map.width and self.height == map.height:
            for x in range(self.width):
                for y in range(self.height):
                    if self.grid[x][y] != map.grid[x][y]:
                        return False
            return True
        return False

    def copy(self):
        map = Map()
        map.width = self.width
        map.height = self.height
        map.grid = copy.deepcopy(self.grid)
        return map

    def get_event(self, event_type):
        grid = []
        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                cell_type = ''
                if cell == 1:
                    cell_type = 'walkable'
                elif cell == 2:
                    cell_type = 'deliverable'
                else:
                    cell_type = 'non-walkable'
                grid.append({'cell_coordinates': [x, y], 'cell_type': cell_type})
        event = {
            "event_type": event_type,
            "object_type": "map",
            "object": {
                "width": self.width,
                "height": self.height,
                "grid": grid
            }
        }
        return event
    
    def dump(self):
        return {
            "width": self.width,
            "height": self.height,
            "grid": self.grid
        }


class Agent:
    def __init__(self, id):
        self.id = id
        self.x = None
        self.y = None
        self.parcels_carried = []
        self.score = 0
    
    def print_agent(self):
        text = "Agent id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " score: " + str(self.score) + " carrying: " + str(self.parcels_carried)
        return text
    
    def is_equal(self, agent):
        if self.id == agent.id and self.x == agent.x and self.y == agent.y and self.score == agent.score:
            if len(self.parcels_carried) == len(agent.parcels_carried):
                for parcel in self.parcels_carried:
                    if parcel not in agent.parcels_carried:
                        return False
                return True
        return False
    
    def is_in_list(self, agents):
        for i, agent in enumerate(agents):
            if self.id == agent.id:
                return i
        return -1
    
    def copy(self):
        agent = Agent(self.id)
        agent.x = self.x
        agent.y = self.y
        agent.parcels_carried = copy.deepcopy(self.parcels_carried)
        agent.score = self.score
        return agent
    
    def get_event(self, event_type):
        event = {
            "event_type": event_type,
            "object_type": "agent",
            "object": {
                "id": self.id,
                "coordinates": [self.x, self.y],
                "parcels_carried_ids": self.parcels_carried,
                "score": self.score
            }
        }
        return event

    def dump(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "parcels_carried": self.parcels_carried,
            "score": self.score
        }

class Parcel:
    def __init__(self, id, x, y, score):
        self.id = id
        self.x = x
        self.y = y
        self.score = score
        self.carried_by = None
        self.to_draw = True
        self.to_draw_on_agent = False
    
    def print_parcel(self):
        text = "Parcel id: " + str(self.id) + " x: " + str(self.x) + " y: " + str(self.y) + " score: " + str(self.score) + " carried by: " + str(self.carried_by)
        return text

    def is_equal(self, parcel):
        if self.id == parcel.id and self.x == parcel.x and self.y == parcel.y and self.score == parcel.score and self.carried_by == parcel.carried_by:
            return True
        return False

    def is_in_list(self, parcels):
        for i, parcel in enumerate(parcels):
            if self.id == parcel.id:
                return i
        return -1

    def copy(self):
        parcel = Parcel(self.id, self.x, self.y, self.score)
        parcel.carried_by = self.carried_by
        return parcel
    
    def get_event(self, event_type):
        event = {
            "event_type": event_type,
            "object_type": "parcel",
            "object": {
                "id": self.id,
                "coordinates": [self.x, self.y],
                "score": self.score,
                "carried_by_id": self.carried_by
            }
        }
        return event

    def dump(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "score": self.score,
            "carried_by_id": self.carried_by if self.carried_by is not None else 0,
            "to_draw": self.to_draw,
            "to_draw_on_agent": self.to_draw_on_agent
        }



'''
Traccio lo stato dell'ambiente, ovvero gli agenti, le parcelle e la mappa.

Ad ogni frame viene controllato se qualcosa contenuto in queste variabili è cambiato e 
viene mandato un evento se qualcosa è cambiato.

Abbiamo diversi tipi di eventi:
- object added
- object removed
- object changed

Questo dovrebbe coprire i casi in cui un oggetto viene spawnato, come parcelle o agenti 
che si connettono, e oggetti che spariscono, come un agente che si disconnette o una 
parcella che scade. Il resto server per informare gli agenti dei cambiamenti nell'ambiente.

Oltre ad avere un tipo di evento, c'è anche un tipo dell'oggetto coinvolto nell'evento, e
questi tipi possono essere per il momento:
- parcella
- agente
- mappa

'''