import argparse


def main():
    parser = argparse.ArgumentParser(description="Cut tool to cut specific portions in each of the lines in a file")

    parser.add_argument('FileName',type=str,nargs='?',help="file to operate cut tool on")
    parser.add_argument('-b','--bytes', type=str, help="select only these bytes")
    parser.add_argument('-c','--character', type=str, help="select only these characters")
    parser.add_argument('-d','--delimiter',default='\t', type=str, help="a delimiter to cut the text and then field to choose")
    parser.add_argument('-f', '--fields', type=str, help='select only these fields, seperate by delimiter')

    args = parser.parse_args()
    
    if args.FileName: 
        with open(args.FileName, 'r') as file:
            text = file.readlines()
    else:
        import sys
        text = sys.stdin.readlines()
        print(text)

    
    
    for line in text:
        if args.bytes:
            range = args.bytes.split('-')
            l = int(range[0])-1
            r = int(range[1])-1
            byte_data = line.encode('utf-8')           
            print(byte_data[l:r+1])
        
        if args.character:
            range = args.character.split('-')
            l = int(range[0])-1
            r = int(range[1])-1
            # for line in text:
            print(line[l:r+1])
    
        if args.fields:
            nums = args.fields.split(',')
            line = line.split(args.delimiter)
            for num in nums:
                num = int(num)
                print(line[num-1],end=args.delimiter)
            print()
            
    
    

if __name__ == "__main__":
    main()