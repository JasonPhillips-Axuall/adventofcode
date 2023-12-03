
import os
import re

token_regex = "\d+"
symbol_regex = "[^A-Za-z0-9.]"

HERE = os.path.dirname(os.path.abspath(__file__))

# return all indexes of tokens in a line
def token_indexes(line, reg = token_regex):
    retval = [(m.start(), m.end()) for m in re.finditer(reg, line)]
    return retval

def has_symbol_between(line, start_idx, end_idx):
    start_idx = max([0, start_idx])

    search_text = line[start_idx:end_idx+1]
    tokens = token_indexes(search_text, symbol_regex)
    if len(tokens) > 0:
        return True
    
    return False
    

def exec(data):

    total = 0
    lines = data.split("\n")
    for y, line in enumerate(lines):
        tokens = token_indexes(line, token_regex)
        for token in tokens:
            for test_line_idx in range(y-1, y+2):
                if test_line_idx < 0:
                    continue
                if test_line_idx >= len(lines):
                    continue

                if has_symbol_between(lines[test_line_idx], token[0]-1, token[1]+1):
                    print("adding", line[token[0]:token[1]])
                    total += int(line[token[0]:token[1]])

    return total


if __name__ == "__main__":
    with open(os.path.join(HERE, "../data/2023/3.txt"), "r") as data:
        print(exec(data.read()))