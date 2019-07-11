n=int(input())
b=[]
a=[int(i) for i in input().split()]
d = {i:bin(i)[2:].count('1') for i in a}
print(sorted(d, reverse=True))