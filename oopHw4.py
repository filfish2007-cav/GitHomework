import datetime


class Recipe:
    def __init__(self, name: str, ingredients: list[str], text: str, cook_time: int):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = datetime.timedelta(minutes=cook_time)

    def __str__(self):
        return f"Dish: {self.name}"

    def __contains__(self, item: str):
        return item.lower() in self.ingredients

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print(f"Name of a dish: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"How to cook?: {self.text}")
        print(f"Time to cook: {self.time}")
        print()


pizza = Recipe(
    "Піца",
    ["борошно", "вода", "дріжджі", "томат", "сир"],
    "Готуємо тісто, додаємо інгредієнти та запікаємо",
    30,
)

salad = Recipe(
    "Салат",
    ["томат", "огірок", "зелень", "олія"],
    "Нарізаємо овочі, додаємо зелень та поливаємо олією",
    10,
)

soup = Recipe(
    "Суп",
    ["вода", "картопля", "морква", "м'ясо"],
    "Варимо всі інгредієнти до готовності",
    45,
)

dishes = [pizza, salad, soup]

for dish in dishes:
    if "томат" in dish:
        print(dish, "has a tomato in it")
        print()

print("The least time to cook: ")
print()
min(dishes).display_info()
