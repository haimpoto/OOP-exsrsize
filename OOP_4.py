class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    def deposit(self, num):
        self.__balance += num

    def withdraw(self, num):
        if num > self.__balance:
            self.__balance -= num

    def get_balance(self):
        print(self.__balance)

a1 = BankAccount("12", "david", 0)
a1.get_balance()

class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self._color = color
        self.__speed = 0

    def accelerate(self, speed_increase):
        self.__speed += speed_increase

    def brake(self, speed_decrease):
        if self.__speed > speed_decrease:
            self.__speed -= speed_decrease

    def get_speed(self):
        print(self.__speed)

    def get_color(self):
        print(self._color)

class Car(Vehicle):
    def __init__(self, model, color, max_speed):
        super().__init__(model, color)
        self.speed = 0
        self.__max_speed = max_speed

    def accelerate(self, speed_increase):
        if self.speed + speed_increase < self.__max_speed:
            self.__speed += speed_increase

    def get_max_speed(self):
        print(self.__max_speed)

class DigitalSafe:
    def __init__(self, safe_id: str, code: str) -> None:
        self._safe_id = safe_id
        self.__code = code
        self.__is_locked = False
        self.__attempt_count = 0

    def try_unlock(self, code) -> None:
        if not self.__is_locked:
            print("The safe is already open")
            return None
        if self.__attempt_count > 2:
            print("The attempts are over")
            return None
        if code == self.__code:
            self.__is_locked = False
            self.__attempt_count = 0
            print("The safe opens")
            return None
        self.__attempt_count += 1
        print(f"Incorrect password, {3 - self.__attempt_count} attempts remaining")
        return None


    def lock(self) -> None:
        self.__is_locked = True
        print("The safe is locked")

    def is_locked(self) -> bool:
        return self.__is_locked

    def get_attempt_left(self) -> int:
        return self.__attempt_count