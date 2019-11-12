import itertools

def permutation(word):
    lst = []
    for i in itertools.permutations(word.lower()):
        if "".join(i) == "".join(i[::-1]):
            lst.append("".join(i))
    return lst[0] if lst else "no"
word=input()
print(permutation(word))



