#sort employee salary and if salary is same sort by name
n = [i for i in input().split()]
name=[]
sal=[]
x=[]
for i in range(len(n)):
    if i%2==0:
        name.append(n[i])
    else:
        sal.append(n[i])
dic = {}
for i in range(len(name)):
    dic[name[i]]=sal[i]

sv=sorted(dic.items(),key=lambda kv: kv[0])
for i in sv:
    x.append(i[0])
    x.append(i[1])
print(*x)

