#! /usr/bin/env python3

from lexer import Lexer
from parser import Parser
import argparse

def main():
    parser = argparse.ArgumentParser(description="Parse JSON")
    
    parser.add_argument('file', help="JSON file to parse")
    
    args = parser.parse_args()
    
    text = ""
    with open(args.file, 'r') as file:
        text = file.read()
    print("text in the file: ", text, "\n\n")
    
    ## lexical analysis
    lexer = Lexer(text)
    temp_output = lexer.process_file()
    
    ## parsing
    parser = Parser(temp_output)
    if parser.process():
        print("Parsed Successfully")
    else:
        print("Had some errors")
    
    
if __name__ == "__main__":
    main()