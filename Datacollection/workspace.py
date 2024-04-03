from datafetcher import fetch_f1_data

data = {'year': None,
        'round': None,
        'circuits': None,
        'constructors': None,
        'drivers': None,
        'grid': None,
        'results': None,
        'fastest': None,
        'status': None,
        'datatype': None,
        'lap': None,
        'pit_num': None
        }

'''
datatypes include:
    - seasons
    - races
    - results
    - qualifying
    - driverStandings
    - constructorStandings
    - drivers
    - constructors
    - circuits
    - status
    - laps
    - pitstops
'''

data['datatype'] = 'constructors'
#data['constructors'] = 'redbull'
data['drivers'] = 'alonso'

print(fetch_f1_data(data))