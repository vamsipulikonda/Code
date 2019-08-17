import itertools

def triplet(n,a):
    count=0
    for i in range(2,int(n)):
        for i in itertools.combinations(a,i):
            if sum(i) in a:
                print(i)
                count+=1
    return count


a=[]
num=int(input())
for k in range(num):
    n=input()
    a = [int(i) for i in input().split()]
    print(triplet(n,a))