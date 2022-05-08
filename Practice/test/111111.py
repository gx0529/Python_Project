def divide(a, b):
    if a == 0:
        return 0

    tmp = abs(b)
    result = abs(a)
    count = 0
    while result >= tmp:
        temp = tmp
        num = 1

        while temp+temp < result:
            num += 1
            temp += temp

        count += num
        result -= tmp*num
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return count
    else:
        return -count

print(divide(-2147483648,-1))