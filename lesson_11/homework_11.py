def sum_numbers(numbers_string):
    numbers = numbers_string.split(",")
    return sum(int(number) for number in numbers)


numbers_list = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3",
]

for item in numbers_list:
    try:
        print(sum_numbers(item))
    except ValueError:
        print("Не можу це зробити!")
