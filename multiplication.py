class EggCalculator:
    def __init__(self):
        self.egg_cartons = []

    def add_carton(self, size, quantity, price_per_dozen):
        self.egg_cartons.append((size, quantity, price_per_dozen))

    def calculate_total_cost(self):
        total_cost = sum((quantity / 12) * price for size, quantity, price in self.egg_cartons)
        return total_cost

    def carton_list(self):
        return self.egg_cartons

egg_calculator = EggCalculator()

egg_calculator.add_carton("Large", 90, 1.5)
egg_calculator.add_carton("Medium", 72, 1.0)
egg_calculator.add_carton("Small", 44, 0.8)

total_cost = egg_calculator.calculate_total_cost()

carton_list = egg_calculator.carton_list()

print(f"Total cost of eggs: ${total_cost:.2f}")
for size, quantity, price_per_dozen in carton_list:
    print(f"{size} eggs: Quantity - {quantity}, Price per dozen - ${price_per_dozen}")
