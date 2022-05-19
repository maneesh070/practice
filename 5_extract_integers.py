def extractIntegerWords(s):
    a = '0123456789'
    b = ''
    for i in s:
        if i in a:
            b = b + i
        elif i>='a' and i<='z' or i>='A' or i<='Z':
            b += ''
        else:
            None
    return b

s = '1 Cool, 11. Cold, 01 Ice, 200C'
extraction = extractIntegerWords(s)
print(extraction)