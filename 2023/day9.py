import math

def build_step(seq):
    retval  = []
    for i, s in enumerate(seq):
        if i+1 > len(seq)-1:
            break

        retval.append(seq[i+1] - s)
    return retval
        
def make_array(line):
    return [int(i) for i in line.split()]

def add_value(arr):
    for line in range(len(arr)-1, -1, -1):
        if line == len(arr)-1:
            arr[line].append(0)
        else:
            new_val = arr[line+1][-1] + arr[line][-1]
            arr[line].append(new_val)
    
    pass

def build_seq(line):
    l = [make_array(line)]
    
    i = 0
    while True:
        new_line = build_step(l[i])
        l.append(new_line)
        i += 1
        if new_line.count(0) == len(new_line):
            break

    add_value(l)
    return l

def main(data):
    lines = data.split('\n')
    count = 0
    for line in lines:
        count += build_seq(line)[0][-1]

    return count


if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/9.txt"), "r") as data:
        print(main(data.read()))