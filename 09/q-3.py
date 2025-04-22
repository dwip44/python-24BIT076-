class Solid:
    def _init_(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def surface_area(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            return 6 * side ** 2
        elif self.shape == "sphere":
            r = self.dimensions['radius']
            return 4 * 3.1416 * r ** 2
        elif self.shape == "cylinder":
            r, h = self.dimensions['radius'], self.dimensions['height']
            return 2 * 3.1416 * r * (r + h)
        return 0

    def volume(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            return side ** 3
        elif self.shape == "sphere":
            r = self.dimensions['radius']
            return (4/3) * 3.1416 * r ** 3
        elif self.shape == "cylinder":
            r, h = self.dimensions['radius'], self.dimensions['height']
            return 3.1416 * r ** 2 * h
        return 0

cube = Solid("cube", {"side": 3})
print("Cube SA:", cube.surface_area(), "Vol:", cube.volume())
