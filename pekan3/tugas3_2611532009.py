print("=== SISTEM TRANSAKSI TOKO ===")
print(" ")
nama_2009 = input("Masukkan Nama Pelanggan : ")
status_2009 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_2009 = int(input("Masukkan Total Belanja : "))
jumlah_2009 = int(input("Masukkan Jumlah Barang : "))
promo_2009 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_2009}")
print(f"Status Pelanggan     : {status_2009}")
print(f"Total Belanja        : Rp{total_2009}")
print(f"Jumlah Barang        : {jumlah_2009}")
print(f"Kode Promo           : {promo_2009}")

kode_promo_2009 = ["HEMAT10", "HEMAT20", "SAKITPERUT", "RRQEVOSSAHABATAN"] #list kode promo

syarat_total_2009 = total_2009 >= 200000 # apakah memenuhi syarat belanja
syarat_jumlah_2009 = jumlah_2009 >= 3 # apakah memenuhi syarat barang
status_valid_2009 = status_2009 == "member" # apakah user member
promo_valid_2009 = promo_2009 in kode_promo_2009 # apakah kode promo ada dalam list

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_total_2009}")
print(f"Jumlah Barang >= 3         : {syarat_jumlah_2009}")
print(f"Status Member              : {status_valid_2009}")
print(f"Kode Promo Tersedia        : {promo_valid_2009}")
print(f"Mendapatkan Diskon         : {syarat_jumlah_2009 or syarat_total_2009}")
print(f"Mendapatkan Promo          : {promo_valid_2009}")

diskon_2009 = 0.05

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                      : Rp{diskon_2009 * total_2009}")
print(f"Total Pembayaran            : Rp{total_2009 - total_2009 * diskon_2009}")
print(f"Rata-rata Harga Barang      : Rp{(total_2009 - total_2009 * diskon_2009)/jumlah_2009}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : ...")
print(f"Member Access               : {status_valid_2009}")
print(f"Promo Access                : {promo_valid_2009}")
print(f"Free Shipping Access        : ...")

kode_transaksi_2009 = int(status_valid_2009) << 0 | int(syarat_total_2009) << 1 | int(syarat_jumlah_2009) << 2 | int(promo_valid_2009) << 3
kode_referensi_2009 = int(status_valid_2009) << 0 | int(syarat_total_2009) << 1 | int(promo_valid_2009) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{format(int(status_valid_2009) << 0,"04b")} | {format(int(syarat_total_2009) << 1,"04b")} | {format(int(syarat_jumlah_2009) << 2,"04b")} | {format(int(promo_valid_2009) << 3,"04b")}")
print(f"Kode Biner   : {format(kode_transaksi_2009,"04b")}")
print(f"Kode Desimal : {kode_transaksi_2009}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_transaksi_2009,"04b")} & {format(int(status_valid_2009) << 0,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_2009) & int(status_valid_2009) << 0,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_2009) & int(status_valid_2009) << 0}")

print("Cek Promo")
print(f"{format(kode_transaksi_2009,"04b")} & {format(int(promo_valid_2009) << 3,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_2009) & int(promo_valid_2009) << 3,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_2009) & int(promo_valid_2009) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_transaksi_2009,"04b")}")
print(f"Kode Referensi : {format(kode_referensi_2009,"04b")}")
print(f"{format(kode_transaksi_2009,"04b")} ^ {format(kode_referensi_2009,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_2009) ^ (kode_referensi_2009),"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_2009) ^ (kode_referensi_2009)}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_2009,"04b")} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_2009) << 1,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_2009) << 1}") 
print("=== SELESAI ===")