def super_fibonacci(n , m):
    if n < 1:
        print "Error!"
        return 0

    if n <= m :
        return 1
    summ_fibonacci = 0

    for x in range(0, m):
        summ_fibonacci += super_fibonacci(n - x - 1, m)

    return summ_fibonacci


#print fibonacci(0, 2)
#print fibonacci(1, 2)
print super_fibonacci(2, 1)
print super_fibonacci(3, 5)
#print fibonacci(4, 2)
#print fibonacci(5, 2)
#print fibonacci(6, 2)
#print fibonacci(7, 2)
print super_fibonacci(8, 2)
print super_fibonacci(9, 3)
print super_fibonacci(9, 4)
