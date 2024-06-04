import threading

class Perception:
    def __init__(self, server):
        self.server = server
        self.events = []
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.main_loop, args=())
        self.thread.start()

    def main_loop(self):
        while not self.stop_event.is_set():
            if len(self.events) > 0:
                new_event = self.events.pop(0)
                print(new_event)
        
        print("Perception exited correctly.")
        exit()
    
    def close(self):
        self.stop_event.set()
        
