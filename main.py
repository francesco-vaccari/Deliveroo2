import time
import signal
import argparse
import subprocess
from utils.Logger import ExperimentLogger

parser = argparse.ArgumentParser(description="Deliveroo2 Experiment Manager")
parser.add_argument('--desc', action='store_true', help="Add a description to the experiment")
parser.add_argument('--map', type=str, required=True, help="Path to the map config file")
parser.add_argument('--parcels', type=str, required=True, help="Path to the parcels config file")
parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help="Host address of the server")
parser.add_argument('--port', type=int, required=False, default=8080, help="Port number of the server")
args = parser.parse_args()

experiment_folder = time.strftime("experiments/%Y-%m-%d-%H-%M-%S")
log_file = 'main.log'
logger = ExperimentLogger(experiment_folder, log_file)

if args.desc:
    description = "Experiment Description: " + input("Please enter a description of the experiment: ")
    logger.log_info(description)

server_args = ['--map', args.map, '--parcels', args.parcels, '--folder', experiment_folder, '--host', args.host , '--port', str(args.port)]
process1 = subprocess.Popen(['python3', 'server.py'] + server_args)
logger.log_debug("Server started")

agent_args = ['--folder', experiment_folder, '--host', args.host, '--port', str(args.port+1), '--server-port', str(args.port)]
process2 = subprocess.Popen(['python3', 'agent.py'] + agent_args)
logger.log_debug("Agent started")

def signal_handler(sig, frame):
    process1.terminate()
    process2.terminate()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

process1.wait()
process2.wait()
logger.log_debug("Server and agent terminated. Experiment finished.")
