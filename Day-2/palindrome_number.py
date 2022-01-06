def palindromeNumber(n):
    rev = 0
    temp = n
    while(temp!= 0):
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    if(rev == n):
        print("Its a palindrome number")
    else:
        print("No its not a palindrome number")
        
if __name__ == '__main__':
    palindromeNumber(360)