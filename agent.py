import time
import signal
import argparse
from utils.Logger import ExperimentLogger
from utils.Communication import Communication
from agent_dir.perception import Perception
from agent_dir.control import Control
from agent_dir.utils.Prompting import Prompting


running = True
def signal_handler(sig, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deliveroo2 Agent")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help="Host address of the server")
    parser.add_argument('--port', type=int, required=True, help="Port number of the agent")
    parser.add_argument('--server-port', type=int, required=True, help="Port number of the server")
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

    prompting = Prompting()
    perception = Perception(args.folder, communication, prompting)
    control = Control(args.folder, communication, prompting, perception.get_control_events, perception.get_belief_set)
    logger.log_debug("Perception and control units started")

    while running:
        if len(communication.buffer) > 0:
            msg, addr = communication.buffer.pop(0)
            if msg.split()[0] == "connected":
                logger.log_info(f"Connected to server as agent ID: {msg.split()[1]}")
            else:
                perception.append_event(msg)
        else:
            time.sleep(0.1)

    perception.stop = True
    control.stop = True
    prompting.stop = True
    while perception.is_alive() or control.is_alive():
        time.sleep(0.1)
    logger.log_debug("Perception and control units terminated")
    
    communication.send_to_server("disconnect")
    communication.close()
    logger.log_debug("Agent terminated")