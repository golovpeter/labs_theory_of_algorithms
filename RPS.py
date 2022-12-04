import random


def five_bones_sum():
    return [random.randrange(1, 7) for _ in range(5)]


def game():
    player_sum, comp_sum = 0, 0

    if input("Введите 'с' для начала игры: ") == "с":
        for i in range(1, 4):
            print("----------------------------------------------")
            print(f"Раунд {i}\n")

            player_turn = five_bones_sum()
            comp_turn = five_bones_sum()

            print(f"Игрок выбросил: {player_turn}, сумма: {sum(player_turn)}")
            print(f"Компьютер выбросил: {comp_turn}, сумма: {sum(comp_turn)}")

            if sum(player_turn) > sum(comp_turn):
                player_sum += sum(player_turn)
            elif sum(comp_turn) > sum(player_turn):
                comp_sum += sum(comp_turn)

            print(f"Счёт: \nВы: {player_sum} \nКомпьютер: {comp_sum}")

            if i == 3:
                print("----------------------------------------------")

        if comp_sum > player_sum:
            print("\nКомпьютер победил!")
        else:
            print("\nВы победили!")

    else:
        print('Неверный ввод!')


if __name__ == "__main__":
    game()
