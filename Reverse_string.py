print ("The reversed string is:",(raw_input("Please enter the string: "))[::-1])

str1="HEllo World"
def reverse_string(stringData):
    x = ""
    for i in range(len(stringData),0,-1):
        x += str(stringData[i-1])
    print x


reverse_string(str1)