n = int(input())
a=[]
lst=[int(i) for i in input().split()]


def right(lst,i):
    return all([lst[i]>j for j in lst[i+1:n]])
def left(lst,i):
    return all([lst[i]>j for j in lst[:i]])
print(" ".join([str(lst[i]) for i in range(n) if right(lst,i)]))
print(" ".join([str(lst[i]) for i in range(n) if right(lst,i) and left(lst,i)]))

     
