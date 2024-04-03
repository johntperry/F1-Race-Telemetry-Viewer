class NoneInStr():
    def __format__(self, spec):
        return '~'
    def __getitem__(self, name):
        return self
    
class formatting_dict(dict):
    '''
    Class that returns formatted dict values with a custom str,
    in this case \'\'. Also allows for nested dictionary values'''
    def __getitem__(self, name):
        value = self.get(name)
        if isinstance(value, dict):
            value = type(self)(value)
        return value if value is not None else NoneInStr
    
data = {'n': 3, 'k': 3.141594, 'p': {'a': 7, 'b': 8}}
del data['k']
data['p']['b'] = None

print('{0[n]}, {0[k]:.2f}, {0[p][a]}, {0[p][b]}'.format(formatting_dict(data)))