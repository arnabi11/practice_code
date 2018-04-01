# k=4
# for i in range(0,3):
# 	for j in range(0,k):
# 		print (" ")
# 	print()
# 	k=k-2
# 	for j in range(0,i+1):
# 		print ("*")
# 	print()

# k = 8
# for i in range(0, 5):
#     for j in range(0, k):
#         print " "
#     print
#     k = k - 2
#     for j in range(0, i+1):
#         print "* "
#     print 

k = 7
j = k
stars = 0
spaces="  "#2Spaces
starImg = "* "
# while k>0:
#     stars += 1
#     whites = k-stars
#     line = []
#     str1 = ""

#     # for i in range (0,stars):line.append(starImg)
#     for i in range (0,whites):line.append(spaces)
#     for i in range (0,stars):line.append(starImg)

#     # for i in range (0,stars):line.append(starImg)
#     string = ""
#     for i in line:
#         string += i
#     print ''.join(line)
#     # print string
#     if k==stars:break

while k/2 >0:
	stars +=1
	line = []
	whites = k-stars-stars
	if k<=stars*2:
		for i in range(0,k):line.append(starImg)
	else:
		for i in range (0,stars):line.append(starImg)
	    	for i in range (0,whites):line.append(spaces)
    		for i in range (0,stars):line.append(starImg)
    
    print ''.join(line)
    if k/2<stars:break
