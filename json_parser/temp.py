import re

# Create a list of compiled regex patterns
regex_list = [
    re.compile(r"\d+"),          # matches one or more digits
    re.compile(r"True|False"),
    re.compile(r"[a-zA-Z]+"),    # matches one or more letters
    re.compile(r"\s+"),          # matches one or more whitespace characters
    re.compile(r"^[A-Z]"),       # matches strings starting with a capital letter
]


text = "Hello"

for regex in regex_list:
    match = regex.search(text)
    if match:
        print(f"Matched: {match.group()} with pattern: {regex.pattern}")
