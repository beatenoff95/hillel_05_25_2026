from math import pi, sqrt


def sum_numbers(numbers_string):
    numbers = numbers_string.split(",")
    return sum(int(number.strip()) for number in numbers)


def create_team_lead(name, salary, department, programming_language, team_size):
    return {
        "name": name,
        "salary": salary,
        "department": department,
        "programming_language": programming_language,
        "team_size": team_size,
    }


def rectangle_area(width, height):
    return width * height


def rectangle_perimeter(width, height):
    return 2 * (width + height)


def circle_area(radius):
    return pi * radius ** 2


def circle_perimeter(radius):
    return 2 * pi * radius


def triangle_perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c


def triangle_area(side_a, side_b, side_c):
    if (
        side_a + side_b <= side_c
        or side_a + side_c <= side_b
        or side_b + side_c <= side_a
    ):
        raise ValueError("Triangle sides are invalid")

    half_perimeter = triangle_perimeter(side_a, side_b, side_c) / 2
    return sqrt(
        half_perimeter
        * (half_perimeter - side_a)
        * (half_perimeter - side_b)
        * (half_perimeter - side_c)
    )


def square_area(side):
    return side ** 2


def square_perimeter(side):
    return 4 * side
