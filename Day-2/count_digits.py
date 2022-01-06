
def countDigits(n):
    res = 0
    while(n > 0):
        n = n//10
        res = res + 1
    return res

if __name__ == '__main__':
    print("Number of digits : % d" % (countDigits(2112)))


