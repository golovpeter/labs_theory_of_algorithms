# Сумма нечетных чисел из числа

# Ввод числа
input_num = input("Введите число: ")
# Сумма нечетных чисел
odd_sum = 0

for el in input_num:
    if int(el) % 2 != 0:  # Проверка цифры на четность
        odd_sum += int(el)

print(odd_sum)
