def rev(x, prod=0):
    if x < 10:
        return prod + x
    else:
        print prod,x
        prod = prod * 10 + x%10 * 10
        print "After operatation: ",prod, x
        return rev(x / 10, prod)


print rev(1945)
