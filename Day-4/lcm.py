def lcm(a, b):
    res = max(a, b)
    while(True):
        if(res%a == 0 and res%b == 0):
            return res
        res = res + 1
    return res

if __name__ == '__main__':
    print("LCM of two numbers is : % d" % (lcm(2, 8)))


