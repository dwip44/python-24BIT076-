class Date:
    def _init_(self, day, month, year):
        self.date = [day, month, year]

    def _eq_(self, other):
        return self.date == other.date

d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
print("Dates are equal:", d1 == d2)

