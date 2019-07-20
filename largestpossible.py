n = int(input())
lst = [int(i) for i in input().split()]
lst = list(sorted(lst, reverse=True))
print(''.join([str(i) for i in lst]))
