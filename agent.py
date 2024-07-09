from communication import Communication
import signal
from agent_dir.perception import Perception
from agent_dir.control import Control
import argparse

class Agent:
    def __init__(self, address, server_port, port):
        self.HOST = address
        self.SERVER_PORT = server_port
        self.PORT = port

        # start up the communication with the server and the perception and control threads
        self.server = Communication(self.HOST, self.PORT, self.SERVER_PORT)
        self.server.send("connect", (self.HOST, self.SERVER_PORT))
        self.perception = Perception(self.server)
        self.control = Control(self.server, self.perception)

        signal.signal(signal.SIGINT, self.signal_handler)

        self.handle_messages()

        self.server.server_thread.join()
        print("Exited correctly.")
    
    def signal_handler(self, sig, frame):
        self.server.send("disconnect", (self.HOST, self.SERVER_PORT))
        self.server.send("exit", (self.HOST, self.PORT))
        self.perception.close()
        self.control.close()
        self.server.server_thread.join()
        print("Exited correctly.")
        exit()

    def handle_messages(self):
        while self.server.is_open:

            if len(self.server.buffer) > 0:
                msg, addr = self.server.buffer.pop(0)
                temp = msg.split()
                
                if temp[0] == 'error':
                    print("An error occured with the server.")
                elif temp[0] == 'connected':
                    print("Connected as agent: ", temp[1])
                else:
                    self.perception.events.append(msg)
        
        self.perception.close()
        self.control.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deliveroo2 Agent")
    parser.add_argument('--server_port', type=int, required=False, help="Port of the server", default=8080)
    parser.add_argument('--port', type=int, required=True, help="Port for the agent")
    args = parser.parse_args()

    agent = Agent('127.0.0.1', args.server_port, args.port)