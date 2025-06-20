""" wimbledon.py
Estimate : 40 minutes
Actual: 1 hour  """


FILENAME = "wimbledon.csv"

def main ():
    """ Main program to process and display wimbledon data. """
    wimbledon_data = read_wimbledon_data (FILENAME)
    champion_to_wins = count_champion_wins (wimbledon_data)
    countries = get_unique_countries (wimbledon_data)
    print ("Wimbledon Champions:")
    for champion , wins in champion_to_wins.items():
        print (f"{champion} {wins}")

    print ()
    print (f"These {len(countries)} countries have won wimbledon:")
    print (",".join(countries))


def read_wimbledon_data (filename):
    """ Read data from the CSV file and return a list of [champion country]."""
    with open (filename, "r", encoding = "utf-8-sig") as in_file:
        in_file.readline()
        data=[]
        for line in in_file:
            parts = line.strip().split(",")
            champion = parts [2].strip()
            country = parts [1].strip()
            data.append([champion, country])
        return data

def count_champion_wins (wimbledon_data):
    """Return a dictionary mapping champion to names to win counts. """
    champion_to_wins = {}
    for champion in wimbledon_data:
        if champion in champion_to_wins:
            champion_to_wins [ champion] += 1
        else:
            champion_to_wins [ champion]= 1
    return champion_to_wins

def get_unique_countries(wimbledon_data):
    """Return a sorted set of unique countries from the data."""
    countries = {country for _, country in wimbledon_data}
    return sorted (countries)



main()


