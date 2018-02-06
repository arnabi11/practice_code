def sumofSquares(num):
    sum = 0
    for i in range(0,num+1):
        sum = sum+(i*i)
    return sum

x = int(raw_input("Enter N: "))
result = sumofSquares(x)
print result