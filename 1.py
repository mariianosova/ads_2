lines = """\tАрифметика для старших\tГеометрия в четырехмерье\tЭсперанто для начинающих
Пятёрка\t205\t300\t420
Академкнига\t500\t200\t250
Всё для школы\t350\t350\t350""".split('\n')

book_names = lines[0][1:].split('\t')
shops = [i.split('\t') for i in lines[1:]]
shop_names = [i[0] for i in shops]
shop_total = [int(i[1]) + int(i[2]) + int(i[3]) for i in shops]

res_shop_name = min(list(zip(shop_names, shop_total)), key=lambda i: i[1])[0]
res_shop = [i for i in shops if i[0] == res_shop_name]

print(res_shop_name)
for i in list(zip(book_names, res_shop[0][1:])):
    print(' '.join(i))