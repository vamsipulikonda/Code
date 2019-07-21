n=input()
lst=[int(i) for i in input().split()]
a=set(lst)-set(i for i in lst if lst.count(i)==1)
if a is not None:
    print(list(a)[0])
else:
    print("uinque")


    