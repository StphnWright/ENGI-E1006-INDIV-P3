"""
A search tool that allows users to locate their local Farmers Market by City
or ZIP Code from a national database containing more than 7000 local markets.

read_markets reads in farmers market data from filename and returns a tuple of
a dictionary mapping ZIP Codes to lists of farmers market tuples and a dictionary
mapping Cities to sets of ZIP codes.
    
print_market returns a human-readable string representing the farmers market tuple
passed to the market parameter. 

The main program (if __name__ == "__main__") reads market.txt and prompts the user
to enter a City or ZIP code in a loop until the user quits.
"""

from collections import defaultdict


def read_markets(filename):
    
    file = open(filename, 'r')
    zip_to_market = defaultdict(list)
    city_to_zip = defaultdict(set)
    
    for vendor in file:
        state, market_name, street, city, zip_code, latitude, longitude = vendor.strip().split('#')
        
        if len(zip_code) != 5:
            continue
        zip_to_market[zip_code].append((state, market_name, street, city, zip_code, latitude, longitude))
        city_to_zip[city.lower().strip()].add(zip_code)
    file.close()
        
    return zip_to_market, city_to_zip


def print_market(market):

    state, market_name, street, city, zip_code = market[0:5]
    return "\n\t{}\n\t{}\n\t{}, {} {}\n".format(market_name, street, city.title(), state, zip_code)


if __name__ == "__main__":

    FILENAME = "markets.txt"

    try: 
        zip_to_market, city_to_zip = read_markets(FILENAME)

        while True:
            search = input("Enter a City or ZIP Code to find your local market, or say 'quit' to exit: ").lower().strip()
            
            if search.lower() == "quit":
                print("\nThanks for shopping local - Goodbye!")
                break
                
            zip_codes = city_to_zip[search]
            if not zip_codes:
                zip_codes = [search]
                
            found = False
            for zip_code in zip_codes:
                markets = zip_to_market[zip_code]
                for market in markets:
                    found = True
                    print(print_market(market))
     
            if not found:
                print("\n\t" + search.title(), "was not found\n")
    
    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
        
