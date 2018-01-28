#code
def power(num,pow):
    if(pow==0):
        return 1 # -*- coding: latin-1 -*-
    if(pow==1):
        return num
    else:
        return(num*power(num,pow-1))

num = int(raw_input("Enter N: "))
exp = int(raw_input("Enter exp: "))
print power(num,exp)