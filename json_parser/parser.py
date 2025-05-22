class Parser:
    
    def __init__(self, chunks_tokens):
        self.chunks_tokens = chunks_tokens
        print(chunks_tokens)
        self.grammar = {
            "start" : [["lf", "stmt", "rf"]],
            "stmt"  : [["string" , "colon", "temp1","ending"],[]],
            "temp1" : [["string"],["digits"],["bool"],["array"],["start"]],
            "ending" : [["comma", "stmt"],[]],
            "array" : [['ls',"rec",'rs']],
            "rec" : [["temp1" , "comma", "rec"],["temp1"]]
        }
    
    def process(self, current_nt = "start", index = [0]):
        rule_status=  False
        temp = index[0]
        for rule in self.grammar[current_nt]:
            if not rule_status:
                rule_status = True
                index[0] = temp
            else:
                return True
            for term in rule:
                # if index == len(self.chunks_tokens[0]):
                #     rule_status = False
                #     break
                if term in self.grammar:
                    # temp = index[0]
                    status = self.process(term, index)
                    if status:
                        pass
                    else:
                        rule_status = False
                        break
                else:
                    if self.chunks_tokens[1][index[0]] == term:
                        index[0] += 1
                    else:
                        rule_status = False
                        break
        return rule_status
        
        