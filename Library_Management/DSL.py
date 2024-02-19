from functools import partial
from typing import Any

class IF(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return IF(partial(self.func, other))
    def __call__(self, v1,v2):
        return self.func(v1,v2)
        
        
@IF
def printfile(x):
    fs = open(x, "r")
    datas = fs.read()

    ds_gs = datas.split("\n")
    fs.close()
    ds_gs.pop()

    return ds_gs

print( printfile|"Library_Management/books.csv")