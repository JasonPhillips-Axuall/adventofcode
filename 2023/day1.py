from enum import Enum
import os
import re
here = os.path.dirname(os.path.abspath(__file__))

number_strings = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"

def get_first_number(line):
    retVal = 100, ""
    for e in number_strings:
        idx = line.find(e)
        if(idx > -1 and idx < retVal[0]):
            retVal = idx, number_strings.index(e) + 1

    for i in range(0, 10):
        idx = line.find(str(i))
        if(idx > -1 and idx < retVal[0]):
            retVal = idx, str(i)

    return str(retVal[1])

def get_last_number(line):
    retVal = -1, ""
    for e in number_strings:
        idx = line.rfind(e)
        if(idx > -1 and idx > retVal[0]):
            retVal = idx, number_strings.index(e) + 1

    for i in range(0, 10):
        idx = line.rfind(str(i))
        if(idx > -1 and idx > retVal[0]):
            retVal = idx, str(i)

    return str(retVal[1])
        

# def exec(data):
#     retVal = 0
#     for line in data.split("\n"):
#         num_str = ""
#         num_str = get_first_number(line)
#         num_str += get_last_number(line)
        
#         print(num_str)
#         retVal += int(num_str)
#         num_str = ""


def get_number_str(line):
    retVal = ""
    retVal += get_first_number(line)
    retVal += get_last_number(line)
    return retVal

def exec(data):
    retVal = 0
    for line in data.split("\n"):
        retVal += int(get_number_str(line) )

    return(retVal)


if __name__ == "__main__":
    with open(os.path.join(here, "../data/2023/1.txt"), "r") as data:
        ans = exec(data.read())
        print(ans)