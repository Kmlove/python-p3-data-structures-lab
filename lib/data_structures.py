spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    food_names = [food["name"] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    pass
    spiciest = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    pass
    for i in range(len(spicy_foods)):
        food = spicy_foods[i]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for i in range(len(spicy_foods)):
        food = spicy_foods[i]
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    pass
    # for i in range(len(spicy_foods)):
    #     food = spicy_foods[i]
    #     if food["heat_level"] > 5:
    #         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

    spicy = [food for food in spicy_foods if food['heat_level'] > 5]
    for food in spicy:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
  

def get_average_heat_level(spicy_foods):
    pass
    total = 0

    # Solution 1:
    # heat = [food["heat_level"] for food in spicy_foods]
    # for num in heat:
    #     total += num

    # Solution 2:
    for i in range(len(spicy_foods)):
        food = spicy_foods[i]
        total += food["heat_level"]

    average = total/len(spicy_foods)
    return int(average)
    

def create_spicy_food(spicy_foods, spicy_food):
    pass
    # new_list = spicy_foods[:]
    # new_list.append(spicy_food)
    # return new_list
    spicy_foods.append(spicy_food)
    return spicy_foods