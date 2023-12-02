
import os


here = os.path.dirname(os.path.abspath(__file__))
valid_game = {"red": 12, "green": 13, "blue": 14}

def strip_space(parts):
    return [s.strip() for s in parts]

def cube_parts(line):
    return strip_space(line.split(":")[1].split(";"))

def count_cubes(cube_parts):
    current_cube_count = {"red": 0, "green": 0, "blue": 0}
    parts = strip_space(cube_parts.split(","))
    for part in parts:
        if "blue" in part:
            current_cube_count["blue"] += int(part.split(" ")[0])
        if "red" in part:
            current_cube_count["red"] += int(part.split(" ")[0])
        if "green" in part:
            current_cube_count["green"] += int(part.split(" ")[0])
        
    return current_cube_count

def is_valid_game(cubes):
    return  cubes["red"] <= valid_game["red"] and \
            cubes["blue"] <= valid_game["blue"] and \
            cubes["green"] <= valid_game["green"]

def is_line_valid(line):
    # current_cube_count = {"red": 0, "green": 0, "blue": 0}
    for part in cube_parts(line):
        # cubes = count_cubes(part, current_cube_count)
        cubes = count_cubes(part)
        if is_valid_game(cubes) != True:
            return False
    
    return True
    # return is_valid_game(cubes)

def get_game_number(line):
    return line.split(":")[0].split(" ")[1]

def exec(data):
    valid_count = 0
    for line in data.split("\n"):
        if is_line_valid(line):
            valid_count += int(get_game_number(line))
            print(line, "is valid")
    return valid_count

if __name__ == "__main__":
    with open(os.path.join(here, "../data/2023/2.txt"), "r") as data:
        print(exec(data.read())) # 8