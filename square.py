class Square:
    def __init__(self, length):
        self.length = length

    @property
    def area(self):
        return self.length ** 2

    @area.setter
    def area(self, new_area):
        self.length = new_area ** 0.5

    @property
    def circumference(self):
        return self.length * 4

    @circumference.setter
    def circumference(self, new_circumference):
        self.length = new_circumference // 4

s1 = Square(10)
print(s1.length, s1.circumference) # 10 40
s1.length = 5
print(s1.length, s1.circumference) # 5 20
s1.circumference = 100
print(s1.length, s1.circumference)