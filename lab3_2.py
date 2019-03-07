import sys

a = 1
result = 0
end = int(sys.argv[1])

if end > 0 :
	for count in range(end):
		if count == 1 :
			temp = 1
		else :
			temp = result
		result = result + a
		a = temp

print(result)
		
