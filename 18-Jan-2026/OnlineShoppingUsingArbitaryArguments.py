def calculate_bill(**kwargs):
    item_cost = kwargs["item_cost"]
    quantity = kwargs["quantity"]

    tax = kwargs.get("tax", 0.05)
    discount = kwargs.get("discount", 0)

    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total


calc_bill = calculate_bill(item_cost=100, quantity=5)
print("calc_bill1", calc_bill)

calc_bill2 = calculate_bill(item_cost=200, quantity=1, tax=0.10, discount=10)
print("calc_bill1", calc_bill2)
