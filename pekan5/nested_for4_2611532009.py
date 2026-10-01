# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2009 = int(input("Masukkan tinggi pola( bilangan genap, misal 10): "))

if tinggi_2009 % 2 == 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2009 = tinggi_2009
    c_2009 = a_2009
    lebar_2009 = (2*tinggi_2009)-2
    
    for i_2009 in range(1, tinggi_2009+1):
        b_2009 = c_2009 + 1
        
        for j_2009 in range(1, lebar_2009+1):
            
            # Baris atas dan bawah
            if i_2009 == 1 or i_2009 == tinggi_2009:
                if j_2009 == 1 or j_2009 == lebar_2009:
                    print("#", end="")
                else:
                    print("=", end="")
                    
            # Baris isi
            else:
                if j_2009 == 1 or j_2009 == lebar_2009:
                    print("|", end="")
                else:
                    if j_2009 == c_2009:
                        print("<", end="")
                    elif j_2009 == b_2009:
                        print(">", end="")
                    elif j_2009 == (lebar_2009 - c_2009):
                        print("<", end="")
                    elif j_2009 == (lebar_2009 - c_2009 + 1) or j_2009 == (lebar_2009 - b_2009 + 1):
                        print(">", end="")
                    elif j_2009 > b_2009 and j_2009 < (lebar_2009 - c_2009):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()
        
        # Logika asli Java
        a_2009 -= 2
        
        if a_2009 <= 0:
            c_2009 = (-a_2009) + 2
        else:
            c_2009 = a_2009