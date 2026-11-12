# Name: Bryan Neilson Salim
# NIM: 2611532009
# Question 4


phone = "081234567890"
masked = phone[:4] + "*" * (len (phone)-7) + phone[-3:]
print(masked)