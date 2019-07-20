#find the value of x is a given eqation.
#INPUT:7+X=9   o/p:2

def add(input1):
    exp=input1[:input1.find('=')]
    a,b=exp.split("+")
    res=input1[input1.find("=")+1:]
    if a=="X":
        return int(res)-int(b)
    elif b=="X":
        return int(res)-int(a)
    else:
        return int(a)+int(b)
print(add(input()))
