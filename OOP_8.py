class User:
    __user_count = 0
    __users_list = []

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.__password_hash = User.__password_hash(password)
        User.__user_count += 1
        User.__users_list.append(self)

    @staticmethod
    def __password_hash(password: str) -> str:
        return str(hash(password))

    @staticmethod
    def is_valid_email(email: str) -> bool:
        if "@" not in email:
            return False
        at = email.index("@")
        if "." not in email[at:]:
            return False
        return True

    @staticmethod
    def is_strong_password(password: str) -> bool:
        if len(password) < 8:
            return False
        digits = False
        big = False
        small = False
        for char in password:
            if char.isdigit():
                digits = True
            elif char.isupper():
                big = True
            elif char.islower():
                small = True
        if digits and big and small:
            return True
        return False

    @staticmethod
    def create_user_safely(username: str, email: str, password: str) -> User | None:
        if User.is_valid_email(email) and User.is_strong_password(password):
            return User(username, email, password)
        print("Error. The user is don't create")
        return None

    @classmethod
    def get_user_count(cls) -> int:
        return cls.__user_count

    @classmethod
    def find_user_by_username(cls, username) -> str | None:
        for user in cls.__users_list:
            if user.username == username:
                return user
        return None


# u1 = User.create_user_safely("haim", "qwerty@gmail.com", "Hp12345678")
# u2 = User.create_user_safely("moshe", "qwert@y.", "1234uuuA")
# print(User.get_user_count())
# print(User.find_user_by_username("haim"))
# print(User.find_user_by_username("david"))

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, num: int) -> None:
        if num > 0:
            self.__width = num
        else:
            print("Error. width must be positive")

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, num: int) -> None:
        if num > 0:
            self.__height = num
        else:
            print("Error. height must be positive")

    @property
    def area(self) -> int:
        return self.__width * self.__height

    @property
    def perimeter(self) -> int:
        return (self.__width + self.__height) * 2

    @property
    def is_square(self) -> bool:
        return self.__width == self.__height

    @staticmethod
    def create_square(side) -> Rectangle:
        return Rectangle(side, side)

    @staticmethod
    def compare_areas(rect1: Rectangle, rect2: Rectangle) -> str:
        if rect1.area > rect2.area:
            return "Rectangle 1 is bigger"
        elif rect1.area < rect2.area:
            return "Rectangle 2 is bigger"
        else:
            return "Both Rectangles are the same size"


# r1 = Rectangle(12, 5)
# r2 = Rectangle.create_square(7)
# print(Rectangle.compare_areas(r1, r2))


class Product:
    TAX_RATES = {
        "food": 0.0,
        "books": 0.0,
        "electronics": 0.10,
        "clothing": 0.17,
        "other": 0.17
    }

    def __init__(self, category: str, base_price: int | float, name: str = "other", discount_percent: int = 0) -> None:
        self.category = category
        self.base_price = base_price
        self.__name = name
        self.discount_percent = discount_percent

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str) -> None:
        if category in Product.TAX_RATES:
            self.__category = category
        else:
            print("Error. invalid category")

    @property
    def base_price(self) -> int | float:
        return self.__base_price

    @base_price.setter
    def base_price(self, price: int | float) -> None:
        if price > 0:
            self.__base_price = price
        else:
            print("Error: price can't be negative")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def discount_percent(self) -> int:
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, num: int) -> None:
        if 0 <= num <= 100:
            self.__discount_percent = num
        else:
            print("Error. discount_percent nust be between 0 and 100")

    @property
    def price_after_discount(self) -> float:
        return self.__base_price * (1 - self.__discount_percent / 100)

    @property
    def final_price(self) -> float:
        return self.price_after_discount * (1 + Product.TAX_RATES[self.__category])

    @staticmethod
    def get_tax_rate(category: str) -> float:
        if category in Product.TAX_RATES:
            return Product.TAX_RATES[category]
        else:
            return Product.TAX_RATES["other"]

    @staticmethod
    def calculate_bulk_discount(quantity: int, unit_price: int | float) -> float:
        if quantity < 10:
            return 0.0
        elif quantity < 50:
            return (unit_price * quantity) * 0.05
        elif quantity < 100:
            return (unit_price * quantity) * 0.1
        else:
            return (unit_price * quantity) * 0.15


# a1 = Product("food", 10, "bread", 10)
# a2 = Product("clothing", 100, "shirt", 20)
# print(a1.final_price)
# print(a2.final_price)
