import sys

line = sys.argv[1]

if (len(line)%2) == 0 :
    if len(line) == 0 :
        print "YES"
    else :
        if line[0] == '(' :
            count = 0
            for x in line :
                if x == '(':
                    count += 1
                else :
                    count -= 1
                    if count < 0 :
                        break
            if count == 0 :
                print "YES"
            else :
                print "NO"
        else:
            print "NO"
else :
    print "NO"
