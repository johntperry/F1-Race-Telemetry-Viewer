class NoneInStr():
    def __format__(self, spec):
        return ''
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