d = 9  # change to the last digit of your NIM
daily_limit = 30000 + d * 1000
expenses = []
# Write your code below
for i in range (1,8):
    daily_expenses = int(input(f"Day {i}: "))
    expenses.append(daily_expenses)
total = 0
highest = expenses[0]
day_above_limit = 0
for expens in expenses:
    total += expens
averange = total / len(expenses)
for i in range (len(expenses)):
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i+1
for expens in expenses:
    if expens > daily_limit:
        day_above_limit += 1
print("Day Limit: ", daily_limit)
print("Total: ", total)
print(f"Averange: {averange:.1f}")
print("Highest: ", "Day", highest_day, "(",highest,")")
print("Day above limit: ", day_above_limit)
            
