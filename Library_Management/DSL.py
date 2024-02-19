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
        # datas:["시\n수필\n소설\n"]
    ds_gs = datas.split("\n")  # 개행 문자를 기준으로 분리
        # dg_gs:["시","수필","소설",""]
    fs.close()
    ds_gs.pop()  # 맨 마지막 원소 삭제

    return ds_gs

print( printfile|"Library_Management/books.csv")