def build_map_names(line):
    return line.split(' ')[0]

def build_map(data):
    lines = data.split('\n')
    names = build_map_names(lines.pop(0))

    m = {}

    for line in lines:
        s = [int(s) for s in line.split()]

        m[s[1], s[1]+s[2]-1] = s[0] - s[1]


    return m

def find_location(maps, seed):
    step = seed
    for m in maps:
        for t in m:
            if step >= t[0] and step <= t[1]:
                step += m[t]
                break
        
    return step
    
def main(data):
    chunks = data.split('\n\n')
    seeds = chunks.pop(0)
    seed_arr = [int(s) for s in seeds.split(':')[1].split()]
    maps = []
    cache = {}
    retval = None
    for idx, chunk in enumerate(chunks):
        m = build_map(chunk)
        maps.append(m)

    # answer_map = combine_maps(maps)

    while len(seed_arr) > 0:
        print(len(seed_arr))
        start = seed_arr.pop(0)
        end = seed_arr.pop(0)

        i = start
        while i <= start + end:
            # if i in cache:
            #     if retval > cache[i]:
            #         retval = cache[i]

            #     print('loaded from cache')
            #     continue

            location = find_location(maps, i)
            if retval is None or retval > location:
                retval = location
                # cache[i] = location
            i += 1
        
    return retval
    
if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/5.txt"), "r") as data:
        print(main(data.read()))