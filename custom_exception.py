class NonIntArgumentException(Exception):
    pass    
    
def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args: 
            if type(arg) is not int:
                raise NonIntArgumentException
        return func(*args)
    return wrapper
