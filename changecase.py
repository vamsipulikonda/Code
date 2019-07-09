"""
Sample Input
6
Dcoder
0 3
Sample Output:
dcoDer
"""
n=int(input())
a=list(input())
lst=[int(i) for i in input().split()]
for i in lst:
    if a[i].isupper():
        a[i]  = a[i].lower()
    else:
        a[i] = a[i].upper()
        
print(''.join(a))