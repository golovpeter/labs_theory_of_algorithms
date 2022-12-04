import os

alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У",
            "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]


# Функция для вывода меню
def print_menu():
    while True:
        os.system("clear")
        print("1.Закодировать\n2.Декодировать\n3.Выход")

        inpt = input(">>> ")

        if inpt == "1":
            encode()
        elif inpt == "2":
            decode()
        elif inpt == "3":
            break
        else:
            continue


# Функция для кодирования сообщения
def encode():
    input_letters = input("Введите символы: ")
    machine_code = []

    # Проходимся по строке, ищем ее в алфавите и индекс буквы добавляем в код
    for i in range(len(input_letters)):
        if input_letters[i].upper() in alphabet:
            machine_code.append(str(alphabet.index(input_letters[i].upper()) + 1))
        elif input_letters[i] == " ":
            machine_code.append(" ")

    # Вывод закодированного сообщения на экран
    print(" ".join(machine_code))
    input()


# Функция для декодирования сообщения
def decode():
    input_numbers = input("Введите код: ")
    result = ""

    # Разделяем строку по пробелам
    splt = input_numbers.split(" ")

    # Проходимся по массиву и добавляем к результирующей строке буквы по индексу
    for el in splt:
        if el == '':
            del splt[splt.index(el) + 1]
            result += " "
            continue

        # Проверка значений массива на то, являются ли они числом
        try:
            int(el)
        except ValueError:
            print("\nВведен некорректный код! Повторите ввод!")
            break

        # Проверка на то, что числа в массиве находятся в нужном диапазоне
        if int(el) > 33 or int(el) < 1:
            print("\nВведены некорректные значения! Повторите ввод!")
            break

        result += alphabet[int(el) - 1].lower()

    print(result)
    input()


if __name__ == "__main__":
    alphabet.reverse()
    print_menu()
