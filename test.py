import numpy


def game():
    input_el = input("Выберите: ")

    list_el = ["К", "Н", "Б"]

    if input_el not in list_el:
        print("Неверный ввод")
        return

    compt = numpy.random.choice(list_el)
    print("Компьютер выбрал:", compt)

    if input_el == compt:
        print("Ничья")
        return

    if (input_el == "К" and compt == "Н") or \
            (input_el == "Н" and compt == "Б") or \
            (input_el == "Б" and compt == "К"):

        print("Вы выиграли")
    else:
        print("Вы проиграли")

    return


if __name__ == "__main__":
    game()
