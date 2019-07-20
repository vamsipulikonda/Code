#vishal
#vishnu
#op_ vish

import os
n=int(input())
lst = []
lst2=[]
for i in range(n):
    lst.append(input())
print(os.path.commonprefix(lst))