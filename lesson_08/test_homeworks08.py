from math import pi
from unittest import TestCase

from lesson_08.homeworks import (
    circle_area,
    circle_perimeter,
    create_team_lead,
    rectangle_area,
    rectangle_perimeter,
    square_area,
    square_perimeter,
    sum_numbers,
    triangle_area,
    triangle_perimeter,
)


class TestHomeworks(TestCase):
    def test_sum_numbers_returns_sum_for_comma_separated_numbers(self):
        self.assertEqual(sum_numbers("1,2,3,4"), 10)

    def test_sum_numbers_ignores_spaces_around_numbers(self):
        self.assertEqual(sum_numbers("10, 20, 30"), 60)

    def test_sum_numbers_raises_value_error_for_non_number(self):
        with self.assertRaises(ValueError):
            sum_numbers("qwerty1,2,3")

    def test_create_team_lead_contains_all_required_fields(self):
        team_lead = create_team_lead("Ivan", 5000, "Development", "Python", 7)

        self.assertEqual(
            team_lead,
            {
                "name": "Ivan",
                "salary": 5000,
                "department": "Development",
                "programming_language": "Python",
                "team_size": 7,
            },
        )

    def test_rectangle_area_returns_width_multiplied_by_height(self):
        self.assertEqual(rectangle_area(4, 6), 24)

    def test_rectangle_perimeter_returns_sum_of_all_sides(self):
        self.assertEqual(rectangle_perimeter(4, 6), 20)

    def test_circle_area_returns_pi_multiplied_by_radius_squared(self):
        self.assertEqual(circle_area(5), pi * 25)

    def test_circle_perimeter_returns_circumference(self):
        self.assertEqual(circle_perimeter(5), 10 * pi)

    def test_triangle_perimeter_returns_sum_of_sides(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_triangle_area_returns_heron_formula_result(self):
        self.assertEqual(triangle_area(3, 4, 5), 6)

    def test_triangle_area_raises_value_error_for_invalid_sides(self):
        with self.assertRaises(ValueError):
            triangle_area(1, 2, 10)

    def test_square_area_returns_side_squared(self):
        self.assertEqual(square_area(7), 49)

    def test_square_perimeter_returns_four_sides_sum(self):
        self.assertEqual(square_perimeter(7), 28)
