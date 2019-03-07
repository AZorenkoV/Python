def count_holes(n):
    one_holes = ['0', '4', '6', '9']
    if isinstance(n, str):
        n = long(n)
    if isinstance(n, int) or isinstance(n, long):
        line = str(n)
        holes = 0
        for x in line:
            if x in one_holes:
                holes+=1
            elif x == '8':
                holes+=2
        return holes
    return 'ERROR'


print count_holes(143)
print count_holes('001')
print count_holes(8.0)
print count_holes(-8)
print count_holes(8888888888)
print count_holes(69L)
