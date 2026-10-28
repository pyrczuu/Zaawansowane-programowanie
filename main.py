from zad2 import zad2
from zad4 import zad4
from zad5 import zad5
from zad6 import zad6
from zad7 import *
import argparse


def main():
    # print(zad2(5, 2))
    # print(zad4(3,3,5))
    # print(zad5([1,2,3,5,6,7,8], 4))
    # res = zad6([1, 2, 3, 4, 5], [1, 2, 7, 8, 9])
    # print(res)
    # print(type(res))

    # zad 8
    parser = argparse.ArgumentParser(description="Fetch 20 breweries.")
    parser.add_argument("--city",
                        help='filter by city, e.g. --city "san diego"')
    args = parser.parse_args()

    for brewery in get_breweries(args.city):
        print(brewery)


if __name__ == "__main__":
    main()
