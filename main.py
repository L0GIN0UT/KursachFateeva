import time
from Menu import *
from Generate import *
from Sort import *


def show_all(restaurants):
    for rest in restaurants:
        print()
        print("Наименование: " + str(rest[0]))
        print("Кухня: " + str(rest[1]))
        print("Средний чек: " + str(rest[2]))
        print("Время работы: " + str(rest[3]))
        print("Оценка: " + str(rest[4]))
        print("Доставка: " + str(rest[5]))
        print("Тип заведения: " + str(rest[6]))
        print("Бизнес-ланч: " + str(rest[7]))
        print("Завтрак: " + str(rest[8]))
        print("Детское меню: " + str(rest[9]))
        print("Барное: " + str(rest[10]))
        print()


def choice_of_person(choice, rest):
    print()
    if choice == 1:
        menuForTypeOfKitchen()
        time_freeze()
        rest = sortByTypeOfKitchen(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 2:
        menuForAveragePrise()
        time_freeze()
        rest = sortByAveragePrise(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 3:
        menuForWorkTime()
        time_freeze()
        rest = sortByWorkTime(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 4:
        menuForStars()
        time_freeze()
        rest = sortByStars(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 5:
        menuForDelivery()
        time_freeze()
        rest = sortByDelivery(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 6:
        menuForType()
        time_freeze()
        rest = sortByType(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 7:
        menuForLunch()
        time_freeze()
        rest = sortByLunch(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 8:
        menuForBreakfast()
        time_freeze()
        rest = sortByBreakfast(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 9:
        menuForChild()
        time_freeze()
        rest = sortByChildMenu(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 10:
        menuForBar()
        time_freeze()
        rest = sortByBarMenu(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 11:
        rest = Restart()
        print("Характеристики были сброшены")
        time_freeze()
        return rest
    elif choice == 12:
        time_freeze()
        if check_res(rest):
            show_all(rest)
    elif choice == 13:
        exit()


def check_input():
    while True:
        a = input("Введите ваш ответ -> ")
        if a.isdigit():
            return int(a)


def check_res(rest):
    if len(rest) == 0:
        print()
        print("Приносим свои извинения")
        print("Но на данный момент в нашем приложении")
        print("Нет ресторанов подходящих вашим предпочтениям")
        print("Попробуйте сбросить характеристики и выбрать другие критерии")
        print()
        time.sleep(2)
    else:
        return rest


def main(gen_rest):
    print("Добро пожаловать в программу для подбора ресторанов")
    rest = gen_rest
    while True:
        time_freeze()
        print()
        menu()
        rest = choice_of_person(check_input(), rest)


def time_freeze():
    time.sleep(1)


res = Restart()
main(res)
