import math

def get_adjacent(char, pos):
    if char == 'S':
        return [north(*pos), south(*pos), east(*pos), west(*pos)]
    
    if char == '|':
        return [north(*pos), south(*pos)]
    
    if char == '-':
        return [east(*pos), west(*pos)]
    
    if char == "L":
        return [east(*pos), north(*pos)]
    
    if char == "7":
        return [west(*pos), south(*pos)]
    
    if char == "J":
        return [west(*pos), north(*pos)]
    
    if char == "F":
        return [east(*pos), south(*pos)]


def north(y, x):
    return y -1, x

def south(y, x):
    return y + 1, x

def east(y, x):
    return y, x + 1

def west(y, x):
    return y, x - 1


def next(previous_pos, current_position, char):
   
    # can go up or down
    if char == '|':
        if previous_pos[0] < current_position[0]:
            return south(*current_position)
        else:
            return north(*current_position)
        
    if char == '-':
        if previous_pos[1] < current_position[1]:
            return east(*current_position)
        else:
            return west(*current_position)
        
    if char == "L":
        if previous_pos[0] < current_position[0]:
            return east(*current_position)
        else:
            return north(*current_position)
         
    if char == "7":
        if previous_pos[0] > current_position[0]:
            return west(*current_position)
        else:
            return south(*current_position)
        
    if char == "J":
        if previous_pos[0] < current_position[0]:
            return west(*current_position)
        else:
            return north(*current_position)
        
    if char == "F":
        if previous_pos[0] > current_position[0]:
            return east(*current_position)
        else:
            return south(*current_position)

def get_char(grid, pos):
    return grid[pos[0]][pos[1]]

def run(grid, prev, n):
    visited = [prev]
    queue = [n]
    while len(queue) > 0:
        current = queue.pop(0)
        if current in visited:
            if get_char(grid, current) == 'S':
                return int(len(visited)/2)
            else:
                return None

        visited.append(current)
        char = get_char(grid, current)
        queue.append(next(prev, current, char))
        prev = current

def valid_direction(grid, dir):
    char = grid[dir[0]][dir[1]]
    valid_char = char in ['|', '-', 'L', '7', 'J', 'F']
    valid_dir = (dir[0] >= 0 and dir[0] < len(grid)-1) and \
                (dir[1] >= 0 and dir[1] < len(grid[0]) -1)
    
    return valid_char and valid_dir

def main(data):
    lines = data.split('\n')
    grid = []
    for y, line in enumerate(lines):
        grid.append(list(line))
        if line.find('S') > -1:
            start = y, line.find('S')
 
    dirs = get_adjacent('S', (start))
    v = [d for d in dirs if valid_direction(grid, d)]
    runs = [run(grid, start, d) for d in v]
    runs = [r for r in runs if runs.count(r) == 2]

    return min(runs)

    
if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/10.txt"), "r") as data:
        print(main(data.read()))