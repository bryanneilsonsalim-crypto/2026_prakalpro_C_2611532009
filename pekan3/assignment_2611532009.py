# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_2009 = int(input("Input angka-1: "))
angka2_2009 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =",angka1_2009)
print("Nilai angka2 =",angka2_2009)

# Assigment biasa
hasil_2009 = angka1_2009 
print("\nAssigment biasa (=)")
print("Hasil =",hasil_2009)

# Assigment penambahan
hasil_2009 = angka1_2009 
hasil_2009 += angka2_2009
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_2009)

# Assigment pengurangan
hasil_2009= angka1_2009 
hasil_2009 -= angka2_2009 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_2009)

# Assigment perkalian
hasil_2009 = angka1_2009 
hasil_2009 *= angka2_2009
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_2009)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_2009 != 0:
    hasil_2009 = angka1_2009
    hasil_2009/= angka2_2009
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_2009)
    # Operator tambahan
    hasil_2009 = angka1_2009 
    hasil_2009 //= angka2_2009
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_2009)
    hasil_2009 = angka1_2009 
    hasil_2009 %= angka2_2009
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_2009)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_2009 = angka1_2009 
hasil_2009 **= angka2_2009
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_2009)