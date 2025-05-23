import base64
import json
from queue import PriorityQueue
from itertools import count

# Define a Node class for Huffman tree
class Node:
    def __init__(self, val, charac=None):
        self.left = None           # Left child
        self.right = None          # Right child
        self.val = val             # Frequency of the character(s)
        self.charac = charac       # The character itself (if a leaf)

# CompressorCore handles encoding and decoding logic
class CompressorCore:

    def __init__(self, text):
        self.pq = PriorityQueue()  # Priority queue for building Huffman tree
        self.text = text
        self.char_freq = {}        # Dictionary to store frequency of each character
        self.codes = {}            # Huffman codes for each character
        self.counter = count()     # Tie-breaker counter for queue
        self.root = None           # Root of Huffman tree
        self.calculate_freq()      # Calculate frequency of characters
        print(self.char_freq)      # Debug print of frequency table

    # Calculate frequency of characters in input text
    def calculate_freq(self):
        for charac in self.text:
            if charac in self.char_freq:
                self.char_freq[charac] += 1
            else:
                self.char_freq[charac] = 1
                
    # Build Huffman tree using priority queue
    def buildTree(self):
        # Step 1: Add all characters as leaf nodes into the priority queue
        for key, value in self.char_freq.items():
            obj = Node(value, key)
            self.pq.put((value, next(self.counter), obj))

        # Step 2: Merge nodes until only one node (the root) remains
        while self.pq.qsize() != 1:
            first = self.pq.get()
            second = self.pq.get()
            combo = Node(first[0] + second[0])  # Create new internal node
            combo.left = first[2]
            combo.right = second[2]
            self.pq.put((first[0] + second[0], next(self.counter), combo))

        self.root = self.pq.get()[2]  # Set final node as root

    # Generate Huffman codes for each character recursively
    def generate_codings(self, root, prefix=''):
        print(root)  # Debug print
        if root.left is None and root.right is None:
            self.codes[root.charac] = prefix  # Save code for leaf character
            return
        if root.left:
            self.generate_codings(root.left, prefix + '0')  # Add '0' for left
        if root.right:
            self.generate_codings(root.right, prefix + '1')  # Add '1' for right

    # Encode input text and optionally create a sharable base64 version
    def encode_text(self, text, codesJsonFilename, sharable=False):
        # Convert text to binary string using Huffman codes
        binary_string = ''.join(self.codes[char] for char in text)

        # Pad the binary string to ensure it's a multiple of 8 bits
        padding = 8 - len(binary_string) % 8
        binary_string += '0' * padding

        # Store padding info in first 8 bits (needed for decoding later)
        padded_info = "{0:08b}".format(padding)
        binary_string = padded_info + binary_string

        # Convert the full binary string into bytes
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))  # Convert each byte to integer

        # Write compressed binary data to file
        with open('output.bin', 'wb') as output:
            output.write(byte_array)

        # Save Huffman codes (needed for decoding) in a JSON file
        with open(codesJsonFilename, 'w') as output_codes:
            json.dump(self.codes, output_codes)

        # Optional: create a base64 encoded sharable version
        if sharable:
            encoded = base64.b64encode(byte_array).decode('utf-8')
            with open('output_sharable.txt', 'w') as file:
                file.write(encoded)

    # Static method for decoding a binary or sharable file
    @staticmethod
    def decode(file_name, codes_json_file, sharable_format=False):
        # Read input either as base64 text if sharable or else  raw binary
        if sharable_format:
            with open(file_name, 'r') as file:
                encoded_sharable = file.read()
                byte_data = base64.b64decode(encoded_sharable) ## converts into binary
        else:
            with open(file_name, 'rb') as file:
                byte_data = file.read()

        # Convert bytes to a full binary string
        binary_string = ''
        for byte in byte_data:
            binary_string += f'{byte:08b}'

        # First 8 bits contain padding info
        padding_info = binary_string[:8]
        padding = int(padding_info, 2)

        # Remove the first 8 bits (padding info)
        encoding_data = binary_string[8:]

        # Remove padding bits from the end
        if padding > 0:
            encoded_data = encoding_data[:-padding]
        else:
            encoded_data = encoding_data  # No padding

        # Load saved Huffman codes
        with open(codes_json_file, 'r') as file:
            codes = json.load(file)

        # Reverse the code dictionary: bitstring → character
        reversed_codes = {value: key for key, value in codes.items()}

        # Decode binary string using the reversed code map
        result = ''
        prefix = ''
        for bit in encoded_data:
            prefix += bit
            if prefix in reversed_codes:
                result += reversed_codes[prefix]
                prefix = ''  # Reset for next character

        # Save the decoded text to a file
        with open('decoded_text.txt', 'w') as file:
            file.write(result)

        print("decoded successfully and written to decoded_text.txt")
