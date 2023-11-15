def sumZero(n):
    list = []
    i = 1
    sum = 0
    for i in range(1, n):
        list.append(i)
        sum += i

    list.append(-sum)
    return list


n = 5
print(sumZero(n))
