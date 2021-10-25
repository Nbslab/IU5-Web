from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from abc import ABC, abstractmethod

class Greeter(ABC):
    @abstractmethod
    def greeting():
        pass

class GreeterLab2(Greeter):
    def greeting():
        print("-"*35)
        print("Лабораторная работа №2. \nВыполнил студент группы РТ5-51Б\nНезаметдинов Т. И.")
        print("-" * 35)
        print('')


def main():
    simple_greeter = GreeterLab2
    simple_greeter.greeting()
    rectangle = Rectangle("синего", 10, 11)
    circle = Circle("зеленого", 11)
    square = Square("красного", 11)
    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()