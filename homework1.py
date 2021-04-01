#ДЗ Сделать класс fraction тоесть взять из математики дробь и сделать её альтернативу в python, с аттрибутами и методами. Методы должны правильно считать дробь к дроби. К примеру
# fraction1.add(fraction2)
# тоесть дробь в методах принимает 1 экземпляр дроби и делает красивый принт результата. Дз скидывать мне в ввиде ссылки на ваше репо в github в лс.

class Fraction(object):
    def __init__(self, top, bottom):
        self.top = int(top)
        self.bottom = int(bottom)

    def Minus(self, n1):
        if self.bottom == n1.bottom:
            self.top -= self.top
        else:
            self.top = self.top * n1.bottom - self.bottom * n1.top
            self.bottom = self.bottom * n1.bottom

    def addition(self, n1):
        self.top += n1.top
        self.bottom += n1.bottom

    def multiply(self, n1):
        self.top *= n1.top
        self.bottom *= n1.bottom

    def display(self):
        print('top of fraction   ', self.top)
        print('bottom of fraction', self.bottom)
        print(f'fraction {self.top}/{self.bottom}')

num = Fraction(2, 7)
num1 = Fraction(5, 7)
num.display()
print()
num1.display()
print()

num3 = Fraction(3, 7)
num4 = Fraction(4, 9)

print('result of subtract')
num3.Minus(num4)
num3.display()
print()

num5 = Fraction(3, 7)
num7 = Fraction(4, 17)

print('result of addition')
num5.addition(num7)
num5.display()
print()

num8 = Fraction(5, 25)
num9 = Fraction(7, 21)
print('result of multiply')
num8.multiply(num9)
num8.display()
