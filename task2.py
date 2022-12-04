# Сумма нечетных чисел из числа

input_num = input("Введите число: ")
odd_sum = 0

for el in input_num:
    if int(el) % 2 != 0:
        odd_sum += int(el)

print(odd_sum)
