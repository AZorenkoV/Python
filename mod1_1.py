"""
Для кодування повідомлень Френсіс Бекон запропонував кожну літеру тексту замінювати на групу з п'яти
символів «А» або «B» (назвемо їх "ab-групами"). Для співставлення літер і кодуючих ab-груп в даному
завданні використовується ключ-ланцюжок aaaaabbbbbabbbaabbababbaaababaab, в якому порядковий номер
літери відповідає порядковому номеру початку ab-групи.

Наприклад: літера "а" - перша літера алфавіту; для визначення її коду беремо 5 символів з ключа, починаючи
з першого: aaaaa. Літера "c" - третя в алфавіті, отже для визначення її коду беремо 5 символів з ключа,
починаючи з третього: aaabb.

Таким чином, оригінальне повідомлення перетворюється на послідовність ab-груп і може далі бути накладене
на будь-який текст відповідної довжини: А позначається нижнім регістром, В - верхнім.
"""
import sys

line = sys.argv[1]
line = line.replace(' ', '')
result = []
for x in range(len(line)/5):
    result.append(line[x*5:((x+1)*5)])

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for x in range(len(result)):
    outer = ""
    for c in result[x]:
        if(c.isupper()):
            outer += "b"
        else :
            outer += "a"
    result[x] = outer

keyResult = ''
for sub in result:
    keyResult += alphabet[key.index(sub)]

print(keyResult)
