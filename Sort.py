# sortByTypeOfKitchen
# European
# Seafood
# Italian
# American
# Asian
# Irish
# Georgian
# Russian
# None
# Street food
# French


def sortByTypeOfKitchen(choice, restaurants):
    newRestaurans = []
    for rest in restaurants:
        if rest[1] == "European" and choice == 1:
            newRestaurans.append(rest)
        if rest[1] == "Seafood" and choice == 2:
            newRestaurans.append(rest)
        if rest[1] == "Italian" and choice == 3:
            newRestaurans.append(rest)
        if rest[1] == "American" and choice == 4:
            newRestaurans.append(rest)
        if rest[1] == "Asian" and choice == 5:
            newRestaurans.append(rest)
        if rest[1] == "Irish" and choice == 6:
            newRestaurans.append(rest)
        if rest[1] == "Georgian" and choice == 7:
            newRestaurans.append(rest)
        if rest[1] == "Russian" and choice == 8:
            newRestaurans.append(rest)
        if rest[1] == "Street food" and choice == 9:
            newRestaurans.append(rest)
        if rest[1] == "French" and choice == 10:
            newRestaurans.append(rest)
    return newRestaurans


# sortByAveragePrise
# до 500р
# до 1000р
# до 1500р
# до 2000р
# до 2500р
# дорого-богато

def sortByAveragePrise(choice, restaurants):
    newRestaurans = []
    for rest in restaurants:
        if rest[2] <= 500 and choice == 1:
            newRestaurans.append(rest)
        elif rest[2] <= 1000 and choice == 2:
            newRestaurans.append(rest)
        elif rest[2] <= 1500 and choice == 3:
            newRestaurans.append(rest)
        elif rest[2] <= 2000 and choice == 4:
            newRestaurans.append(rest)
        elif rest[2] <= 2500 and choice == 5:
            newRestaurans.append(rest)
    return newRestaurans


# sortByWorkTime
# утреннее (с 8 до 12)
# дневное (с 13 до 16)
# вечернее (с 17 до 21)
# ночное (с 22 до 3)

def sortByWorkTime(choice, restaurants):
    if choice == 1:  # утреннее время (с 8 до 12)
        time_range = range(8, 13)
    elif choice == 2:  # дневное время (с 13 до 16)
        time_range = range(13, 17)
    elif choice == 3:  # вечернее время (с 17 до 21)
        time_range = range(17, 23)
    elif choice == 4:  # ночное время (с 22 до 3)
        time_range = list(range(23, 24)) + list(range(0, 4))

    newRestaurants = []
    for rest in restaurants:
        working_hours = rest[3]
        start_time, end_time = working_hours.split('-')
        start_hour, _ = start_time.split(':')
        end_hour, _ = end_time.split(':')
        if int(start_hour) in time_range or int(end_hour) in time_range:
            newRestaurants.append(rest)

    return newRestaurants

# sortByStars
# 1 - 1 звезда и выше
# 2 - 2 звезды и выше
# 3 - 3 звезды и выше
# 4 - 4 звезды и выше
# 5 - 5 звезд

def sortByStars(choice, restaurants):
    newRestaurants = []
    for rest in restaurants:
        if int(rest[4]) >= choice:
            newRestaurants.append(rest)
    return newRestaurants


# sortByDelivery
# 1 - да
# 2 - нет


def sortByDelivery(choice, restaurants):
    if choice == 1:
        choice == "yes"
    elif choice == 2:
        choice == "no"
    newRestaurants = []
    for rest in restaurants:
        if rest[5] == choice:
            newRestaurants.append(rest)
    return newRestaurants


# sortByLunch
# 1 - кондитерская
# 2 - ресторан
# 3 - кафе
# 4 - бар
# 5 - магазин выпечки

def sortByType(choice, restaurants):
    newRestaurants = []
    for rest in restaurants:
        if choice == 1:
            if rest[6] == "confectionery":
                newRestaurants.append(rest)
        if choice == 2:
            if rest[6] == "restaurant":
                newRestaurants.append(rest)
        if choice == 3:
            if rest[6] == "cafe":
                newRestaurants.append(rest)
        if choice == 4:
            if rest[6] == "bar":
                newRestaurants.append(rest)
        if choice == 5:
            if rest[6] == "pastry shop":
                newRestaurants.append(rest)
    return newRestaurants


# sortByLunch
# 1 - да
# 2 - нет

def sortByLunch(choice, restaurants):
    if choice == 1:
        choice == "yes"
    elif choice == 2:
        choice == "no"
    newRestaurants = []
    for rest in restaurants:
        if rest[7] == choice:
            newRestaurants.append(rest)
    return newRestaurants


# sortByBreakfast
# 1 - да
# 2 - нет

def sortByBreakfast(choice, restaurants):
    if choice == 1:
        choice == "yes"
    elif choice == 2:
        choice == "no"
    newRestaurants = []
    for rest in restaurants:
        if rest[8] == choice:
            newRestaurants.append(rest)
    return newRestaurants


# sortByChildMenu
# 1 - да
# 2 - нет

def sortByChildMenu(choice, restaurants):
    if choice == 1:
        choice == "yes"
    elif choice == 2:
        choice == "no"
    newRestaurants = []
    for rest in restaurants:
        if rest[9] == choice:
            newRestaurants.append(rest)
    return newRestaurants


# sortByBarMenu
# 1 - да
# 2 - нет

def sortByBarMenu(choice, restaurants):
    if choice == 1:
        choice == "yes"
    elif choice == 2:
        choice == "no"
    newRestaurants = []
    for rest in restaurants:
        if rest[10] == choice:
            newRestaurants.append(rest)
    return newRestaurants



