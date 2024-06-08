import threading

class Control:
    def __init__(self, server):
        self.server = server

        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.main_loop, args=())
        self.thread.start()

    def main_loop(self):
        while not self.stop_event.is_set():

            import random
            import time
            time.sleep(1)
            actions = ['moveleft', 'moveright', 'moveup', 'movedown', 'pickup', 'putdown']
            action = random.choice(actions)
            self.send_action(action)
        
        print("Control exited correctly.")
        exit()
    
    def send_action(self, action):
        self.server.send(action)
    
    def close(self):
        self.stop_event.set()
