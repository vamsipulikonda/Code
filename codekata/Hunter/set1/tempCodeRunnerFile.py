n=input()
lst=[int(i) for i in input().split()]
a=set(lst)-set(i for i in lst if lst.count(i)>1)
for i in a:
    print(i, end=' ')


    