from datacollection.datafetcher import fetch_f1_data

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

data['datatype'] = 'seasons'

print(fetch_f1_data(data))