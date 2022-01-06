def countZeros(n):
    res = 0
    i = 5
    for i in range(1, n):
        i = i * 5
        res = res + n//i
    return res

if __name__ == '__main__':
    print("Number of Trailing zeros : % d" % (countZeros(10)))