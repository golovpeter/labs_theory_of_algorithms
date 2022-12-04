import os
import random


# Написать комментарии

# Печать игрового поля
def print_field(game_field):
    os.system("clear")

    print("┌───┬───┬───┐")

    for i in range(0, len(game_field), 3):
        print("│", game_field[i], "│", game_field[i + 1], "│", game_field[i + 2], "│")

        if i != 6:
            print("├───┼───┼───┤")
        else:
            print("└───┴───┴───┘")


# Проверка на окончание игры
def check_the_win(game_field):
    # Список со списками возможных победных вариаций
    solution = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                (1, 4, 7), (2, 5, 8), (3, 6, 9),
                (1, 5, 9), (3, 5, 7))

    # Цикл, который проходится по списку solution, проверяя на совпадения 3 элемента из списка el
    for el in solution:
        if (game_field[el[0] - 1] == game_field[el[1] - 1] != ' ') and \
                (game_field[el[1] - 1] == game_field[el[2] - 1] != ' ') and \
                (game_field[el[0] - 1] == game_field[el[2] - 1] != ' '):
            return 'Игра закончена!'


# Основная игровая функция
def game():
    # Список игрового поля
    game_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Список возможных значений для ввода
    possible_values = game_field.copy()

    # Список свободных значений для выбора
    free_squares = game_field.copy()

    # Словарь для проверки ничьи
    inputs = {
        'X': 0,
        'O': 0
    }

    # Основной игровой цикл
    while True:
        print_field(game_field)

        player_input = input("\nВыберите клетку: ")

        # Проверка значения на корректность
        try:
            int(player_input)
        except ValueError:
            print("\n", "Введено неверное значение! Попробуйте снова")
            continue

        # Проверка введенного значения на то, есть ли он в списке возможных значений
        if int(player_input) not in possible_values or (int(player_input) > 9 and player_input < 1):
            print("\n", "Введено неверное значение! Попробуйте снова")
            input()
            continue

        # Проверка введенного значения на то, есть ли он в списке свободных значений
        if int(player_input) not in free_squares:
            print("\n", "Клетка уже занята!")
            input()
            continue

        # Изменение игрового поля
        game_field[int(player_input) - 1] = "X"
        inputs['X'] += 1
        free_squares.remove(int(player_input))

        if inputs["X"] + inputs["O"] == 9:
            print_field(game_field)
            print("\n", "Ничья!")
            break

        # Проверка на окончание игры
        check_win = check_the_win(game_field)
        if check_win is not None:
            print_field(game_field)
            print("\n", check_win)
            break

        # Рандомный выбор компьютера из свободных значений
        comp_input = random.choice(free_squares)

        # Изменение игрового поля
        game_field[comp_input - 1] = "O"
        inputs['O'] += 1
        free_squares.remove(int(comp_input))

        # Проверка на окончание игры
        check_win = check_the_win(game_field)
        if check_win is not None:
            print_field(game_field)
            print("\n", check_win)
            break


if __name__ == '__main__':
    game()
