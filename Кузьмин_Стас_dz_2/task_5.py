# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

def find_sign(num):
    if num[0] in '+-':
        return num[0]


price_list = [30.90, 20.52, 42, 90, 15, 59, 60, 65.90, 86.50, 30.50, 13.40, 21.90, 30, 36.90, 20.06]
price_kk = []
price_cc = []
prices = []
for i in range(len(price_list)):
    price = round(price_list[i] // 1)

    i = i + 1
    price_kk.append(price)
for i in range(len(price_list)):
    kk = round((price_list[i] % 1) * 1, 2)
    i = i + 1
    if kk <= 1:
        r = round(kk * 100)
        if r <= 10:
            null = str(0)
            r = str(r)
            r = null + r.zfill(0)
    price_cc.append(r)
# print(price_kk)
# print(price_cc)
for i in range(len(price_kk)) and range(len(price_cc)):
    r = f'{price_kk[i]} рублей {price_cc[i]} копеек'
    i = i + 1
    prices.append(r)
str_list = ', '.join(prices)
print(str_list)
# Задание B
sort = sorted(prices)
sort_list = ', '.join(sort)
print(sort_list)
# Задание C
new_prices = prices
unsort = sorted(new_prices, reverse=True)
unsort_list = ', '.join(unsort)
print(unsort_list)
