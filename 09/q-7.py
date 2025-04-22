class Weather:
    def _init_(self, parameters):
        self.parameters = parameters

    def _contains_(self, item):
        return item in self.parameters

w = Weather(["sunny", "windy", "humid"])
print("sunny" in w)
print("snowy" in w)  

