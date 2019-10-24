def rem(n, ele, count):
    k = 0
    for i in range(len(n)):
        if n[i] == ele:
            k += 1
            if k == count:
                print(n[i+1:])
num = int(input())
for _ in range(num):
    n = input()
    ele = input()
    count = int(input())
    rem(n,ele,count)
   
    
