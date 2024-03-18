"""
Contains functions that take the original data through the f1 api and sort it
such that it can be properly used in further parsing functions
"""

import json
import os
import requests

def fetch(url):
    """Fetch data from url and return a JSON object"""
    r = requests.get(url)
    data = r.json()
    return data


def dump(data, filename):
    """Save JSON object to file"""
    f = open(filename, 'w')
    data = json.dump(data, f)
    f.close()


def load(filename):
    """Load JSON object from file"""
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data


"""
\"data\" object can contain the following information:
    - year
    - round
    - circuitId
    - constructorId
    - driverId
    - grid position
    - results position
    - fastest rank
    - statusId
    - data type: e.g. season, race, race results along with the intended 'type' of data type
"""

data = {'year': 2014, 'round': 10, 'circuits': 'monza', 'constructors': 'mercedes', 'drivers': 'hamilton',
         'grid': 14, 'results': 4, 'fastest': 2, 'status': 'statusId', 'datatype': 'standings', 'lap': 24, 'pit_num': 1}

def fetch_f1_data(data, limit=30, use_cache=True):
    """
    Fetch data from Ergast for data types specifically requested, returning
    as a JSON object.
    
    Fetched data is dumped to a cached file so on subsequent call it can optionally
    be retreived from the cache file. This is faster than the retrieval over the 
    internet as well as not clogging up the Ergast servers.
    
    Args:
        use_cache: If ``True``, use file cache. o/w fetch data from internet.
        
    Returns:
        Requested data as a .json file
    """

    """
    Data that can be included in the request includes:
        - Season: tuple that can contain a circuitId, constructorId, driverId, grid position,
                results position, fastest rank, statusId (if none lists currently supported seasons)
        - Race: tuple that can contain a circuitId, constructorId, driverId, grid position, 
                results position, fastest rank, statusId (if just year lists race schedule, info
                about specific race add round number)
        - Race Results: tuple that can contain a circuitId, constructorId, driverId, grid position,
                        fastest rank, statusId (if just race lists the results)
        - Quali Results: tuple that can contain circuitId, constructorId, driverId, grid position,
                        results position, fastest rank, statusId (if just race lists the quali results)
        - Standings: can request after a specific race, at end of season, all those who finished
                    at a point in the standings for a season, results for a specific driver, results
                    for a specific constructor
        - Driver info: tuple that can contain a circuitId, constructorId, driverId, grid position,
                        results position, fastest rank, statusId, can also request list of drivers in
                        a series, year or round
        - Constructor info: tuple that can contain circuitId, constructorId, driverId, grid position,
                            results position, fastest rank, statusId, can also request list of
                            constructors in a series year or round.
        - Circuit info: tuple that can contain constructorId, driverId, grid position, results position,
                        fastest rank, statusId, can also obtain the list of circuits used within a 
                        series, year or round.
        - Finishing status: tuple that can contain circuitId, constructorId, driverId, grid position,
                            results position, fastest rank, statusId, can just obtain list of finishing
                            status codes.
        - Lap times: need to specify the season, round and lap number. can also include driver data.
        - Pit stops: need to specify a season and round, can request all data for a round or a stop number,
                    can also include driver data or lap number
    """
    # URL for retreiving data from the Ergast API:

    url = """http://ergast.com/api/f1/{data}.json?limit={limit}"""

    sub_dir = 'cache'


    if data['datatype'] == 'seasons':                   # Lists the seasons
        for i in data:
            if data[i] == None or 'seasons':
                sub_str = 'seasons'
            else:
                break
        sub_str = "{year}/{round}/{circuits}/{drivers}/{grid}/{results}/{fastest}/{status}/"
        sub_str.format(data['year'], data['round'], data['circuits'], data['drivers'], data['grid'],
                       data['results'], data['fastest'], data['status'])
    elif data['datatype'] == 'races':                   # Lists the races
        pass
    elif data['datatype'] == 'results':                 # Lists the race results
        pass
    elif data['datatype'] == 'qualifying':              # Lists the qualifying results
        pass
    elif data['datatype'] == 'driverStandings':         # Lists the driver standings
        pass
    elif data['datatype'] == 'constructorStandings':    # Lists the constructor standings
        pass
    elif data['datatype'] == 'drivers':                 # Lists the drivers
        pass
    elif data['datatype'] == 'constructors':            # Lists the constructors
        pass
    elif data['datatype'] == 'circuits':                # Lists the circuits
        pass
    elif data['datatype'] == 'status':                  # Lists the finishing status codes
        pass
    elif data['datatype'] == 'laps':                    # Gives the lap times
        pass
    elif data['datatype'] == 'pitstops':                # Lists the pit stops
        pass

    ### Make seperate caches for different strings of information that are called
    try:
        os.makedirs(sub_dir)
    except FileExistsError:
        pass
    cache_file = os.path.join(sub_dir, 'f1_data.json')


    ### Make this so that it can retreive data from the correct cache if it exists
    # Attempt to load data from file, o/w fetch over internet
    if use_cache:
        try:
            # Attempt to load data from file
            data = load(cache_file)
        except FileNotFoundError:
            # If load from file fails, fetch and dump to file
            data = fetch(url.format(data, limit))
            dump(data, cache_file)

    return data