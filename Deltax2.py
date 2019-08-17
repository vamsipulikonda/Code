"""5 2 3
3 3 2 3 1
op-2(no of elements with sum 6 and not having length 2)"""


import itertools
n, a, b=[int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
k = []
count=0
for i in range(n + 1):
    if i == a:
        continue
    for j in itertools.combinations(lst2,i):
        if sum(j) == b:
            # count+1
            k.append(j)
print(len(set(k)))

