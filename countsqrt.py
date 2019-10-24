import math
def sqtt(n):
    c=0
    if math.sqrt(n)== math.floor(math.sqrt(n)):
        return 0
    return 1

n=[int(i) for i in input().split()]

x=map(sqtt,n)

print(sum(list(x)))

