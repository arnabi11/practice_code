def uniquePrinter(string):
    s1 = set(string)      #Gets all the unique chars in string
    print s1               #Prints the array
    s2=""                   #convert the array to string
    for i in s1:
        s2+=str(i)
    print s2
    # return s2               #Use this if you want the function  to return

s = "Hello there"
uniquePrinter(s)

# str1 = uniquePrinter(s)   #Use this in combination with return statement in function