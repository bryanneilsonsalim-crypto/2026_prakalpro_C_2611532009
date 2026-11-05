total = 0

while True:
    user_input = input("Enter a number: ")
    number = int(user_input)
    
    if number < 0:
        break
        
    if number == 0:
        continue
        
    print(f"Positive number: {number}")
    total += number

print(f"Total: {total}")