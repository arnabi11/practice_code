# k = 5
# j = k
# stars = 0
# spaces="  "#2Spaces
# starImg = "* "
# while k>0:
#     stars += 1
#     whites = k-stars
#     line = []
#     str1 = ""
#     for i in range (0,whites):line.append(spaces)
#     for i in range (0,stars):line.append(starImg)
#     string = ""
#     for i in line:
#         string += i
#     print ''.join(line)
#     # print string
#     if k==stars:break

# for i in range(1, 9):
#     for i in range(-1+i, -1, -1):
#         print(format(2**i, "4d")),
#     print

# a = input('Enter value of a: ')
# b = input('Enter value of b: ')

# temp = a
# a = b
# b = temp

# print('After swapping a: {}'.format(a))
# print('After swapping b: {}'.format(b))

# num = raw_input("Enter any number: ") 
# rev_num = reversed(num) 
# # check if the string is equal to its reverse 
# if list(num) == list(rev_num): 
#              print("Palindrome number") 
# else: 
#              print("Not Palindrome number")


# def isPrime(num):
#     isPrime = True
#     for i in range(2,num/2):
#         if num%i==0:
#           isPrime = False
#           break
#     return isPrime
    

# def Main():
#   n = int(raw_input("Enter range: "))
#   for i in range(2,n+1):
#       if(isPrime(i)):
#           print "The number ",i,"is Prime",isPrime(i)


# Main()

# year = int(input("Enter any Year: "))
# if year%4==0:  
#     print  "Year is Leap"  
# else:  
#     print "Year is not Leap"  

# def isPrime(num):
#     isPrime = True
#     for i in range(2,num/2):
#         if num%i==0:
#           isPrime = False
#           break
#     return isPrime
    

# def Main():
#   n = int(raw_input("Enter range: "))
#   for i in range(2,n+1):
#       if(isPrime(i)):
#           print "The number ",i,"is Prime",isPrime(i)


# Main()


# print ("The reversed string is:",(raw_input())[::-1])


# printAllOnes(14)
# printLinesWith_0_and_1(14)
# mainPrinter(int(raw_input("Enter N: ")))

# function which return reverse of a string
# def reverse(s):
#     return s[::-1]
 
# def isPalindrome(s):
#     # Calling reverse function
#     rev = reverse(s)
 
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False
 
 
# # Driver code
# s = raw_input()
# ans = isPalindrome(s)
 
# if ans == 1:
#     print("Yes")
# else:
#     print("No")


# a = int(raw_input())
# b = int(raw_input())
# print("\nBefore swap a = %d and b = %d" %(a, b))
# a, b = b, a
# print("\nAfter swaping a = %d and b = %d" %(a, b))
# print()


n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    print dig
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
def sumOfDigits(rev):
    if rev==0:
        # print 0
        return 0
    else:
        print (rev%10)
        return (rev % 10) + sumOfDigits(rev // 10)

print sumOfDigits(rev)
