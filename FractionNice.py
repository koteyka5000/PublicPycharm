class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def get_numerator(self):  # Получиить числитель
        return self.numer

    def get_denominator(self):  # Получить знаменатель
        return self.denom

    def flip(self):  # Перевернуть дробь: 3/6 - 6/3
        return Fraction(self.denom, self.numer)

    def __str__(self):  # print()
        return f'{self.numer} / {self.denom}'

    def __add__(self, other):  # Сложение +
        new_1 = self.numer * other.denom + self.denom * other.numer
        new_2 = self.denom * other.denom
        return Fraction(new_1, new_2)

    def __sub__(self, other):  # Вычитание -
        new_1 = self.get_numerator() * other.get_denominator() - self.get_denominator() * other.get_numerator()
        new_2 = self.get_denominator() * other.get_denominator()
        return Fraction(new_1, new_2)

    def __mul__(self, other):  # Умножение *
        q = self.numer * other.numer
        w = self.denom * other.denom
        return Fraction(q, w)

    def __float__(self):  # float()
        return self.numer / self.denom

    def __int__(self):  # int()
        return int(self.numer / self.denom)

    def __truediv__(self, other):  # деление /
        q = self.numer * other.denom
        w = self.denom * other.numer
        return Fraction(q, w)


q12 = Fraction(2, 2)
q13 = Fraction(8, 3)
qwe = q12 / q13
print(qwe)