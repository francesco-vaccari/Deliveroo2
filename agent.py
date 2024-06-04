from communication import Communication
import signal
import argparse
from perception import Perception
from control import Control

parser = argparse.ArgumentParser(description="LLMbAA agent")
parser.add_argument('--server-port', type=int, required=False, help="Port for the server", default=8080)
parser.add_argument('--port', type=int, required=False, help="Port for the agent", default=8081)
args = parser.parse_args()

HOST = '127.0.0.1'
SERVER_PORT = args.server_port
PORT = args.port

# start up the communication with the server and the perception and control threads
server = Communication(HOST, PORT, SERVER_PORT)
server.send("connect", (HOST, SERVER_PORT))
perception = Perception(server)
control = Control(server)


# set the SIGINT handler
def signal_handler(sig, frame):
    server.send("disconnect", (HOST, SERVER_PORT))
    server.send("exit", (HOST, PORT))
    perception.close()
    control.close()
    server.server_thread.join()
    print("Exited correctly.")
    exit()
signal.signal(signal.SIGINT, signal_handler)


# handle messages and events received from the server
def handle_messages():
    while server.is_open:

        if len(server.buffer) > 0:
            msg, addr = server.buffer.pop(0)
            temp = msg.split()
            
            if temp[0] == 'error':
                print("An error occured with the server.")
            elif temp[0] == 'connected':
                print("Connected as agent: ", temp[1])
            else:
                perception.events.append(msg)
    
    perception.close()
    control.close()
handle_messages()


# wait for the server listening thread to exit
server.server_thread.join()
print("Exited correctly.")
exit()