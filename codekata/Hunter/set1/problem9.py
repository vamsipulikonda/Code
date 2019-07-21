n = int(input())
lst = [int(i) for i in input().split()]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == 0:
            print(lst[i],lst[j])