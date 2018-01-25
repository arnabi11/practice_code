def printAllOnes(len):
    string = ""
    for i in range(0,len):
        string+="1"+" "
    print string

def printLinesWith_0_and_1(len):
    string="1 "
    for i in range(0,len-2):
        string+="0 "
    string+="1"
    print string

def mainPrinter(num):
    if(num<=0):
        return
    if(num<=3):
        i = 1
        while i<=num:
            printAllOnes(i)
            i+=1
    else:
        printAllOnes(1)
        printAllOnes(2)
        for i in range(3,num):
            printLinesWith_0_and_1(i)
        printAllOnes(num)

# printAllOnes(14)
# printLinesWith_0_and_1(14)
mainPrinter(int(raw_input("Enter N: ")))