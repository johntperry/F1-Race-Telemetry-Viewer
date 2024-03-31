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

data['datatype'] = 'constructors'
#data['constructors'] = 'redbull'
data['drivers'] = 'ricciardo'

print(fetch_f1_data(data))