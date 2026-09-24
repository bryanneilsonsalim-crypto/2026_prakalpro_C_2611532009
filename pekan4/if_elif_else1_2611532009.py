# Buat file dengan nama if_elif_else_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2009 =  int(input("Input umur Anda: "))
sim_2009 = input("Apaakh Anda sudah punya SIM C: ")[0]

if umur_2009 >= 17 and sim_2009 == 'y':
    print("Anda Sudah Dewasa dan Boleh Membawa Motor")

elif umur_2009>= 17 and sim_2009 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh membawa motor")
    
elif umur_2009< 17 and sim_2009 == 'y':
    print("Anda Belum cukup umur punya SIM")

else:
    print("Anda Belum Cukup umur dan tidak boleh bawa motor")

print("Program Selesai")