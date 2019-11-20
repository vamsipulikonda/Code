for i, j in zip(lst, lst[1:]):
    if i==j:
        lst = lst.replace(i,'', 1)
print(lst)
