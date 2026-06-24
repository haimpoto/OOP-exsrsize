class Animal:
    def __init__(self, legs_num, suns_num):
        self.tail = None
        self.legs_num = legs_num
        self.suns_num = suns_num

    def add_tail(self, length, thickness, speed):
        self.tail = Tail(length, thickness, speed)


class Tail:
    def __init__(self, length, thickness, speed):
        self.length = length
        self.thickness = thickness
        self.speed = speed


class Cat(Animal):
    def __init__(self, color, mustache_length, legs_num=4, suns_num=4):
        super().__init__(legs_num, suns_num)
        self.color = color
        self.mustache_length = mustache_length
        self.mice_counter = 0

    def hunt_mouse(self):
        self.mice_counter += 1

    def get_hunted_mice(self):
        return self.mice_counter


lion = Animal(4, 5)
lion.add_tail(30, 5, 30)
print(lion.tail.speed)
mizi = Cat("black", 8)
shifrah = Cat("yellow", 17.5)