def PalinArrey(arr):
    for i in arr:
        arr2 = str(i)
        if arr2[::] == arr2[::-1]:
            continue
        else:
            return 0
    return 1
arr = [111, 222, 333, 444, 55455, 100]
n = len(arr)
palindrome = PalinArrey(arr)
print(palindrome)