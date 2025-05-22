from queue import PriorityQueue
from itertools import count
class Node:
    def __init__(self,val,charac=None):
        self.left = None
        self.right = None
        self.val = val
        self.charac = charac


class CompressorCore:

    def __init__(self, text):
        self.pq = PriorityQueue()
        self.text = text
        self.char_freq = {}
        self.codes = {}
        self.counter = count()
        self.root = None
        self.calculate_freq()
        print(self.char_freq)

    def calculate_freq(self):
        for charac in self.text:
            if charac in self.char_freq:
                self.char_freq[charac] += 1
            else:
                self.char_freq[charac] = 1
                
        
    def buildTree(self):
        for key, value in self.char_freq.items():
            obj = Node(value, key)
            self.pq.put((value, next(self.counter) ,obj))
        
        while self.pq.qsize() != 1:
            first = self.pq.get()
            second =self.pq.get()
            combo = Node(first[0] + second[0])
            combo.left = first[2]
            combo.right = second[2]
            self.pq.put((first[0] + second[0], next(self.counter), combo))
        
        self.root=  self.pq.get()[2]
        print(self.root)
        
    def generate_codings(self,root, prefix=''):
        print(root)
        if root.left == None and root.right == None:
            self.codes[root.charac] = prefix
            return
        else:
            if root.left:
                temp = prefix + '0'
                self.generate_codings(root.left, temp)
            if root.right:
                temp = prefix + '1'
                self.generate_codings(root.right, temp)
            
    def rewrite_text(self, text):
        # Convert text to encoded binary string
        binary_string = ''.join(self.codes[char] for char in text)

        # Pad binary string
        padding = 8 - len(binary_string) % 8
        binary_string += '0' * padding

        # Store padding info in first 8 bits
        padded_info = "{0:08b}".format(padding)
        binary_string = padded_info + binary_string

        # Convert binary string to byte array
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))

        # Write as binary file
        with open('output.bin', 'wb') as output:
            output.write(byte_array)
