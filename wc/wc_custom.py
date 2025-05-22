#! /usr/bin/env python3
import argparse

def count_words(file):
    with open(file,'r') as file:
        text = file.read()
        lines = text.splitlines()
        num_lines = len(lines)
        words = text.split()
        num_words = len(words)
        num_chars = len(text)
        return num_lines,num_words, num_chars

def main():
    parser = argparse.ArgumentParser(description="A Custom Word Count tool")
    parser.add_argument('file',help="File to check for word count")
    args = parser.parse_args()
    
    num_lines, num_words, num_chars = count_words(args.file)
    print(f"number of lines in {args.file}: {num_lines}")
    print(f"number of words in {args.file}: {num_words}")
    print(f"number of characters in {args.file}: {num_chars}")
if __name__ == "__main__":
    main()