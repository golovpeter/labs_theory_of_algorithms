inpt = input("Введите число: ")  # Введите число

i = 0  # Индекс

counter = 1  # Сумма цифр в числе

while i < len(inpt):
    counter *= int(inpt[i])

    # Увеличиваем индекс
    i += 1

# Проверка, что произведение цифр в числе меньше или больше 1000000
if counter < 1000000:
    print("Произведение цифр меньше 1000000")
else:
    print("Произведение цифр больше 1000000")
