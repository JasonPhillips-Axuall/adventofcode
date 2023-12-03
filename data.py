import argparse
import datetime
from data_file import DataFile

def get_current_year():
    return datetime.datetime.now().year

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--year", help="The year of the puzzle", default=get_current_year())
    argparser.add_argument("--day", help="The day of the puzzle")

    args = argparser.parse_args()
    print("getting data")
    DataFile(args.year, args.day)
    print("done")