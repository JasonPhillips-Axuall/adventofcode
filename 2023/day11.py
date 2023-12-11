from itertools import permutations

def get_galaxy_list(grid):
    galaxy_list = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#":
                galaxy_list.append((y, x))
    return galaxy_list

def make_grid(data):
    lines = data.split('\n')
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

def get_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def get_expands(grid):
    y, x = [], []

    for i in range(len(grid)):
        if grid[i].count("#") == 0:
            y.append(i)

    for j in range(len(grid[i])):
        if [row[j] for row in grid].count("#") == 0:
            x.append(j)

    return y, x

def shift_galaxies(galaxy_list, expands, multiplier):
    ys = expands[0]
    xs = expands[1]

    for i, galaxy in enumerate(galaxy_list):

        for x in xs:
            if galaxy_list[i][1] > x:
                galaxy = galaxy[0], galaxy[1] + (multiplier - 1)

        for y in ys:
            if galaxy_list[i][0] > y:
                galaxy = galaxy[0] + (multiplier - 1), galaxy[1]

        galaxy_list[i] = galaxy

def get_all_adistance(galaxy_list, expands, multiplier):
    shift_galaxies(galaxy_list, expands, multiplier)

    d = 0
    
    done = []

    for g1 in range(len(galaxy_list)):
        for g2 in range(len(galaxy_list)):
            if g1 == g2:
                continue

            d += get_distance(galaxy_list[g1], galaxy_list[g2])

    return int(d/2)

def main(data, multiplier):
    grid = make_grid(data)
    galaxy_list = get_galaxy_list(grid)
    expands = get_expands(grid)
    return get_all_adistance(galaxy_list, expands, multiplier)

if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/11.txt"), "r") as data:
        print(main(data.read(),  1000000))


