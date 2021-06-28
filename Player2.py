from random import choice
import pickle


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
    save - Сохранить игру в файл
    load - Загрузить игру из файла
    ! reset - Почти полная перезагрузка движка
    f3 - Вкл / Откл показ координат
    mf3 - Режим полной откладки             DELETED
    ! Дополнительно при моделе keyboard (Сочетание клавиш):
    ! Ctrl + 1 - Вкл / Откл показ координат
    КЛАВИШИ У КОТОРЫХ В НАЧАЛЕ ЕСТЬ ! ВРЕМЕННО НЕ РАБОТАЮТ
    
    Также можно использовать 
    русские слова для перемещения.''')
    input('Нажмите Enter для продолжения ')
    print('''Обьекты:
    X - Персонаж
    _ - Пустая клетка
    o - Стена
    ''')


def f3on_off(isf3):
    if not isf3:
        isf3 = True
    else:
        isf3 = False
    return isf3


def mf3on_off(ismf3):
    if not ismf3:
        ismf3 = True
    else:
        ismf3 = False
    return ismf3


def check_wall(area, x, y):
    if not area[y][x] == 'o':
        return True
    else:
        print('Тут стена :|')
        return False


def move(area, nowx, nowy, xnowx, xnowy):
    if check_wall(area, xnowx, xnowy):
        area[xnowy][xnowx] = 'X'
        area[nowy][nowx] = '_'
        return xnowx, xnowy
    return nowx, nowy


def move_up(area, nowx, nowy):
    if nowy != 0:
        xnowx = nowx
        xnowy = nowy - 1
        nowx, nowy = move(area, nowx, nowy, xnowx, xnowy)
    else:
        print('Вы дошли до края платформы!')
    return nowx, nowy


def move_down(area, nowx, nowy, area_len):
    if nowy != area_len - 2:
        nowx, nowy = move(area, nowx, nowy, nowx, nowy + 1)
    else:
        print('Вы дошли до края платформы!')
    return nowx, nowy


def move_left(area, nowx, nowy):
    if nowx != 0:
        nowx, nowy = move(area, nowx, nowy, nowx - 1, nowy)
    else:
        print('Вы дошли до края платформы!')
    return nowx, nowy


def move_right(area, nowx, nowy, area_len):
    if nowx != area_len - 1:
        nowx, nowy = move(area, nowx, nowy, nowx + 1, nowy)
    else:
        print('Вы дошли до края платформы!')
    return nowx, nowy


def load():
    try:
        with open('playerData.data', 'rb') as f:
            data = pickle.load(f)
        return data['nowx'], data['nowy'], data['area'], data['area_len']
    except FileNotFoundError:
        print('Не найден файл сохранения')


def save(area, nowx, nowy, area_len):
    data = {'area': area, 'nowx': nowx, 'nowy': nowy, 'area_len': area_len}
    with open('playerData.data', 'wb') as f:
        pickle.dump(data, f)
    print('Сохранение прошло успешно!')


def reset_map(area_len, area, nowx, nowy):
    if input('Введите r ещё раз для подтверждения') == 'r':
        area = get_area(area_len)[0]
        return area, 0, 0
    else:
        print('+=+ОТМЕНЕНО+=+')
        return area, nowx, nowy


def check_where(where, area, nowx, nowy, area_len, isf3):
    if where == 'w':
        nowx, nowy = move_up(area, nowx, nowy)
    elif where == 's':
        nowx, nowy = move_down(area, nowx, nowy, area_len)
    elif where == 'a':
        nowx, nowy = move_left(area, nowx, nowy)
    elif where == 'd':
        nowx, nowy = move_right(area, nowx, nowy, area_len)
    elif where == 'save':
        save(area, nowx, nowy, area_len)
    elif where == 'load':
        try:
            nowx, nowy, area, area_len = load()
        except TypeError:
            pass
        else:
            print('Загрузка прошла успешно')
    elif where == 'help':
        helpq()
    elif where == 'r':
        area, nowx, nowy = reset_map(area_len, area, nowx, nowy)
    elif where == 'f3':
        isf3 = f3on_off(isf3)
    return nowx, nowy, area, area_len, isf3


# try:
#     import keyboard
#     isf3 = True
#     keyboard.add_hotkey('ctrl+1', lambda: f3on_off(isf3))
# except:
#     print('У вас не установлен модуль keyboard. Для использования дополнительных функций, можно его установить:\n'
#           'pip install keyboard')


def game(areaq):
    print('=+=+=+=+=\nВведите help для обучения\n=+=+=+=+=')
    process = True
    where = ''
    isf3 = True
    area = areaq[0]
    area_len = areaq[1]
    print_map(area)
    nowx = 0
    nowy = 0
    while process:
        last = where
        where = input('Куда: ')
        if where == '':
            where = last
            print(where)
        nowx, nowy, area, area_len, isf3 = check_where(where, area, nowx, nowy, area_len, isf3)
        if isf3:
            print(f'X={nowx}, Y={nowy}')
        print_map(area)


game(get_area(int(input('Размер поля: '))))
