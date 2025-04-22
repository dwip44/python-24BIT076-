class Shape:
    def _init_(self, shape, data):
        self.shape = shape
        self.data = data

    def area(self):
        if self.shape == "circle":
            r = self.data['radius']
            return 3.1416 * r ** 2
        elif self.shape == "square":
            s = self.data['side']
            return s ** 2
        elif self.shape == "rectangle":
            return self.data['length'] * self.data['breadth']
        return 0

    def perimeter(self):
        if self.shape == "circle":
            r = self.data['radius']
            return 2 * 3.1416 * r
        elif self.shape == "square":
            return 4 * self.data['side']
        elif self.shape == "rectangle":
            return 2 * (self.data['length'] + self.data['breadth'])
        return 0

rect = Shape("rectangle", {"length": 5, "breadth": 3})
print("Area:", rect.area(), "Perimeter:", rect.perimeter())
