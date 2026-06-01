# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
   print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4

# task 05 == виправте назви змінних
storona1 = 1
storona2 = 2
storona3 = 3
storona4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona1 + storona2 + storona3 + storona4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple = 4
pear = apple + 5
plum = apple - 2

trees = apple + plum + pear

print("Усього дерев в саду:", trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_morning = 5
temperature_afternoon = temperature_morning - 10
temperature_evening  = temperature_afternoon + 4
if temperature_evening == 1 or temperature_evening == -1:
    print("Температура надвечір =", temperature_evening, "градус")

elif temperature_evening == 2 or temperature_evening == 3 or temperature_evening == 4:
    print("Температура надвечір =", temperature_evening, "градуси")

else:
    print("Температура надвечір =", temperature_evening, "градусів")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
children = (boys - 1) + (girls - 2)
print("Сьогодні",children, "дітей у театральному гуртку")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book1 = 8
book2 = book1 + 2
book3 = (book1 + book2) / 2
print("Разом книги коштують", book1+book2+book3, "грн")