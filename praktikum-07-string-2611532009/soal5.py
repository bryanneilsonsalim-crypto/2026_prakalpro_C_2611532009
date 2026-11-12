# Name: Bryan Neilson Salim
# NIM: 2611532009
# Question 5


username = input("Username: ")

# Check the rules in a safe order and print the first rule that fails.
# Message:
# "Invalid: at least 5 characters"
# "Invalid: letters and digits only"
# "Invalid: must start with a letter"
# "Valid"

#Part A
if len(username)<=5:
    print("Invalid: at least 5 characters")
    
elif not username.isalpha() and not username.isdigit():
    print("Invalid: letters and digits only")
    
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("valid")
    

#Part B
nim = input("NIM: ")

if not nim.isdigit():
    print("Invalid: NIM must a digit only")
    
elif len(nim) != 10:
    print("Invalid NIM")
else:
    print("Valid","intake year 20" + nim[:2] )
    print(nim[:9])
    print(nim[:9] + "A")