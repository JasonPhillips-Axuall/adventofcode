import re

class node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, node):
            return False

        return self.data == other.data

def build(data):
    retval = {}
    lines = data.split('\n')
    for line in lines:
        line_parts = re.findall(r'[a-zA-Z]+', line)
        retval[line_parts[0]] = line_parts[1:]

    return retval

def build_tree(tree_string):
    root = node('AAA')
    queue = [root]
    done = []
    while len(queue) > 0:
        current_node = queue.pop(0)
        left = node(tree_string[current_node.data][0])
        right = node(tree_string[current_node.data][1])
        if current_node == left == right:
            break

        current_node.left = left
        current_node.right = right

        if left in queue:
            continue
        
        queue.append(current_node.left)

        if right in queue: 
            continue

        queue.append(current_node.right)

    return root

def has_more_children(hash, key):
    if key == hash[key][0] == hash[key][1]:
        return False
    return True
    

def main(data):
    instructions = data.split('\n\n')[0]
    tree_string = build(data.split('\n\n')[1])
    # tree = build_tree(tree_string)
    # current_node = tree
    step = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        for i in instructions:
            
            if i == 'R':
                current_node = tree_string[current_node][1]
            elif i == 'L':
                current_node = tree_string[current_node][0]
            
            step += 1
    return step



if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/8.txt"), "r") as data:
        print(main(data.read()))