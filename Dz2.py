class Pizza:
    def __init__(self, size="medium", cheese=True, pepperoni=False, mushrooms=False,onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        ingredients = ", ".join([ing for ing, val in self.__dict__.items() if ing != "size" and val])
        return f"Pizza ({self.size}): {ingredients}"

class PizzaBuilder:
    def __init__(self, size="medium"):
        self.pizza = Pizza(size=size)

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def get_pizza(self):
        return self.pizza

class PizzaDirector:
    def make_pizza(self, builder: PizzaBuilder):
        builder.add_cheese()
        return builder.get_pizza()

director = PizzaDirector()
builder = PizzaBuilder(size="small")
pizza1 = director.make_pizza(builder)
print(pizza1)

builder = PizzaBuilder("medium").add_bacon()
pizza2 = builder.get_pizza()
print(pizza2)

builder = PizzaBuilder("large")
builder.add_pepperoni().add_mushrooms().add_onions()
pizza3 = builder.get_pizza()
print(pizza3)