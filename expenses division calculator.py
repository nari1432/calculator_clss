class EventExpensesCalculator:
    def __init__(self):
        self.expense_items = []

    def add_expense(self, item, cost):
        self.expense_items.append((item, cost))

    def calculate_total_expenses(self):
        total_cost = sum(cost for item, cost in self.expense_items)
        return total_cost

    def divide_total_expenses(self, divisor):
        if divisor != 0:
            return self.calculate_total_expenses() / divisor
        else:
            return "Error: Division by zero is not allowed."

    def expenses(self):
        return self.expense_items

# Example usage
event_calculator = EventExpensesCalculator()

event_calculator.add_expense("food", 30000)
event_calculator.add_expense("decorations", 10000)
event_calculator.add_expense("taxes", 5000)

divisor = 2

result = event_calculator.divide_total_expenses(divisor)

total_expenses = event_calculator.calculate_total_expenses()

expenses_list = event_calculator.expenses()

print(f"Total expenses: {total_expenses}")
for item, cost in expenses_list:
    print(f"{item}: {cost}")

print(f"\nTotal expenses divided by {divisor}: {result}")
