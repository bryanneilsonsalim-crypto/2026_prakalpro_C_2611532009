# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2009 = int(input("Masukkan nilai batas: "))

jumlah_2009 = 0
for i_2009 in range(1, ulang_2009+1):
    if i_2009 % 2 == 0:
        print(i_2009, end=" ")
        jumlah_2009 += i_2009

print()
print("Jumlah =", jumlah_2009)