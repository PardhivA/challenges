#! /usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='A freindly command line tool to greet anyone')
    parser.add_argument('name',help='Takes your name to greet you')
    args = parser.parse_args()
    
    print(f"Hello, {args.name}! Have a good day")

if __name__ == "__main__":
    main()