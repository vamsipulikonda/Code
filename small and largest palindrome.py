n=input('enter a string')
z=[]
def reverse(a):
    return a[::-1]
for i in range(len(n)+1):
    for j in range(len(n)+1):
        if n[i:j]==reverse(n[i:j]):
            z.append(n[i:j])
y=[i for i in z if len(i)>2 and len(i)!=0]
print(max(y))
print(min(y))
    
