def gcd(a, b):
    res = min(a, b)
    while(res > 0):
        if(a % res == 0 and b % res == 0):
            break
        res -= 1
    return res

if __name__ == '__main__':
    print("Greatest Common divisor is : % d" % (gcd(10, 15)))


###################################### (approach - 2 using euclidean algorithm) ##########################

# def gcd(a, b):
#     while(a!= b):
#         if(a > b):
#             a = a - b
#         else:
#             b = b - a
#     return a
# if __name__ == '__main__':
#     print("Greatest Common divisor is : % d" % (gcd(100, 200)))

#############################################################################################################

################################### (approach - 3 optimized euclidean algorithm) ############################

# def gcd(a, b):
#     if(b == 0):
#         return a
#     else:
#         return gcd(b, a%b)
#
# if __name__ == '__main__':
#     print("Greatest Common divisor is : % d" % (gcd(10, 20)))

################################################################################################################