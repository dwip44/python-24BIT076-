class Time:
    def _init_(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def _str_(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

t1 = Time(2, 45)
t2 = Time(1, 30)
t3 = t1.add(t2)
print("Time after addition:", t3)
