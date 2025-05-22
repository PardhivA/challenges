import re


class Lexer:
    def __init__(self, input_file):
        self.input_file = input_file
        self.accepted_ordered_lexeme = [
    re.compile(r"\d+"),
    re.compile(r"True|False"),
    re.compile(r"\"[a-zA-Z]+\""),
    re.compile(r"\{"),
    re.compile(r"\}"),
    re.compile(r"\["),
    re.compile(r"\]"),
    re.compile(r"\:"),
    re.compile(r"\,")
]
        self.tokens = [
            "digits",
            "bool",
            "string",
            "lf",
            "rf",
            "ls",
            "rs",
            "colon",
            "comma"
        ]
    
    def process_file(self):
        chunks = self.input_file.split()
        tokens_associated = []
        print("chunks in the file: ", chunks, '\n', '\n')
        for chunk in chunks:
            status = False
            index = 0
            for regex in self.accepted_ordered_lexeme:
                
                if regex.search(chunk):
                    tokens_associated.append(self.tokens[index])
                    
                    status = True
                else:
                    pass
                    # status = True
                index += 1
            if status:
                pass    
            else:
                raise Exception(f"{chunk} is not accepted JSON")
             
        print('lexical anaylsis done successfully')
        return [chunks, tokens_associated]
        




