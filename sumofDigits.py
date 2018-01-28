def sumOfDigits(number):
    if number==0:
        # print 0
        return 0
    else:
        return (number % 10) + sumOfDigits(number // 10)

print sumOfDigits(121)

