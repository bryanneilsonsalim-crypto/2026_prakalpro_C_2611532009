# Buat file dengan nama nested_for2_NIM.p
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2009 = int(input("Masukkan nilai batas: "))
for i_2009 in range(1, batas_2009+1):
    for j_2009 in range(1, batas_2009+1):
        print("*", end=" ")
    print() # pindah ke baris berikutnya