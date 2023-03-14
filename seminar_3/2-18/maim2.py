items = [1,2,3,4,5] # список чисел
value = 6        # число к которому найти ближайшее
 
def nearest_value(items, value):
    '''Поиск ближайшего значения до value в списке items'''
    found = items[0]        # принимаем допущение что ближайшее число к искомому первое в списке (с индексом 0)
    for item in items:      # для каждого элемента (item) из items (т.е. попеременно item=1, item=2..)
        # проверяем условие если разница между item value по модулю меньше разницы found и value, то
        if abs(item - value) < abs(found - value): # если условие истинно (True)
            found = item # меняем значение нашего допущения на item (т.е. item оказался ближе к искомому значению)
    return found # возвращаем ближайшее значение до value в списке items
 
print(f'Ближайшее число к {value} в списке {items} является {nearest_value(items, value)}')