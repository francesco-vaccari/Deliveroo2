import sys
import signal
import argparse
import subprocess
from logger import ExperimentLogger
import time

parser = argparse.ArgumentParser(description="Deliveroo2 Experiment Manager")
parser.add_argument('--port', type=int, required=False, help="Port for the server", default=8080)
parser.add_argument('--map', type=str, required=True, help="Map configuration file")
parser.add_argument('--parcels', type=str, required=True, help="Parcels configuration file")
parser.add_argument('--framerate', type=int, required=False, help="Framerate of the game", default=60)
parser.add_argument('--width', type=int, required=False, help="Width of the game window", default=600)
parser.add_argument('--height', type=int, required=False, help="Height of the game window", default=600)
args = parser.parse_args()


server = 'server.py'
server_args = ['--port', str(args.port), '--map', str(args.map), '--parcels', str(args.parcels), '--framerate', str(args.framerate), '--width', str(args.width), '--height', str(args.height)]

agent = 'agent.py'
agent_args = ['--port', str(args.port), '--port', str(args.port+1)]

process1 = subprocess.Popen(['python3', server] + server_args)
time.sleep(1)
process2 = subprocess.Popen(['python3', agent] + agent_args)

print("Server and agent started.")

def signal_handler(sig, frame):
    print('Interrupt received, terminating subprocesses...')
    process1.terminate()
    process2.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    process1.wait()
    process2.wait()
except KeyboardInterrupt:
    signal_handler(None, None)





# log_dir = "logs"
# log_file_name = "experiment.log"
# exp_logger = ExperimentLogger(log_dir, log_file_name)

# exp_logger.log_info("This is an info message.")
# exp_logger.log_debug("This is a debug message.")
# exp_logger.log_warning("This is a warning message.")
# exp_logger.log_error("This is an error message.")