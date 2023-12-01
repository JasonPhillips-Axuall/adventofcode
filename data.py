import argparse
from data_file import DataFile

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--year", help="The year of the puzzle")
    argparser.add_argument("--day", help="The day of the puzzle")

    args = argparser.parse_args()
    print("getting data")
    DataFile(args.year, args.day)
    print("done")