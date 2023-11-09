class Calculator:
    def __init__(self):
        self.expense_items = []

    def add_expense(self, item, cost):
        self.expense_items.append((item, cost))

    def calculate_total_expenses(self):
        total_cost = sum(cost for item, cost in self.expense_items)
        return total_cost

    def expenses(self):
        return self.expense_items

event_calculator = Calculator()

event_calculator.add_expense("food", 30000)
event_calculator.add_expense("decorations", 10000)
event_calculator.add_expense("taxes", 5000)

total_expenses = event_calculator.calculate_total_expenses()

expenses_list = event_calculator.expenses()

print(f"total expenses: {total_expenses}")
for item, cost in expenses_list:
    print(f"{item}: {cost}")







    