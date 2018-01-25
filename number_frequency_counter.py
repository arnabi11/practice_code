def freqCounter(num):

    bin = [0,0,0,0,0,0,0,0,0,0]
    # print len(bin)
    for i in num:
        bin[int(i)]+=1
    print "Frequency of each digits in %s is: "%(num)
    for i in range(0,len(bin)):
        print "Frequency of %s = %s"%(i,bin[i])

x= str(raw_input("Enter any number: "))

freqCounter(x)