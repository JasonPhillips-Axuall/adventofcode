import math
import re

def build(data):
    retval = {}
    lines = data.split('\n')
    for line in lines:
        line_parts = re.findall(r'[a-zA-Z0-9]+', line)
        retval[line_parts[0]] = line_parts[1:]

    return retval

def has_more_children(hash, key):
    if key == hash[key][0] == hash[key][1]:
        return False
    return True
  
def run(instructions, tree_string, current_node):
    step = 0
    while current_node[-1] != 'Z':
        for i in instructions:
            if i == 'R':
                current_node = tree_string[current_node][1]
            elif i == 'L':
                current_node = tree_string[current_node][0]
            
            step += 1
    return step

def main(data):
    instructions = data.split('\n\n')[0]
    tree_string = build(data.split('\n\n')[1])
    # tree = build_tree(tree_string)
    # current_node = tree
    runs = []
    keys = [k for k in tree_string.keys() if k[-1] == 'A']
    for k in keys:
        runs.append(run(instructions, tree_string, k))

    return math.lcm(*runs)

if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/8.txt"), "r") as data:
        print(main(data.read()))