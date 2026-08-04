# -*- coding: utf-8 -*-

class Rhombus:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а

    def __setattr__(self, name, value):
        if name == "сторона_а":
            if value <= 0:
                raise ValueError("Side сторона_а must be greater than 0")

        elif name == "кут_а":
            if not 0 < value < 180:
                raise ValueError("Angle кут_а must be greater than 0 and less than 180")

            super().__setattr__(name, value)
            super().__setattr__("кут_б", 180 - value)
            return

        elif name == "кут_б":
            angle_a = getattr(self, "кут_а", None)

            if angle_a is None:
                raise AttributeError("Angle кут_б is calculated automatically from кут_а")

            if angle_a + value != 180:
                raise ValueError("Angles кут_а and кут_б must add up to 180")

        super().__setattr__(name, value)

    def show_info(self):
        print(f"Side сторона_а: {self.сторона_а}")
        print(f"Angle кут_а: {self.кут_а}")
        print(f"Angle кут_б: {self.кут_б}")


if __name__ == "__main__":
    rhombus = Rhombus(10, 60)
    rhombus.show_info()

    print("\nAfter changing angle кут_а:")
    rhombus.кут_а = 120
    rhombus.show_info()
