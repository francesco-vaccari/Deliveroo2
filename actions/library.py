import json
import re
import time
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Action:
    def __init__(self, function_name, description, action_name):
        self.function_name = function_name
        self.description = description
        self.action_name = action_name

class Function:
    def __init__(self, function_name, function_string, description):
        self.function_name = function_name
        self.function_string = function_string
        self.description = description

class FunctionsGraph:
    def __init__(self):
        self.id = 0
        self.nodes = {} # key is function_name, value is the id
        self.edges = {} # key is the id, value is a set of ids
    
    def add_function(self, function_name, function_string, library_function_names):
        library_function_names = set(library_function_names)
        functions_called = self.extract_function_calls(function_string, library_function_names)
        self.add_node(function_name)
        for function_called in functions_called:
            self.add_edge(function_name, function_called)
        print(self.nodes)
        print(self.edges)
        print("\n\n")
        self.draw_directed_graph()
    
    def add_base_action(self, function_name):
        self.add_node(function_name)
        print(self.nodes)
        print(self.edges)
        print("\n\n")
        self.draw_directed_graph()

    def extract_function_calls(self, function_string, allowed_functions):
        function_call_pattern = re.compile(r'\b(\w+)\s*\(')
        matches = function_call_pattern.findall(function_string)
        function_name = re.match(r'def\s+(\w+)\s*\(', function_string).group(1)
        called_functions = [match for match in matches if match != function_name]
        valid_called_functions = [func for func in called_functions if func in allowed_functions]
        return valid_called_functions
    
    def add_node(self, function_name):
        if function_name not in self.nodes:
            self.nodes[function_name] = self.id
            self.edges[self.id] = set()
            self.id += 1
    
    def add_edge(self, function_name_1, function_name_2):
        id_1 = self.nodes[function_name_1]
        id_2 = self.nodes[function_name_2]
        self.edges[id_1].add(id_2)
    
    def draw_directed_graph(self):
        G = nx.DiGraph()
        for node_name, node_number in self.nodes.items():
            G.add_node(node_number, label=node_name)
        for node_number, linked_nodes in self.edges.items():
            for linked_node in linked_nodes:
                G.add_edge(node_number, linked_node)
        
        labels = {node_number: node_name for node_name, node_number in self.nodes.items()}
        
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(10,7))
        
        nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', edgecolors='black')
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='black')
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_weight='bold')
        plt.savefig(f'functions_graph_{time.time()}.png', format='PNG', bbox_inches='tight')
        plt.close()

class Library:
    def __init__(self, base_actions_path):
        self.functions_graph = FunctionsGraph()
        self.library_base_actions = self.load_library_base(base_actions_path)
        self.library = {}

    def load_library_base(self, path):
        library = {}
        config = json.load(open(path))
        actions = config["actions"]
        for action in actions:
            function_name = action["function_name"]
            description = action["description"]
            action_name = action["action_name"]
            library[function_name] = Action(function_name, description, action_name)
            self.functions_graph.add_base_action(function_name)
        return library

    def update_library(self, function_name, function_string, intention):
        new_function = Function(function_name, function_string, intention)
        self.library[function_name] = new_function
        self.functions_graph.add_function(function_name, function_string, self.get_list_function_names())
        return new_function
    
    def get_unified_library(self):
        unified_library = dict(self.library_base_actions)
        unified_library.update(self.library)
        return unified_library
    
    def get_test_file_content(self):
        content = ""
        for _, action in self.library_base_actions.items():
            content += f"def {action.function_name}(belief_set):\n"
            content += f"    # test function definition\n"
            content += f"    pass\n\n"
        
        for _, function in self.library.items():
            content += function.function_string
            content += "\n\n"
        
        return content
    
    def get_file_content(self):
        content = "plan = []\n\n"
        for _, action in self.library_base_actions.items():
            content += f"def {action.function_name}(belief_set):\n"
            content += f"    global plan\n"
            content += f"    plan.append('{action.action_name}')\n\n"
        
        for _, function in self.library.items():
            content += function.function_string
            content += "\n\n"
        
        return content

    def get_list_function_names(self):
        names = []
        for _, action in self.library_base_actions.items():
            names.append(action.function_name)
        
        for _, function in self.library.items():
            names.append(function.function_name)

        return names

    def get_dump(self): # to change in get_content_for_prompt
        dump = {}
        for _, action in self.library_base_actions.items():
            dump[action.function_name] = {"function_name": action.function_name, "description": action.description, "action_name": action.action_name}
        
        for _, function in self.library.items():
            dump[function.function_name] = {"function_name": function.function_name, "function_string": function.function_string, "description": function.description}
        
        return dump