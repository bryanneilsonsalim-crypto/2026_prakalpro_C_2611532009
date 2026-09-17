from typing import Final

#Menentukan Konstanta
batas_nilai_2009 : Final = 75.0

#Penggunaan Multistring 
alamat_2009 = """
Jl. Kampus Unand
Kecamatan Pauh,
Kota Padang
"""
# Tipe data Complex
token_sinyal_2009 = 100 + 3j

print("=== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 ===")
Nama_2009 = input("Masukkan Nama Mahasiswa: ")
Jenis_Kelamin_2009 = input('L/P: ')
Umur_2009 = int(input("Masukkan Umur: "))
Skor_tes_awal_2009 = float(input("Masukkan Skor Tes Awal: "))



hasil_kelulusan_2009 = Skor_tes_awal_2009 >= batas_nilai_2009

print('')
print("=== DATA PRAKTIKAN & HASIL PEMRIKSAAN === ")
print(f"Nama Mahasiswa: {Nama_2009} | Tipe: {type(Nama_2009)}")                                                  
print(f"Jenis Kelamin: {Jenis_Kelamin_2009} | Tipe: { type(Jenis_Kelamin_2009)}")
print(f"Alamat Domisili: {alamat_2009} | Tipe {type(alamat_2009)}")
print(f"Umur: {Umur_2009} | Tipe: {type(Umur_2009)}")
print(f"Skor Tes Awal: {Skor_tes_awal_2009} | Tipe: {type(Skor_tes_awal_2009)}")
print(f"ID Token Sinyal: {token_sinyal_2009} | Tipe: {type(token_sinyal_2009)}")

print('')
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimun Nilai: {batas_nilai_2009} | Tipe: {type(batas_nilai_2009)}")
print(f"Apakah Dinyatakan lulus? {hasil_kelulusan_2009} | Tipe: {type(hasil_kelulusan_2009)}")


