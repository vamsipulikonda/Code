n=int(input())
s=[int(i)for i in input().split()]
res = set(s) - set([i for i in s if s.count(i) == 1])
print(res if res else "unique")
    