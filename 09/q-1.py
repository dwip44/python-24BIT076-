class Complex:
    def _init_(self, real, imag):
        self.real = real
        self.imag = imag

    def _add_(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def _sub_(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def _mul_(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def _truediv_(self, other):
        denom = other.real*2 + other.imag*2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def _str_(self):
        return f"{self.real} + {self.imag}i"

a = Complex(3, 2)
b = Complex(1, 7)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

