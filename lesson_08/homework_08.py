class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_average_grade):
        self.average_grade = new_average_grade

    def show_info(self):
        print(f"Name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")


student = Student("Ivan", "Petrenko", 20, 88.5)

student.show_info()

student.change_average_grade(94.0)

print("\nAfter changing average grade:")
student.show_info()
