def seqprinter(num):
    string=""
    for i in range(1,(num*2)):
        string+=str(i)
    print string

def mainPrinter(num):
    for i in range(1,num+1):
        seqprinter(i)
    for i in range(num-1,0,-1):
        seqprinter(i)

x=int(raw_input("Enter N: "))
mainPrinter(5)
