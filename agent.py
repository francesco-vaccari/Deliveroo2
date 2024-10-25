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

def is_experiment_concluded(desire_steps, intention_steps, requests_made, cost_estimate):
    # if desire_steps > 4 or cost_estimate > 20:
    #     return True
    return False

def receive_events(communication, perception, control, prompting, logger, visualizer):
    global running
    while running:
        if len(communication.buffer) > 0:
            msg, addr = communication.buffer.pop(0)
            if msg.split()[0] == "connected":
                logger.log_info(f"Connected to server as agent ID: {msg.split()[1]}")
            else:
                perception.append_event(msg)
        else:
            time.sleep(0.1)
        
        if is_experiment_concluded(control.desire_steps, control.intention_steps, prompting.get_requests_made(), prompting.get_cost_estimate()):
            running = False
            logger.log_debug("Experiment limit reached. Shutting down agent...")
    
    visualizer.self_close = True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deliveroo2 Agent")
    parser.add_argument('--folder', type=str, required=True, help="Path to the experiment folder")
    parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help="Host address of the server")
    parser.add_argument('--port', type=int, required=True, help="Port number of the agent")
    parser.add_argument('--server-port', type=int, required=True, help="Port number of the server")
    parser.add_argument('--user-generated-desire', action='store_true', help="Use user-generated desire")
    parser.add_argument('--stateless-intention-generation', action='store_true', help="Use stateless intention generation")
    parser.add_argument('--no-desire-triggering', action='store_true', help="Disable desire triggering")
    parser.add_argument('--no-evaluation-triggered-desires', action='store_true', help="Disable evaluation of triggered desires")
    parser.add_argument('--perception-generation-only-on-error', action='store_true', help="Generate perception only on error")
    args = parser.parse_args()

    logger = ExperimentLogger(args.folder, 'agent.log')
    logger.log_debug("Agent started")

    communication = Communication(args.folder, args.host, args.port, args.server_port)
    
    id = None
    while running:
        communication.send_to_server("connect")
        time.sleep(0.1)
        if len(communication.buffer) > 0:
            msg, addr = communication.buffer.pop(0)
            msg = msg.split()
            if msg[0] == "connected":
                logger.log_info(f"Connected to server as agent ID: {msg[1]}")
                id = msg[1]
                break
    
    logger.log_debug(f"Agents started with configuration:\n\tstateless intention generation: {args.stateless_intention_generation}\n\tuser generated desire: {args.user_generated_desire}\n\tno desire triggering: {args.no_desire_triggering}\n\tperception generation only on error: {args.perception_generation_only_on_error}\n\tno evaluation of triggered desires: {args.no_evaluation_triggered_desires}")
    print(f"Agents started with configuration:\n\tstateless intention generation: {args.stateless_intention_generation}\n\tuser generated desire: {args.user_generated_desire}\n\tno desire triggering: {args.no_desire_triggering}\n\tperception generation only on error: {args.perception_generation_only_on_error}\n\tno evaluation of triggered desires: {args.no_evaluation_triggered_desires}")
    
    prompting = Prompting(args.folder, id)
    perception = Perception(args.folder, communication, prompting, args.perception_generation_only_on_error)
    control = Control(args.folder, communication, prompting, perception.get_control_events, perception.get_belief_set, args.user_generated_desire, args.stateless_intention_generation, args.no_desire_triggering, args.no_evaluation_triggered_desires)
    logger.log_debug("Perception and control units started")


    app = QApplication(sys.argv)
    visualizer = RealTimeVisualizer(perception, control, prompting, args.folder)
    
    listener = threading.Thread(target=receive_events, args=(communication, perception, control, prompting, logger, visualizer))
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