# Cat years, Dog years

def human_years_cat_years_dog_years(human_years):
    c = 15
    d = 15
    h = 0
    for i in range(human_years):
        h += 1
        c += 4
        d += 5
    if human_years >= 3:
        return [human_years, c +1, d -1]    
    if human_years >= 2:
        return [2,24,24]
    elif human_years >= 1:
        return [1,15,15]