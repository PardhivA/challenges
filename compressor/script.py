from compressor_core import CompressorCore
import argparse



def main():
    parser = argparse.ArgumentParser(description="Compress a given text")
    
    parser.add_argument('Filename',help='provide file name')
    parser.add_argument('--codes', required=True,help='Json file for Codes')
    parser.add_argument('-e', '--encode', action = 'store_true', help="Encode the text in a file")
    parser.add_argument('-d', '--decode', action = 'store_true', help="Decode the bin text in a bin file")
    parser.add_argument('-s', '--share', action='store_true', help='Convert into sharable format as well')
    
    args = parser.parse_args()
    
        
    if args.encode:
        text =""
        with open(args.Filename, 'r') as file:
            text = file.read()
        obj = CompressorCore(text)
        obj.buildTree()
        print(obj.root)
        obj.generate_codings(obj.root)
        # print(obj.codes)
        if args.share:
            obj.encode_text(text,args.codes, True)
        else:
            obj.encode_text(text ,args.codes)
        
    elif args.decode:
        # with open(, 'rb') as file: 
        #     byte_data = file.read()
        jsonFilename = args.codes
        if args.share:
            CompressorCore.decode(args.Filename,jsonFilename,True) 
        else:
            CompressorCore.decode(args.Filename,jsonFilename)
if __name__ == "__main__":
    main()