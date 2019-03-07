def clean_list(list_to_clean):
    new_list = []
    for x in range(len(list_to_clean)):
        if str(list_to_clean[x]) not in new_list:
            new_list.append(list_to_clean[x])
    return new_list

def counter(a, b):
    count = 0
    a_new = clean_list(list(str(a)))
    b_new = clean_list(list(str(b)))
    for x in a_new:
        if x in b_new:
            count += 1
    return count

print counter(12345, 567)
print counter(1233211, 12128)
print counter(123, 45)
