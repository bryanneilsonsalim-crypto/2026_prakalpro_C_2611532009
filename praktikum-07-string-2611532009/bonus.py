kalimat = input("Masukkan kalimat: ")
teks_bersih = kalimat.lower().replace(" ", "")

if teks_bersih == teks_bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")