import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
content = response.content.decode(encoding=response.encoding)


def currency_rates (char):
    my_list1=[]
    my_list2=[]
    for el in content.split('CharCode>')[1:]:
        code = el.split('<')[0]
        my_list1.append(code)
    for el in content.split('Value>')[1:]:
        numb = el.split('<')[0]
        my_list2.append(numb)

    result = dict(zip(my_list1, my_list2))
    numbs = char
    print(f'{numbs} = {result[numbs]} руб')
    return result[numbs]


print(currency_rates('USD'))
print(currency_rates('EUR'))

