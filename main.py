Python

# main.py

import argparse
from config import PROJECT_ID, DEFAULT_ZONE
import instance_manager

def main():
    parser = argparse.ArgumentParser(description="Ascension2AnotherDimension - GCP Automation Tool")
    parser.add_argument('--list', action='store_true', help='List VM instances')
    parser.add_argument('--start', type=str, help='Start a VM instance')
    parser.add_argument('--stop', type=str, help='Stop a VM instance')
    parser.add_argument('--zone', type=str, default=DEFAULT_ZONE, help='GCP zone (default: us-central1-a)')

    args = parser.parse_args()

    if args.list:
        instance_manager.list_instances(PROJECT_ID, args.zone)
    elif args.start:
        instance_manager.start_instance(PROJECT_ID, args.zone, args.start)
    elif args.stop:
        instance_manager.stop_instance(PROJECT_ID, args.zone, args.stop)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
