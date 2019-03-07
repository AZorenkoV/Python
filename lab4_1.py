import sys
string = sys.argv[1].lower().replace(" ", "")

#print(string)
if string == string[::-1] :
    print('YES')
else :
    print('NO')
