import time
import signal
import argparse
import subprocess
from utils.Logger import ExperimentLogger

parser = argparse.ArgumentParser(description="Deliveroo2 Experiment Manager")
parser.add_argument('--desc', action='store_true', help="Add a description to the experiment")
parser.add_argument('--user-generated-desire', action='store_true', help="Use user-generated desire")
parser.add_argument('--stateless-intention-generation', action='store_true', help="Use stateless intention generation")
parser.add_argument('--no-desire-triggering', action='store_true', help="Disable desire triggering")
parser.add_argument('--perception-generation-only-on-error', action='store_true', help="Generate perception only on error")
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

maps_path = 'server_dir/conf/maps/' + args.map
parcels_path = 'server_dir/conf/parcels/' + args.parcels

server_args = ['--map', maps_path, '--parcels', parcels_path, '--folder', experiment_folder, '--host', args.host , '--port', str(args.port)]
process1 = subprocess.Popen(['python3', 'server.py'] + server_args)
logger.log_debug("Server started")

agent_args = ['--folder', experiment_folder, '--host', args.host, '--port', str(args.port+1), '--server-port', str(args.port), '--user-generated-desire', str(args.user_generated_desire), '--stateless-intention-generation', str(args.stateless_intention_generation), '--no-desire-triggering', str(args.no_desire_triggering), '--perception-generation-only-on-error', str(args.perception_generation_only_on_error)]
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
