import sys
import time
import signal
import argparse
import threading
from utils.Logger import ExperimentLogger
from utils.Communication import Communication
from PyQt5.QtWidgets import QApplication
from utils.Visualizer import RealTimeVisualizer
from agent_dir.perception import Perception
from agent_dir.control import Control
from agent_dir.utils.Prompting import Prompting


running = True
def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def receive_events(communication, perception, visualizer):
    while running:
        if len(communication.buffer) > 0:
            msg, addr = communication.buffer.pop(0)
            if msg.split()[0] == "connected":
                logger.log_info(f"Connected to server as agent ID: {msg.split()[1]}")
            else:
                perception.append_event(msg)
        else:
            time.sleep(0.1)
    visualizer.self_close = True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deliveroo2 Agent")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help="Host address of the server")
    parser.add_argument('--port', type=int, required=True, help="Port number of the agent")
    parser.add_argument('--server-port', type=int, required=True, help="Port number of the server")
    parser.add_argument('--user-generated-desire', required=True, help="Use user-generated desire")
    parser.add_argument('--stateless-intention-generation', required=True, help="Use stateless intention generation")
    parser.add_argument('--no-desire-triggering', required=True, help="Disable desire triggering")
    parser.add_argument('--perception-generation-only-on-error', required=True, help="Generate perception only on error")
    args = parser.parse_args()

    logger = ExperimentLogger(args.folder, 'agent.log')
    logger.log_debug("Agent started")

    communication = Communication(args.folder, args.host, args.port, args.server_port)

    while running:
        communication.send_to_server("connect")
        time.sleep(0.1)
        if len(communication.buffer) > 0:
            msg, addr = communication.buffer.pop(0)
            msg = msg.split()
            if msg[0] == "connected":
                logger.log_info(f"Connected to server as agent ID: {msg[1]}")
                break

    prompting = Prompting(args.folder)
    perception = Perception(args.folder, communication, prompting, args.perception_generation_only_on_error)
    control = Control(args.folder, communication, prompting, perception.get_control_events, perception.get_belief_set, args.user_generated_desire, args.stateless_intention_generation, args.no_desire_triggering)
    logger.log_debug("Perception and control units started")


    app = QApplication(sys.argv)
    visualizer = RealTimeVisualizer(perception, control, args.folder)
    
    listener = threading.Thread(target=receive_events, args=(communication, perception, visualizer))
    listener.start()
    
    app.exec_()
    
    listener.join()

    perception.stop = True
    control.stop = True
    prompting.stop = True
    while perception.is_alive() or control.is_alive():
        time.sleep(0.1)
    logger.log_debug("Perception and control units terminated")
    
    communication.send_to_server("disconnect")
    communication.close()
    logger.log_debug("Agent terminated")




'''
Need to track:
perception.get_printable_belief_set()
perception.manager.get_printable_functions()
control.manager.get_printable_intentions()
control.manager.get_printable_desires()
control.manager.get_printable_intentions_graph()
'''