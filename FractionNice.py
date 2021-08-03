class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def get_numerator(self):
        return self.numer

    def get_denominator(self):
        return self.denom

    def __str__(self):
        return f'{self.numer} / {self.denom}'

    def __add__(self, other):
        new_1 = self.get_numerator() * other.get_denominator() + self.get_denominator() * other.get_numerator()
        new_2 = self.get_denominator() * other.get_denominator()
        return Fraction(new_1, new_2)

    def __sub__(self, other):
        new_1 = self.get_numerator() * other.get_denominator() - self.get_denominator() * other.get_numerator()
        new_2 = self.get_denominator() * other.get_denominator()
        return Fraction(new_1, new_2)

    def __mul__(self, other):
        q = self.numer * other.numer
        w = self.denom * other.denom
        return Fraction(q, w)

    def __float__(self):
        return self.numer / self.denom


q12 = Fraction(2, 2)
q13 = Fraction(8, 3)
qwe = q12 * q13
print(qwe)
