class MyString:
    def _init_(self, value=""):
        self.value = value

    def _iadd_(self, other):
        self.value += other.value
        return self

    def toLower(self):
        return self.value.lower()

    def toUpper(self):
        return self.value.upper()

    def _str_(self):
        return self.value

s1 = MyString("Hello")
s2 = MyString("World")
s1 += s2
print("Concatenated:", s1)
print("Lowercase:", s1.toLower())
print("Uppercase:",s1.toUpper())