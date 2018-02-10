'''
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Constraints 
 
 

Input Format

The first line contains integers,  and  separated by a space. 
The next  lines contains the words belonging to group . 
The next  lines contains the words belonging to group .

Output Format

Output  lines. 
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and . 
'b' appeared  times in positions  and . 
In the sample problem, if 'c' also appeared in word group , you would print .
'''


from collections import defaultdict

def main():
    din = map(int, (raw_input().split()))
    numA = din[0];numB=din[1]
    lst1 = [];lst2 = []
    for i in range(0,numA):
        lst1.append(raw_input())
    # print lst1
    for i in range(0,numB):
        lst2.append(raw_input())
    # print lst2
    dict1 = defaultdict(list)
    for i in range(0,len(lst1)):
        dict1[lst1[i]].append(i+1)
    # dict2 = dict(list)
    for i in range(0,len(lst2)):
        templst = dict1[lst2[i]]
        if len(templst)<1:
            print -1
        else:
            print ' '.join(map(str,templst))
    # print dict1

if __name__=="__main__":
    main()