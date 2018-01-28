def rev(x, prod=0):
    if x < 10:
        return prod + x
    else:
        print prod,x
        prod = prod * 10 + x%10 * 10
        print "After operatation: ",prod, x
        return rev(x / 10, prod)


def isPalindrome(num):
    if(num==rev(num)):print "Palindrome %s"%(num)
    else:print "Not Palindrome %s"%(num)

print rev(1945)

isPalindrome(131)
isPalindrome(1945)