def toLower(S):
    lowerCase = ''
    for i in S:
        asciiValue = ord(i)
        if asciiValue >= 65 and asciiValue <= 90:
            asciiValue += 32
            asciiValue = chr(asciiValue)
            lowerCase += asciiValue
        else:
            lowerCase += i
    return lowerCase


S = "qqWWWEErr"
Lower = toLower(S)
print(Lower)