def longest(names):
    newNames = ''
    for i in names:
        if len(i) > len(newNames):
            newNames = i
    return newNames
names = ['rohit', 'kamal', 'kamalkant', 'qwertyuio']
displayName = longest(names)
print(displayName)