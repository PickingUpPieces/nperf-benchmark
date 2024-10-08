# This python script tests the benchmark host and gets relevant sytem information.
import argparse
import logging
import subprocess

print("Sysinfo")

RESULTS_FILE = "../results/sysinfo.txt"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=RESULTS_FILE, filemode='a')

command = [
    "uname -a", 
    "lsb_release -a",
    "lscpu",
    "lscpu --extended"
    ]

# Function to execute a command and return its output
def execute_command(command: str):
    with open(RESULTS_FILE, 'a') as results_file:
        subprocess.run(command, shell=True, stdout=results_file, stderr=results_file)
    logging.info('----------------------')

def main():
    parser = argparse.ArgumentParser(description="Retrieving system information of host")
    parser.add_argument("interface", type=str, help="The network interface")
    parser.add_argument("--ip", default="0.0.0.0", type=str, help="The IP address of the network interface")
    args = parser.parse_args()

    logging.info(f'Interface: {args.interface}')
    logging.info('----------------------')

    for cmd in command:
        logging.info(f"Executing command: {cmd}")
        execute_command(cmd)

    execute_command(f'ethtool -k {args.interface}')
    execute_command(f'ifconfig {args.interface}')


if __name__ == '__main__':
    logging.info('Starting sysinfo script')
    main()
    logging.info('Script sysinfo finished')