import numpy as np

# METHOD : METHOD TO MAP ANOTHER METHOD TO A LIST OF INPUTS
#@decorator.decorator
def MathDecor(Function, *args, **kwargs):
    """Apply a method on a set/list/tuple of entries"""
    
    import functools   #, decorator
    
    @functools.wraps(Function)
    def Wrapper(*args, **kwargs):
        #if isinstance(args, (list, tuple)):
        return Function(*args, **kwargs)
    return Wrapper