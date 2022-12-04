def getType():
    first_question = input("Вы пьете молоко? ")

    if str.lower(first_question) == "да":
        second_question = input("Вы едите мясо? ")
        
        if str.lower(second_question) == "да":
            third_question = input("Вы едите траву? ")

            if str.lower(third_question) == "да":
                print("Вы всеядное")
                return
            elif str.lower(third_question) == "нет":
                print("Вы хищник")
                return
            else:
                print("Неверный ввод")
                return

        elif str.lower(second_question) == "нет":
            print("Вы травоядное")
            return
        else:
            print("Неверный ввод")
            return
    
    elif str.lower(first_question) == "нет" :
        print("Вы насекомое")
        return
    else:
        print("Неверный ввод")
        return
    

if __name__ == "__main__":
    getType()