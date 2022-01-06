def factorialNumber(n):
    res = 1
    i = 2
    for i in range(n):
        i = i + 1
        res = res * i
    return res

if __name__ == '__main__':
    print("Factorial is : % d" % (factorialNumber(5)))