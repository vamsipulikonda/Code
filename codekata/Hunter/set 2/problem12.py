n, x = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]
print(sorted(set(lst))[-x])