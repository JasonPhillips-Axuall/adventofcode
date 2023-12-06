import math

def calc_valid_run(time, dist):
    retval = []
    time = time
    start = calc_min_multiplier(time, dist)
    end = time - start
    for i in range(start, end +1):
        distance = calc_run_distance(time, i)

        if distance > dist:
            retval.append(i)

    return retval

def calc_run_distance(race_time, multiplier):
    time_left = race_time - multiplier
    distance = 0
    while time_left > 0:
        time_left -= 1
        distance += multiplier
    
    return distance

def calc_min_multiplier(time, dist):
    return math.ceil(dist / time)

def main(data):
    times_str = [s for s in data.split('\n')[0].split(":")[1].split()]
    dist_str = [s for s in data.split('\n')[1].split(":")[1].split()]
    
    times = int(''.join(times_str))
    dist = int(''.join(dist_str))

    # vals = []
    # # for i in range(len(times)):
    # vals.append(calc_valid_run(times, dist))

    # return math.prod([len(v) for v in vals])
    
    b1 = math.floor((times + math.sqrt(pow(times, 2) - 4 * dist))/2)
    b2 = math.ceil((times - math.sqrt(pow(times, 2) - 4 * dist))/2)

    return b1 - b2 + 1
    
    

if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/6.txt"), "r") as data:
        print(main(data.read()))