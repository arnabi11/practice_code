def uniquePrinter(string):
    s1 = set(string)        #Gets all the unique chars in string
    print s1                #Prints the array
    # s2=''.join(s1)        #Using single line join statement
    # print s2
    s2=""                   #convert the array to string
    for i in s1:
        s2+=str(i)
    print s2
# return s2                 #Use this if you want the function  to return



s = "Hello there"
# s = str(raw_input("Enter the string:"))
uniquePrinter(s)
uniquePrinter(s.upper())
uniquePrinter(s.lower())
# str1 = uniquePrinter(s)   #Use this in combination with return statement in function
