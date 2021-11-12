#Вывод времени

days = 86400
hours = 3600
minuts = 60

duration = int(input('Введите промежуток времени в секундах: '))
duration= duration % (24*86400)
if duration < minuts:
    print('{} сек '.format(duration))
elif minuts <= duration and hours> duration:
    my_minute= duration// minuts
    my_second = duration% minuts
    print('{} мин {} сек '.format(my_minute,my_second))
elif duration>= hours and duration<days:
    my_hour = duration// hours
    duration=duration% hours
    my_minute= duration// minuts
    my_second = duration% minuts
    print('{} часов {} мин {} сек '.format(my_hour,my_minute,my_second))
elif duration >= days:
    my_days = duration // days
    duration = duration % days
    my_hour = duration // hours
    duration = duration % hours
    my_minute = duration // minuts
    my_second = duration % minuts
    if duration % days ==0:
        print('{} часов {} мин {} сек '.format( my_hour, my_minute, my_second))
    print('{} дней {} часов {} мин {} сек '.format(my_days, my_hour, my_minute, my_second))
