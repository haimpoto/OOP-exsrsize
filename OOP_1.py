class Person:
    def __init__(self, name:str, age:int, city:str):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"hello. I am {self.name}, I am {self.age} years old, from {self.city}.")

    def have_birthday(self):
        self.age += 1
        print(f"happy birthday!! now {self.name} {self.age} years old")

a = Person("abraham", 18, "jerusalem" )
b = Person("isaac", 25, "petah tikva")
c = Person("jacob", 50, "haifa")

# a.introduce()
# b.introduce()
# c.introduce()
# b.have_birthday()

class Mosad:
    def __init__(self, name: str, mosad_type: str, students_count: int, city: str):
        self.name = name
        self.type = mosad_type
        self.students_count = students_count
        self.city = city

    def print_details(self):
        print(f"{self.name} is a {self.type} in {self.city}, there are {self.students_count} students there")

    def add_students(self, students_num):
        if students_num > 0:
            self.students_count += students_num

    def remove_students(self, students_num):
        if students_num > 0:
            self.students_count -= students_num

a = Mosad("Kodcode", "university", 100, "petah tikva")
b = Mosad("Htron", "Yeshiva", 1000, "jerusalem")

# a.print_details()
# b.print_details()
#
# a.add_students(50)
# b.remove_students(20)
#
# a.print_details()
# b.print_details()