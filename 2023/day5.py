import copy

def build_map_names(line):
    return line.split(' ')[0]

def build_map(data):
    lines = data.split('\n')
    names = build_map_names(lines.pop(0))

    m = []

    for line in lines:
        s = [int(s) for s in line.split()]

        m.append([s[1], s[1]+s[2]-1, s[0] - s[1] ])


    return m

def find_location(maps, seed):
    step = seed
    for m in maps:
        for t in m:
            if step >= t[0] and step <= t[1]:
                step += m[t]
                break
        
    return step

def sort_maps(map):
    return sorted(map, key=lambda n: (n[0], n[1]))

def non_overlapping_span(arr1, arr2):
    retval = []
    # end is after start just return them
    # |------|                  arr1
    #         |---------------| arr2
    if arr1[1] < arr2[0]:
        return [arr1, arr2]

    if arr1[0] == arr2[0] and arr1[1] == arr2[1]:
        section = [arr1[0], arr1[1], arr1[2] + arr2[2]]
        return [section]
    
    # start or next == end
    # |-------|                 arr1
    #         |---------------| arr2
    if arr1[1] == arr2[0]:
        section1 = [arr1[0], arr2[0] -1, arr1[2]] # gets value from one
        section2 = [arr2[0], arr1[1], arr1[2] + arr2[2]] #gets value from both
        section3 = [arr1[1]-1, arr2[1], arr2[2]] #gets value from two

        return [section1, section2, section3]
    
    # |--------------------|    arr1
    #         |---------------| arr2
    # end is before start and end is after start
    if arr1[1] > arr2[0] and arr1[1] < arr2[1]:
        section1 = [arr1[0], arr2[0] -1, arr1[2]]# gets value from one
        section2 = [arr2[0], arr1[1], arr1[2] + arr2[2]] #gets value from both
        section3 = [arr1[1] + 1, arr2[1], arr2[2]] #gets value from two
        return [section1, section2, section3]


    # |-------------------|     arr1
    #        |---------|        arr2
    # |-----||---------||--|
    if arr1[1] > arr2[0] and arr1[1] > arr2[1]:
        section1 = [arr1[0], arr2[0] -1, arr1[2]] # gets value from one
        section2 = [arr2[0], arr2[1], arr1[2] + arr2[2]] #gets value from both
        section3 = [arr2[1] + 1, arr1[1], arr2[2]] #gets value from two
        return [section1, section2, section3]


def combine_maps(maps):
    retval = []
    # current = maps.pop(0)
    # while len(maps) > 0:
        # next = maps.pop(0)
    m = maps.pop(0)
    
    while len(maps) > 0:
        m += maps.pop(0)
        tmp = sort_maps(m)
        rv = [tmp.pop(0)]
        for i in range(len(tmp)):
            t = tmp[i]
            l = rv.pop()
            rv += non_overlapping_span(l, t)

            # if t[0] > rv[-1][1]:
            #     rv.append(t)
            #     continue

            # # reset last element ad new 
            # if t[0] <= rv[-1][1] and t[1] >= rv[-1][1]:
            #     rv[-1][1] = t[0] -1
            #     rv[-1][2] = rv[-1][2] + t[2]
            #     rv.append(t)
            #     continue

            # if t[0] <= rv[-1][1] and t[1] < rv[-1][1]:
            #     r = rv.pop()
            #     r2  = copy.deepcopy(r)
            #     r[1] = t[0] - 1
            #     r[2] = r[2] + t[2]
            #     rv.append(r)
            #     rv.append(t)
            #     r2[0] = t[1] + 1
            #     r2[2] = r2[2] + t[2]
            #     rv.append(r2)
            #     continue
        m = rv
        rv = []

    retval = rv
    return retval
    
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

    answer_map = combine_maps(maps)

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