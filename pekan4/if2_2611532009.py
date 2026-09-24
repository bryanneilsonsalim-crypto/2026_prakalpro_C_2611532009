# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if 
# Nama variabel ditambah dengan 4 digit NIM terakhir contoh: ipk_1234
#  Program ini menggunakan fungsi input()

ipk_2009 = float(input("Input IPK Anda = "))

if ipk_2009>2.75:
    print("Anda Lulus dengan Sangat Memuaskan IPK " + str(ipk_2009))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")