#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Returns the addition of a and b
    
    Raises: TypeError if a and b are not integers or floats
    """
    if (not isinstance(a, (int, float))):
        raise TypeError('a must be an integer')
    
    if (not isinstance(b, (int, float))):
        raise TypeError('b must be an integer')
        
    return (int (a) + int(b))
