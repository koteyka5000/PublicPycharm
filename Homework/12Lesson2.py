class Player:
    def attack(self):
        print(f'{self.name} attacks!')


class Mage(Player):
    def __init__(self):
        self.name = 'mage'


class Barb(Player):
    def __init__(self):
        self.name = 'barbarian'


m = Mage()
b = Barb()
while 1:
    q = input('Кого атакуем? - ')
    if q == 'mage':
        m.attack()
    elif q == 'barbarian':
        b.attack()
    elif q == 'exit':
        break
    else:
        print('Try Again or type exit to finish')