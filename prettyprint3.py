def seqprinter(num):
    string=""
    for i in range(1,num+1):
        string+=str(num*i)+" "
    print string

def mainprinter(num):
    for i in range(1,num+1):
        seqprinter(i)


# seqprinter(5)
if __name__ == '__main__':
    x = int(raw_input("Enter N: "))
    mainprinter(x)