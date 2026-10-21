from zad2 import zad2
from zad4 import zad4
from zad5 import zad5
from zad6 import zad6
import Brewery
import argparse

def main():
    #print(zad2(5, 2))
    #print(zad4(3,3,5))
    #print(zad5([1,2,3,5,6,7,8], 4))
    #res = zad6([1, 2, 3, 4, 5], [1, 2, 7, 8, 9])
    #print(res)
    #print(type(res))

    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help = "filter by city")
    args = parser.parse_args()

    breweries = Brewery.get_breweries(city = args.city)
    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()