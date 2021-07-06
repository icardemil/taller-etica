def digitize(n):
    temp = [int(i) for i in str(n)]
    return temp[::-1]
print(digitize(12345))