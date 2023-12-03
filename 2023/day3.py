
import os
import re

number_regex = r"\d+"
symbol_regex = r"[^A-Za-z0-9.]"
gear_regex = r"[*]"

HERE = os.path.dirname(os.path.abspath(__file__))

# return all indexes of tokens in a line
def token_indexes(line, reg = number_regex):
    retval = [(m.start(), m.end()) for m in re.finditer(reg, line)]
    return retval

def has_symbol_between(line, start_idx, end_idx, reg):
    start_idx = max([0, start_idx])

    search_text = line[start_idx:end_idx+1]
    tokens = token_indexes(search_text, reg)
    if len(tokens) > 0:
        return True
    
    return False

def is_between(line, number_token, symbol_token):
    symbol_set = set(range(symbol_token[0]-1, symbol_token[1]+1))
    number_set = set(range(number_token[0], number_token[1]))
    test = symbol_set.intersection(number_set)

    return len(test) > 0

def exec(data):

    total = 0
    lines = data.split("\n")
    for y, line in enumerate(lines):
        print("line: ", y+1)
        tokens = token_indexes(line, gear_regex)
        
        for token in tokens:  
            num_arr = []
            for test_line_idx in range(y-1, y+2):

                if test_line_idx < 0:
                    continue
                if test_line_idx >= len(lines):
                    continue

                number_tokens = token_indexes(lines[test_line_idx], number_regex)
                for number_token in number_tokens:
                    if is_between(lines[test_line_idx], number_token, token):
                        print(lines[test_line_idx][number_token[0]:number_token[1]])
                        num_arr.append(int(lines[test_line_idx][number_token[0]:number_token[1]]))

            if len(num_arr) == 2:
                print(num_arr)
                total += (num_arr[0] * num_arr[1])
 
    return total


if __name__ == "__main__":
    with open(os.path.join(HERE, "../data/2023/3.txt"), "r") as data:
        print(exec(data.read()))
