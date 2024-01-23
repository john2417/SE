def input_int(msg=''):
    try:
        ns = input(msg)
        return int(ns)
    except:
        return 0
def tryinput_int(msg=''):
    try:
        ns = input(msg)
        return int(ns),True
    except:
        return 0,False