class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def addition(self, other):
        top = self.top * other.bottom + other.top * self.bottom
        bottom = self.bottom * other.bottom
        print('result of addition')
        print(top)
        print('--')
        print(bottom)

    def subtract(self, other):
        top = self.top * other.bottom - other.top * self.bottom
        bottom = self.bottom * other.bottom
        print('result of subtraction')
        print(top)
        print('--')
        print(bottom)


    def multiply(self, other):
        top = self.top * other.top
        bottom = self.bottom * other.bottom
        print('result of multiply')
        print(top)
        print('--')
        print(bottom)

    def division(self, other):
        top = self.top * other.bottom
        bottom = self.bottom * other.top
        print('result of division')
        print(top)
        print('--')
        print(bottom)

fraction1 = Fraction(3, 5)
fraction2 = Fraction(2, 15)
fraction1.addition(fraction2)
print()
fraction1.subtract(fraction2)
print()
fraction1.multiply(fraction2)
print()
fraction1.division(fraction2)