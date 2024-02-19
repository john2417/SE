def superprint(a,b,function):
    
    return lambda x: print((function()),x*(a+b))

def mul(a,b):
    return a*b
def load_genres():
    fs = open("Library_Management/genres.csv", "r")
    datas = fs.read()
        # datas:["peom\non-novel\nnovel\n"]
    ds_gs = datas.split("\n")  # divid them by \n
        # dg_gs:["peom","non-novel","novel",""]
    fs.close()
    ds_gs.pop()  # Delete the last argument
        # ds_gs:["peom","non-novel","novel"]
    return ds_gs
a = superprint(2,4,load_genres)

b = a("!")

print(b)


get_sub = lambda a,b :a-b

print(get_sub(2,3))
print((lambda a,b : a - b)(2,3))
