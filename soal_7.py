menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    daily_sales = []
    for menu in menus:
        qty = int(input(f"Day {day}, {menu}: "))
        daily_sales.append(qty)
    sales.append(daily_sales)

for i in range(number_of_days):
    total_day = 0
    for j in range(len(menus)):
        total_day += sales[i][j]
    print(f"Day {i + 1}: {total_day}")

menu_totals = []
for j in range(len(menus)):
    total_menu = 0
    for i in range(number_of_days):
        total_menu += sales[i][j]
    menu_totals.append((menus[j], total_menu))

print(f"Total per menu: {menu_totals}")

best_menu = ""
max_total = -1

for name, total in menu_totals:
    if total > max_total:
        max_total = total
        best_menu = name

print(f"Best seller: {best_menu} ({max_total})")
     