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
parser.add_argument('--no-evaluation-triggered-desires', action='store_true', help="Disable evaluation of triggered desires")
parser.add_argument('--perception-generation-only-on-error', action='store_true', help="Generate perception only on error")
parser.add_argument('--conf', type=str, required=True, help="Path to the configuration folder")
parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help="Host address of the server")
parser.add_argument('--port', type=int, required=False, default=8080, help="Port number of the server")
args = parser.parse_args()

experiment_folder = time.strftime("experiments/%Y-%m-%d-%H-%M-%S")
log_file = 'main.log'
logger = ExperimentLogger(experiment_folder, log_file)

if args.desc:
    description = "Experiment Description: " + input("Please enter a description of the experiment: ")
    logger.log_info(description)

conf_path = 'server_dir/conf/' + args.conf

server_args = ['--conf', conf_path, '--folder', experiment_folder, '--host', args.host , '--port', str(args.port)]
process1 = subprocess.Popen(['python3', 'server.py'] + server_args)
logger.log_debug("Server started")

arguments = []
if args.user_generated_desire:
    arguments.append('--user-generated-desire')
if args.stateless_intention_generation:
    arguments.append('--stateless-intention-generation')
if args.no_desire_triggering:
    arguments.append('--no-desire-triggering')
if args.perception_generation_only_on_error:
    arguments.append('--perception-generation-only-on-error')
if args.no_evaluation_triggered_desires:
    arguments.append('--no-evaluation-triggered-desires')

agents_processes = []
with open(conf_path + '/agents.conf', 'r') as file:
    n_agents = int(file.readline().split()[0])
for i in range(n_agents):
    agent_args = ['--folder', experiment_folder + f'/agent_{i+1}', '--host', args.host, '--port', str(args.port+i+1), '--server-port', str(args.port)]
    process = subprocess.Popen(['python3', 'agent.py'] + agent_args + arguments)
    agents_processes.append(process)
    logger.log_debug(f"Agent {i} started")

def signal_handler(sig, frame):
    process1.terminate()
    for process in agents_processes:
        process.terminate()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

process1.wait()
for process in agents_processes:
    process.wait()
logger.log_debug("Server and agents terminated. Experiment finished.")
