from compressor_core import CompressorCore
import argparse
def main():
    parser = argparse.ArgumentParser(description="Compress a given text")
    parser.add_argument('Filename',help='provide file name')
    
    args = parser.parse_args()
    
    
    text =""
    with open(args.Filename, 'r') as file:
        text = file.read()
        # print(text)
    
    obj = CompressorCore(text)
    obj.buildTree()
    print(obj.root)
    obj.generate_codings(obj.root)
    print(obj.codes)
    obj.rewrite_text(text)
        
        
if __name__ == "__main__":
    main()