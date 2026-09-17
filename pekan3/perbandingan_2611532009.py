# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2009 = int(input("Input angka-1: "))
angka2_2009 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2009 = angka1_2009 > angka2_2009
print("\nOperator lebih besar dari")
print("angka1 > angka2 =",hasil_2009)

# Lebih kecil dari
hasil_2009 = angka1_2009 < angka2_2009
print("\nOperator lebih kecil dari")
print("angka1 < angka2 =",hasil_2009)

# Lebih besar dari atau sama dengan
hasil_2009 = angka1_2009 >= angka2_2009
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =",hasil_2009)

# Lebih kecil dari atau sama dengan
hasil_2009 = angka1_2009 <= angka2_2009
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =",hasil_2009)

# Sama dengan
hasil_2009 = angka1_2009 == angka2_2009
print("\nOperator sama dengan")
print("angka1 == angka2 =",hasil_2009)

# Tidak sama dengan
hasil_2009 = angka1_2009 != angka2_2009
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =",hasil_2009)

# Tambahan: perbandingan berantai dalam Python
hasil_2009 = 0 < angka1_2009 < 100
print("\nPerbandingan berantai")
print("0 < angka1_2009 < 100 =",hasil_2009)

hasil_2009 = 0 < angka2_2009 < 100
print("0 < angka2_2009 < 100 =",hasil_2009)