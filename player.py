from random import choice


def get_area(s):
    area = []
    s -= 1
    f = True
    tmp = ['X']
    allq = ['_', '_', '_', 'o']
    for i in range(s):
        for j in range(s):
            tmp.append(choice(allq))
        area.append(tmp)
        tmp = []
        if f:
            s += 1
        f = False

    # area = [['X', '.', '.', '.'],
    #         ['.', 'o', '.', '.'],
    #         ['.', '.', '.', 'o'],
    #         ['.', '.', '.', '.']]
    print(area)
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
    reset - Полная перезагрузка движка
    
    Также можно использовать 
    русские слова для перемещения.''')
    input('Нажмите Enter для продолжения ')
    print('''Обьекты:
    X - Персонаж
    _ - Пустая клетка
    o - Стена
    ''')
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
            if nowy <= area_len - 2:
                pass
            try:
                if not area[nowy + 1][nowx] == 'o':
                    nowy += 1
                    area[nowy][nowx] = 'X'
                    area[nowy - 1][nowx] = '_'
                else:
                    print('Тут стена :|')

            except:
                print('Вы дошли до края платформы!')


        elif where == "вверх" or where == 'w':
            if nowy >= area_len - 3:
                pass
            try:

                if not area[nowy - 1][nowx] == 'o':
                    nowy -= 1
                    area[nowy][nowx] = 'X'
                    area[nowy + 1][nowx] = '_'
                else:
                    print('Тут стена :|')

            except:
                print('Вы дошли до края платформы!')


        elif where == "право" or where == 'd':
            if nowx <= area_len - 2:
                pass
            try:

                if not area[nowy][nowx + 1] == 'o':
                    nowx += 1
                    area[nowy][nowx] = 'X'
                    area[nowy][nowx - 1] = '_'
                else:
                    print('Тут стена :|')

            except:
                print('Вы дошли до края платформы!')


        elif where == "лево" or where == "a":
            if nowx >= area_len - 3:
                pass
            try:
                if not area[nowy][nowx - 1] == 'o':
                    nowx -= 1
                    area[nowy][nowx] = 'X'
                    area[nowy][nowx + 1] = '_'
                else:
                    print('Тут стена :|')

            except:
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
            game(get_area(area_len))

        print(f'X={nowx}, Y={nowy}')
        print_map(area)


game(get_area(int(input('Размер поля: '))))
