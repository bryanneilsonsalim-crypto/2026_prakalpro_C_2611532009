# Name: Bryan Neilson Salim
# NIM: 2611532009
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0::11])

#Part B

text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "AaIiUuEeOo":
        count +=1
print("Vowels:", count)
