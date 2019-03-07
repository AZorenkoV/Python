# coding: utf8
"""
Розробити функцію clean_list(list_to_clean),
яка приймає 1 аргумент - список будь-яких значень (рядків, цілих та дійсних чисел) довільної довжини,
та повертає список, який складається з тих самих значень, але не містить повторів елементів. Це значить,
що у випадку наявності значення в початковому списку в кількох екземплярах перший екземпляр значення
залишається на своєму місці, а другий, третій та ін. видаляються.

Наприклад
Виклик функції: clean_list([1, 1.0, '1', -1, 1])
Повертає: [1, 1.0, '1', -1]
Виклик функції: clean_list(['qwe', 'reg', 'qwe', 'REG'])
Повертає: ['qwe', 'reg', 'REG']
Виклик функції: clean_list([32, 32.1, 32.0, -123])
Повертає: [32, 32.1, 32.0, -123]
Виклик функції: clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
Повертає: [1, 2, 3, 4, 5, 6, '2', 7, 8, 9, 0]
"""
def clean_list(list_to_clean):
    new_list = []
    for x in range(len(list_to_clean)):
        if str(list_to_clean[x]) not in new_list:
            new_list.append(list_to_clean[x])
    return new_list


#Example 1
list = [1, 1.0, '1', -1, 1]
print list
list = clean_list(list)
print list
#Example 2
list = ['qwe', 'reg', 'qwe', 'REG']
print list
list = clean_list(list)
print list
#Example 3
list = [32, 32.1, 32.0, -123]
print list
list = clean_list(list)
print list
#Example 4
list = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
print list
list = clean_list(list)
print list
