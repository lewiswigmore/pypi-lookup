#!/usr/bin/env python3

import argparse
from iplookup.aggregator import aggregate_ip_data

def main():
    parser = argparse.ArgumentParser(description="IP Lookup Tool")
    parser.add_argument("ip", type=str, help="IP address to lookup")
    args = parser.parse_args()
    
    ip = args.ip
    data = aggregate_ip_data(ip)
    
    print(data)

if __name__ == "__main__":
    main()
