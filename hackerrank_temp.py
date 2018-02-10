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