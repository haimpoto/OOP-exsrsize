from OOP_1 import Person

class Student(Person):
    def __init__(self, name: str, age: int, city: str, student_id: str, grade: int) -> None:
        super().__init__(name, age, city)
        self.student_id = student_id
        self.grade = grade

    def study(self) -> None:
        print(f"{self.name} study in {self.grade} grade.")

    def introduce(self) -> None:
        super().introduce()
        print("study in {self.grade} grade.")

    def advance_grade(self) -> None:
        self.grade += 1

class Teacher(Person):
    def __init__(self, name: str, age: int, city: str, subject: str, years_experience: int) -> None:
        super().__init__(name, age, city)
        self.subject = subject
        self.years_experience = years_experience

    def teach(self) -> None:
        print(f"H{self.name} tich {self.subject} for {self.years_experience} years")

    def introduce(self) -> None:
        super().introduce()
        print(f"tich {self.subject}")

    def gain_experience(self) -> None:
        self.years_experience += 1

class Principal(Person):
    def __init__(self, name: str, age: int, city: str, years_as_principal):
        super().__init__(name, age, city)
        self.years_as_principal = years_as_principal

    def manage(self):
        print(f"{self.name} manage the mosad {self.years_as_principal} years")

    def introduce(self):
        super().introduce()
        print("the principal of the mosad")

    def add_management_experience(self):
        self.years_as_principal += 1

a = Student("haim", 23, "petah tikva", "1", 12)
b = Teacher("moshe", 33, "bney brak", "English", 10)
c = Principal("david", 37, "petah tikva", 5)

# a.study()
# b.teach()
# c.manage()
#
# a.advance_grade()
# b.gain_experience()
# c.add_management_experience()
#
# a.study()
# b.teach()
# c.manage()