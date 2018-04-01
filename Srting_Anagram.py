def main():
    str1 = raw_input()
    str2 = raw_input()
    str1 = sorted(str1)
    str2 = sorted(str2)
    str_one = ''.join(str1)
    str_two = ''.join(str2)
    if len(str_one)==len(str_two):
        if str_one==str_two:print "True"
        else:
            print "False"
    else:
        print "False"

main()