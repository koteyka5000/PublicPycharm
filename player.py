from random import choice


def get_area(s):
    area = []
    s -= 1
    f = True
    tmp = ['X']
    allq = ['_', '_', '_', 'o']
    for i in range(s):  # По вертикале поле генерируется на 1 меньше, но мне кажется так выглядит лучше,
        for j in range(s):  # Это можно исправить, добавив +1 в for i in range(s + 1)
            tmp.append(choice(allq))
        area.append(tmp)
        tmp = []
        if f:
            s += 1
        f = False
    return [area, s]


def print_map(area):
    print('==========')
    for i in range(len(area)):
        # print(*area[0], '\n', *area[1], '\n', *area[2], '\n', *area[3], sep='')
        print(*area[i], sep=' ')
    print('==========')


def helpq():
    print('+=+=+=+=+=+=+=+=+=+=+=')
    print('''Назначение клавиш:
    w - Вверх
    a - Влево
    s - Вниз
    d - Вправо
    r - Перезагрузить карту, например если некуда ходить
    reset - Почти полная перезагрузка движка
    f3 - Вкл / Откл показ координат
    mf3 - Режим полной откладки      BETA
    Дополнительно при моделе keyboard (Сочетание клавиш):
    Ctrl + 1 - Вкл / Откл показ координат
    
    Также можно использовать 
    русские слова для перемещения.''')
    input('Нажмите Enter для продолжения ')
    print('''Обьекты:
    X - Персонаж
    _ - Пустая клетка
    o - Стена
    ''')


def f3on_off():
    global isf3
    if not isf3:
        isf3 = True
    else:
        isf3 = False


def mf3on_off():
    global ismf3
    if not ismf3:
        ismf3 = True
    else:
        ismf3 = False

try:
    import keyboard

    keyboard.add_hotkey('ctrl+1', f3on_off)
except:
    print('У вас не установлен модуль keyboard. Для использования дополнительных функций, можно его установить:\n'
          'pip install keyboard')

isf3 = False
ismf3 = False

def game(areaq):
    print('=+=+=+=+=\nВведите help для обучения\n=+=+=+=+=')
    process = True
    area = areaq[0]
    area_len = areaq[1]
    print_map(area)
    nowx = 0
    nowy = 0
    while process:
        where = input('Куда: ')

        if where == "вниз" or where == 's':
            if nowy != area_len - 2:
                if not area[nowy + 1][nowx] == 'o':
                    nowy += 1
                    area[nowy][nowx] = 'X'
                    area[nowy - 1][nowx] = '_'
                else:
                    print('Тут стена :|')
            else:
                print('Вы дошли до края платформы!')

        elif where == "вверх" or where == 'w':
            if nowy != 0:
                if not area[nowy - 1][nowx] == 'o':
                    nowy -= 1
                    area[nowy][nowx] = 'X'
                    area[nowy + 1][nowx] = '_'
                else:
                    print('Тут стена :|')
            else:
                print('Вы дошли до края платформы!')

        elif where == "право" or where == 'd':
            if nowx != area_len - 1:
                if not area[nowy][nowx + 1] == 'o':
                    nowx += 1
                    area[nowy][nowx] = 'X'
                    area[nowy][nowx - 1] = '_'
                else:
                    print('Тут стена :|')
            else:
                print('Вы дошли до края платформы!')

        elif where == "лево" or where == "a":
            if nowx != 0:
                if not area[nowy][nowx - 1] == 'o':
                    nowx -= 1
                    area[nowy][nowx] = 'X'
                    area[nowy][nowx + 1] = '_'
                else:
                    print('Тут стена :|')
            else:
                print('Вы дошли до края платформы!')

        elif where == 'help':
            helpq()

        elif where == 'r':
            if input('Введите r ещё раз для подтверждения') == 'r':
                area = get_area(area_len)[0]
                nowx = 0
                nowy = 0
            else:
                print('+=+ОТМЕНЕНО+=+')

        elif where == 'reset':
            process = False
            game(get_area(int(input('Размер поля: '))))

        elif where == 'f3':
            f3on_off()

        elif where == 'mf3':
            mf3on_off()

        if ismf3:
            print(f'''X={nowx}
Y={nowy}
Area_len={area_len}
Where={where}
process={process}
isf3={isf3}''')

        if isf3:
            print(f'X={nowx}, Y={nowy}')
        print_map(area)


game(get_area(int(input('Размер поля: '))))
