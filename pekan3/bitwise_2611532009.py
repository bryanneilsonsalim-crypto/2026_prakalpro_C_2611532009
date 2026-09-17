# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_2009 = int(input("Masukkan angka bitwise-1: "))
angka2_2009 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_2009,"| biner =",bin(angka1_2009))
print("angka1 =",angka2_2009,"| biner =",bin(angka2_2009))

# Bitwise AND
hasil_2009 = angka1_2009 & angka2_2009
print("\nBitwise AND (&)")
print(angka1_2009,"&",angka2_2009,hasil_2009)
print("Biner hasil =",bin(hasil_2009))
print("Biner hasil (8 bit) =",format(hasil_2009,"08b"))

# Bitwise OR
hasil_2009 = angka1_2009 | angka2_2009
print("\nBitwise OR (|)")
print(angka1_2009,"|",angka2_2009,hasil_2009)
print("Biner hasil =",bin(hasil_2009))
print("Biner hasil (8 bit) =",format(hasil_2009,"08b"))

# Bitwise XOR
hasil_2009 = angka1_2009 ^ angka2_2009
print("\nBitwise XOR (^)")
print(angka1_2009,"^",angka2_2009,hasil_2009)
print("Biner hasil =",bin(hasil_2009))
print("Biner hasil (8 bit) =",format(hasil_2009,"08b"))

# Bitwise NOT
hasil_2009 = ~angka1_2009
print("\nBitwise NOT (~)")
print(angka1_2009,"~",angka2_2009,hasil_2009)
print("Biner hasil =",bin(hasil_2009))
print("Biner hasil (8 bit) =",format(hasil_2009,"08b"))

# Bitwise geser kiri
jumlah_geser_2009 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2009 = angka1_2009 << jumlah_geser_2009
print("\nBitwise geser kiri (<<)")
print(angka1_2009,"<<",jumlah_geser_2009,"=",hasil_2009)
print("Biner hasil =",bin(hasil_2009))
print("Biner hasil (8 bit) =",format(hasil_2009,"08b"))

# Bitwise geser kanan
hasil_2009 = angka1_2009 >> jumlah_geser_2009
print("\nBitwise geser kiri (>>)")
print(angka1_2009,">>",jumlah_geser_2009,"=",hasil_2009)
print("Biner hasil =",bin(hasil_2009))
print("Biner hasil (8 bit) =",format(hasil_2009,"08b"))