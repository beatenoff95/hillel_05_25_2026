from abc import ABC, abstractmethod
from math import pi, sqrt


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def test_team_lead_attributes():
    team_lead = TeamLead("Ivan", 5000, "Development", "Python", 7)

    assert hasattr(team_lead, "name")
    assert hasattr(team_lead, "salary")
    assert hasattr(team_lead, "department")
    assert hasattr(team_lead, "programming_language")
    assert hasattr(team_lead, "team_size")


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.__radius


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2
        return sqrt(
            half_perimeter
            * (half_perimeter - self.__side_a)
            * (half_perimeter - self.__side_b)
            * (half_perimeter - self.__side_c)
        )

    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return 4 * self.__side


if __name__ == "__main__":
    test_team_lead_attributes()
    print("TeamLead has all required attributes.")

    figures = [
        Rectangle(4, 6),
        Circle(5),
        Triangle(3, 4, 5),
        Square(7),
    ]

    for figure in figures:
        print(f"{figure.__class__.__name__}:")
        print(f"Area: {figure.get_area():.2f}")
        print(f"Perimeter: {figure.get_perimeter():.2f}")
