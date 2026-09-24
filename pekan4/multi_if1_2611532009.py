# Buat file dengan nama multi_if1_NIM.py
# Buat program untuk kondisioanl if 
# Nama variabel ditambah 4 digit NIM terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2009 = int(input("Input umur anda: "))
sim_2009 = input("Apakah Anda Sudah Punya SIM C(y/t): ")[0]

if umur_2009 >= 17 and sim_2009 == 'y':
    print("Anda Sudah Dewasa dan Boleh Membawa Motor")

if umur_2009 >= 17 and sim_2009 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh membawa motor")
    
if umur_2009 < 17 and sim_2009 == 'y':
    print("Anda Belum cukup umur punya SIM")

if umur_2009 < 17 and sim_2009 != 'y':
    print("Anda Belum Cukup Umur bawa motor")
    