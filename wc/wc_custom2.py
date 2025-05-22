#! /usr/bin/env python3
import argparse
import sys

def countWords(text):
    words = text.split()
    return len(words)

def countLines(text):
    Lines = text.splitlines()
    return len(Lines)
    
def countChars(text):
    Chars = text
    return len(Chars)

def countBytes(text):
    Bytes = text.encode('utf-8')
    return len(Bytes)


def main():
    parser = argparse.ArgumentParser(description="A Word count tool")
    parser.add_argument('file',nargs='?',default=None, help="File to check for word count")
    parser.add_argument('-l','--lines',action='store_true',help='set this flag to know how many lines are present')
    parser.add_argument('-w','--words',action='store_true',help='set this flag to know how many words are present')
    parser.add_argument('-c','--chars',action='store_true',help='set this flag to know how many characters are present')
    parser.add_argument('-b','--bytes',action='store_true',help='set this flag to know how many bytes are present')
    
    args = parser.parse_args()
    text = None
    if not args.file:
        text = sys.stdin.read()
    else:
        with open(args.file, 'r',encoding='utf-8') as file:
            text = file.read()
            
    if args.lines:
        print(f"Number of lines present in {args.file if args.file else 'command line'} is {countLines(text)}")  
    
    if args.words:
        print(f"Number of words present in {args.file if args.file else 'command line'} is {countWords(text)}")  
    if args.chars:
        print(f"Number of chars present in {args.file if args.file else 'command line'} is {countChars(text)}")  
    if args.bytes:
        print(f"Number of bytes present in {args.file if args.file else 'command line'} is {countBytes(text)}")  
    
    if args.lines or args.words or args.chars or args.bytes:
        pass
    else:
        print(f"Number of lines present in {args.file if args.file else 'command line'} is {countLines(text)}")  

        print(f"Number of words present in {args.file if args.file else 'command line'} is {countWords(text)}")  

        print(f"Number of chars present in {args.file if args.file else 'command line'} is {countChars(text)}")  

        print(f"Number of bytes present in {args.file if args.file else 'command line'} is {countBytes(text)}")  

        
    
if __name__ == "__main__":
    main()
     