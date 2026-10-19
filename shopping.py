def calculate_total(price, quantity, discount):
    subtotal = price * quantity
    total = subtotal - discount
    return total

print(calculate_total(2500, 3, 500))
print(calculate_total(1000, 5, 200))
print(calculate_total(5000, 2, 0))