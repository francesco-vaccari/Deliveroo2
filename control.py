import threading

class Control:
    def __init__(self, server, belief_set):
        self.server = server

        self.belief_set = belief_set

        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.main_loop, args=())
        self.thread.start()

    def main_loop(self):
        while not self.stop_event.is_set():

            print(self.belief_set)
            import time
            time.sleep(1)
            
            # chiedere desire

            # chiedere funzione

            # testare funzione

            # testare piano

            # valutare funzione

            # valutare desire

            pass
        
        print("Control exited correctly.")
        exit()
    
    def send_action(self, action):
        self.server.send(action)
    
    def close(self):
        self.stop_event.set()
