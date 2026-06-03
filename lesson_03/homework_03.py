alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02
print("Task 02")
print("All single quote symbols in the text:")

for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

# task 03
print("\nTask 03")
print(alice_in_wonderland)

# task 04
black_sea_area = 436_402
azov_sea_area = 37_800
total_sea_area = black_sea_area + azov_sea_area

print("\nTask 04")
print(f"Black Sea and Azov Sea together occupy {total_sea_area} km2.")

# task 05
total_goods = 375_291
first_and_second_warehouse = 250_449
second_and_third_warehouse = 222_950

third_warehouse = total_goods - first_and_second_warehouse
first_warehouse = total_goods - second_and_third_warehouse
second_warehouse = first_and_second_warehouse - first_warehouse

print("\nTask 05")
print(f"The first warehouse has {first_warehouse} goods.")
print(f"The second warehouse has {second_warehouse} goods.")
print(f"The third warehouse has {third_warehouse} goods.")

# task 06
months_in_year = 12
payment_years = 1.5
monthly_payment = 1_179
computer_price = int(months_in_year * payment_years * monthly_payment)

print("\nTask 06")
print(f"The computer costs {computer_price} UAH.")

# task 07
print("\nTask 07")
print(f"a) The remainder of 8019 / 8 is {8019 % 8}.")
print(f"b) The remainder of 9907 / 9 is {9907 % 9}.")
print(f"c) The remainder of 2789 / 5 is {2789 % 5}.")
print(f"d) The remainder of 7248 / 6 is {7248 % 6}.")
print(f"e) The remainder of 7128 / 5 is {7128 % 5}.")
print(f"f) The remainder of 19224 / 9 is {19224 % 9}.")

# task 08
big_pizza_total = 4 * 274
medium_pizza_total = 2 * 218
juice_total = 4 * 35
cake_total = 1 * 350
water_total = 3 * 21
birthday_order_total = (
    big_pizza_total
    + medium_pizza_total
    + juice_total
    + cake_total
    + water_total
)

print("\nTask 08")
print(f"Irynka needs {birthday_order_total} UAH for the whole order.")

# task 09
photos = 232
photos_per_page = 8
album_pages = photos // photos_per_page

print("\nTask 09")
print(f"Ihor needs {album_pages} album pages.")

# task 10
distance_km = 1_600
fuel_per_100_km = 9
tank_capacity = 48

fuel_needed = distance_km // 100 * fuel_per_100_km
refuel_stops = (fuel_needed - tank_capacity) // tank_capacity

print("\nTask 10")
print(f"The family needs {fuel_needed} liters of fuel.")
print(f"The family needs to visit a gas station at least {refuel_stops} times.")
