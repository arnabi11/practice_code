def gcd(x,y):
    # print x,y
    least = min(x, y)
    while True:
        if x%least == 0 and y%least == 0:
            print "GCD is", least
            break
        else:
            least-= 1


    
# gcd(36,27)

gcd(int(raw_input("Enter 1st num: ")), \
    int(raw_input("Enter 2nd num: "))  \
    )


