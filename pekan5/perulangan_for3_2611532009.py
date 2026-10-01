# Buat file dengan nama perulangan_for3_2611532009.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2009 = int(input("Masukkan jumlah perulangan: "))

jumlah_2009 = 0
for i_2009 in range(1, ulang_2009+1):
    print(i_2009, end=" ")
    jumlah_2009 += i_2009
    
    if i_2009 < ulang_2009:
        print("+", end=" ")
    else:
        print("=", jumlah_2009, end=" ")
print()
print("Jumlah = ", jumlah_2009)