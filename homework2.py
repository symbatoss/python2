# Complex
# 1) magic method (+, -, /, *)
# 2) return Complex ->
# complex2 = Complex(2, 5)
# complex3 = complex1 + complex2
# 3) __str__

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'{self.real}+{self.imag}' + 'i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __truediv__(self, other):
        return Complex(self.real / other.real, self.imag / other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imag * other.imag)
comp1 = Complex(10, 12)
comp2 = Complex(5, 5)
print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 / comp2)
print(comp1 * comp2)
