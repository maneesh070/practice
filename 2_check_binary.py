def isBinary(str):
    for i in str:
        if i == '0' or i == '1':
            continue
        else:
            return False
    return True
str = '111012'
binary = isBinary(str)
print(binary)