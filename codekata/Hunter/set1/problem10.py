n, m = [int(i) for i in input().split()]
lst1=[int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
if set(lst2).issubset(set(lst1)):
    print("YES")
else:
    print("NO")