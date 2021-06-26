print('''Welcome to the birthday dictionary. We know birdth dates of:
Albert Einstein
Ada Lovelace
Guido van Rossum
What birth date you want to know?''')
q = input('Enter a name: ')
dates = {'Albert Einstein': '14/03/1879',
         'Ada Lovelace': '10/12/1815',
         'Guido van Rossum': '31/01/1956'}
if q in dates:
    print(f'{q}`s birthday is {dates[q]}')
else:
    print(f'We don\'t have recors for this name: {q}')
