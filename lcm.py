def lcm(x,y):
    greater=max(x,y)
    while True:
        if greater%x==0 and greater%y==0:
            print "LCM is",greater
            break
        else:
            greater+=1

x=int(raw_input("Enter the 1st no."))
y=int(raw_input("Enter the 2nd no."))



lcm(x,y)
