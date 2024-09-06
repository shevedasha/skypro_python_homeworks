
def month_to_season(mon):
    if mon in [12,1,2]:
        return "Winter"
    elif mon in [3,4,5]:
        return "Spring"
    elif mon in [6,7,8]:
        return "Summer"
    elif mon in [9,10,11]:
        return "Autumn"
    else:
        return "Такого месяца не существует"
print(month_to_season(6))


    

        