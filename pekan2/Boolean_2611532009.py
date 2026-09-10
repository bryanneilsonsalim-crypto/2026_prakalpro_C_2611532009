# Buat file dengan nama Boolean_NIM.py
# Nama variable ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean 
is_lulus = True
is_cumlaude = True

# Menggunakan Boolean
nilai_2009 = 85
batas_lulus_2009 = 75

# Menemtukan nilai Boolean dari kondisi
status_kelulusan_2009 = nilai_2009 >= batas_lulus_2009 # Hasilnya akan True

print( "===Check Kelulusan===")
print("Nilai:", nilai_2009)
print("Apakah Lulus?:", status_kelulusan_2009)
if is_lulus and is_cumlaude :
    print("Selamat, Anda lulus dengan predikat Cum laude!")
    