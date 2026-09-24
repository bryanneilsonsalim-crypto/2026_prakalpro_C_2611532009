# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if 
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_2009
# Program ini menggunakan fungsi input()
# Program menghitung diskon belanja

# Input dari user
total_belanja_2009 = float(input("Masukkan total belanja(Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau "ya")
input_member_2009 = input("Apakah Anda member? (y/t): ")
is_member_2009 = input_member_2009 in ["y", "ya"]

#Input status kode promo (mengecek apakah user mengetik 'y' atau "ya")
input_promo_2009 = input("Apakah kode promo valid (y/t): ") .strip().lower()
kode_promo_valid_2009 = input_promo_2009 in ['y',"ya"]

total_diskon_persen_2009 = 0

# Multi-If terpisah: Setiap kondisi diperiksa secara independen 
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2009 > 1000000:
    total_diskon_persen_2009 += 10 # Diskon belanja besar

if is_member_2009:
    total_diskon_persen_2009 += 5 # Diskon member

if kode_promo_valid_2009:
    total_diskon_persen_2009 += 15 # Diskon voucher
    
# Menghitung nominal diskon dan total  bayar
nominal_diskon_2009 = total_belanja_2009*(total_diskon_persen_2009 / 100)
total_bayar_2009 = total_belanja_2009 - nominal_diskon_2009

# Output hasil
print("\n --- Rincian Pembayaran---")
print(f"Total Diskon : {total_diskon_persen_2009}% (Rp {nominal_diskon_2009 :,.0f})")
print(f"Total Bayar : Rp {total_bayar_2009 :,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_2009}%")
#Output : Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid