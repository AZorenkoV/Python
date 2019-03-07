import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
lucky = 0

for x in range(num1, num2+1) :
    number = list(str(x))
    while len(number) != 6 :
        number.insert(0, 0)
    count1 = 0
    for i in number[:3]:
        count1 += int(i)
    count2 = 0
    for i in number[3:]:
        count2 += int(i)
    if count1 == count2:
        lucky += 1

print lucky
