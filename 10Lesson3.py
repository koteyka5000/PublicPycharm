name = input('Имя: ')
typeq = input('Тип персонажа: ')
item = input('Предмет с собой: ')
poition = input('Зелье с собой: ')
player = {name: {typeq: {'item': item, 'poition': poition}}}
print('Составленный словарь:', player)