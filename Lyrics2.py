def get_txt():
    with open('lyrics.txt', encoding='utf8') as f:
        return f.read()


def get_lyrics(lyrics):
    return lyrics.replace('(', '').replace(')', '').replace('!', '').replace(',', '').replace('.',
                                                                                              '').lower().split()


def found_dupes(txt):
    print(txt)
    check_dupes = {}
    for w in txt:
        w.lower()
        if w not in check_dupes:
            check_dupes[w] = 1
        else:
            check_dupes[w] += 1
    return check_dupes


def check_what(what, check_dupes):
    if what == 'all':
        for q in check_dupes.items():
            print(f'{q[0]}: {q[1]}')
    elif what == 'min':
        print(f'{min(check_dupes)}: {check_dupes.get(min(check_dupes))}')
    elif what == 'max':
        print(f'{max(check_dupes)}: {check_dupes.get(max(check_dupes))}')
    else:
        if what in check_dupes:
            print(f'{what}: {check_dupes.get(what)}')
        else:
            print('Такого слова в тексте не нашлось')


def start():
    check_dupes = found_dupes(get_lyrics(get_txt()))
    what = ''
    print('exit - Выход\nall - Посмотреть все значения\nmin - посмотреть самое малоиспользуемое слово'
          '\nmax - посмотреть самое частоиспользуемое слово\n<Слово> - Посмотреть информацию о нужном слове')
    while what != 'exit':
        what = input('Действие: ')
        print('===========')
        check_what(what, check_dupes)
        print('===========')


start()
