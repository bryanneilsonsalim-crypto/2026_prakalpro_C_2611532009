# Name: Bryan Neilson Salim
# NIM: 2611532009
# Question 7

name = "bryan neilson salim"  
nim = "2611532009"   


nama_depan = name.split()[0]
username = nama_depan + nim[-3:]


intake = "20" + nim[:2]

lebar = 30
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * lebar)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * lebar)

