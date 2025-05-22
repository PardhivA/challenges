    #! /usr/bin/env python3
# Shebang line to indicate the script should be run using Python 3

import argparse  # Import the argparse module to handle command-line arguments

# Function to count the number of words in a file
def countWords(fileName):
    with open(fileName, 'r') as file:
        words = file.read().split()  # Split the file content by whitespace
        return len(words)  # Return the number of words

# Function to count the number of lines in a file
def countLines(fileName):
    with open(fileName, 'r') as file:
        Lines = file.read().splitlines()  # Split the content by line breaks
        return len(Lines)  # Return the number of lines
    
# Function to count the number of characters in a file (text mode)
def countChars(fileName):
    with open(fileName, 'r') as file:
        Chars = file.read()  # Read the entire content as a string
        return len(Chars)  # Return the number of characters

# Function to count the number of bytes in a file (binary mode)
def countBytes(fileName):
    with open(fileName, 'rb') as file:  # Open the file in binary mode
        Bytes = file.read()  # Read the entire binary content
        return len(Bytes)  # Return the number of bytes


def main():
    # Create an argument parser object
    parser = argparse.ArgumentParser(description="A Word count tool")
    
    # Positional argument: file name
    parser.add_argument('file', help="File to check for word count")
    
    # Optional flags for counting lines, words, characters, and bytes
    parser.add_argument('-l', '--lines', action='store_true', help='set this flag to know how many lines present')
    parser.add_argument('-w', '--words', action='store_true', help='set this flag to know how many words present')
    parser.add_argument('-c', '--chars', action='store_true', help='set this flag to know how many characters present')
    parser.add_argument('-b', '--bytes', action='store_true', help='set this flag to know how many bytes present')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # If the user requests line count
    if args.lines:
        print(f"Number of lines present in {args.file} is {countLines(args.file)}")  
    
    # If the user requests word count
    if args.words:
        print(f"Number of words present in {args.file} is {countWords(args.file)}")  
    
    # If the user requests character count
    if args.chars:
        print(f"Number of chars present in {args.file} is {countChars(args.file)}")  
    
    # If the user requests byte count
    if args.bytes:
        print(f"Number of bytes present in {args.file} is {countBytes(args.file)}")  
    
    # If no specific flag is provided, display all counts
    if args.lines or args.words or args.chars or args.bytes:
        pass
    else:
        print(f"Number of lines present in {args.file} is {countLines(args.file)}")  
        print(f"Number of words present in {args.file} is {countWords(args.file)}")  
        print(f"Number of chars present in {args.file} is {countChars(args.file)}")  
        print(f"Number of bytes present in {args.file} is {countBytes(args.file)}")  

# Entry point of the script
if __name__ == "__main__":
    main()
