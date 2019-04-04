
'''
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]




way1:
def friend(x):
    return [f for f in x if len(f) == 4]


way2:
def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

way3:
def friend(x):
    return list(filter(lambda name: len(name) == 4, x))
'''
def friend(x):
    return list(filter(lambda name: len(name) == 4, x))

str1=["Ryan", "Kieran", "Mark",]

print(friend(str1))















