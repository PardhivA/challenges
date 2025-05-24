# Huffman Compressor

A simple Python-based Huffman encoding and decoding tool for compressing text files. It supports binary output and an optional Base64-encoded sharable format.

---

## 📦 Features

- Compress plain text using Huffman coding
- Decompress `.bin` files or Base64 sharable format
- Generates a JSON file for Huffman codes
- CLI support using `argparse`
- Supports binary file output and text-based Base64 encoding for sharing

---

## 🛠 Requirements

- Python 3.6 or later

All dependencies are part of the Python standard library.

---

## 📁 Project Structure

```
huffman_compressor/
│
├── compressor_core.py         # Huffman encoding and decoding logic
├── script.py                  # Command-line interface for compression & decompression
├── README.md                  # This file
├── output.bin                 # Compressed binary output (generated after encoding)
├── output_sharable.txt        # Optional base64-encoded output (if -s flag is used)
├── decoded_text.txt           # File created after decoding
└── codes.json             # JSON file containing Huffman codes
```

---

## 🚀 Usage

### ✅ Encoding (Compression)

```bash
python script.py input.txt --codes codes.json -e
```

This will:
- Read `input.txt`
- Encode the contents using Huffman encoding
- Save binary output to `output.bin`
- Save Huffman codes to `codes.json`

### 🧩 Optional: Create a Sharable Format

```bash
python script.py input.txt --codes codes.json -e -s
```

This will also generate a Base64-encoded version in `output_sharable.txt`.

---

### 🔓 Decoding (Decompression)

For regular binary output:
```bash
python script.py output.bin --codes codes.json -d
```

For Base64 sharable format:
```bash
python script.py output_sharable.txt --codes codes.json -d -s
```

The decoded result is saved in `decoded_text.txt`.

---

## 📝 Example

```bash
python script.py sample.txt --codes sample_codes.json -e -s
python script.py output_sharable.txt --codes sample_codes.json -d -s
```

---

## 📌 Notes

- The encoded binary file is always `output.bin`.
- The decoded file is always written as `decoded_text.txt`.
- Make sure to keep the Huffman codes JSON file when decoding, as it's necessary to reconstruct the text.

---

## 🧠 How It Works

1. **Frequency Analysis**: Count the frequency of each character in the input.
2. **Huffman Tree**: Build a binary tree based on character frequencies.
3. **Encoding**: Generate binary codes for each character.
4. **Padding**: Pad the final binary to fit byte structure.
5. **Compression**: Store binary bytes and optionally Base64 encode them.
6. **Decompression**: Read the binary, decode using stored codes, and reconstruct original text.

---

## 📬 License

This project is open-source and free to use.
