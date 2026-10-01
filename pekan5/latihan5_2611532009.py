# Buat file dengan nama latihan5_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2009 = int(input("Masukkan tinggi segitiga: "))

for baris_2009 in range(1, tinggi_2009 + 1):
    # cetak spasi di kiri
    for spasi_2009 in range(tinggi_2009 - baris_2009):
        print(" ", end="")
    # cetak bintang
    for bintang_2009 in range(baris_2009):
        print("*", end=" ")
    # pindah ke baris baru
    print()