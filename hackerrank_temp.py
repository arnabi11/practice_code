from collections import defaultdict

def main():
    pass

if __name__ == '__main__':
    main()

    dict1 = defaultdict(list)
    print type(dict1["hello"])
    dict2 = {}
    dict2["arm"]="mam"
    dict2["arm2"]=["mam1"]
    print type(dict2["arm"])
    print type(dict2["arm2"])
    dict1["arm1"] = "mam"
    dict2["arm1"] = 23

    print type(dict1["arm1"])
    print len(dict2)
    for key,val in dict2.iteritems():
        print ("key:%s, value:%s"%(key,val))
    
    