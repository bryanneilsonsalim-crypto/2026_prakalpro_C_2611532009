print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_2009 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Membuat garis atas
print("#", end="")

for j_2009 in range(4 * n_2009 + 5):
    print("=", end="")

print("#")

# Fase 1: Jam pasir atas (baris N turun sampai 1)
for baris_2009 in range(n_2009, 0, -1):

    # Garis tegak kiri dan satu spasi padding
    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_2009 in range(2 * (n_2009 - baris_2009)):
        print(" ", end="")

    # Angka menurun
    for angka_2009 in range(baris_2009, 0, -1):
        print(angka_2009, end=" ")

    # Poros kristal tengah
    print("<*>", end="")

    # Angka menaik (diawali spasi)
    for angka_2009 in range(1, baris_2009 + 1):
        print(" " + str(angka_2009), end="")

    # Spasi penyeimbang kanan
    for spasi_2009 in range(2 * (n_2009 - baris_2009)):
        print(" ", end="")

    # Satu spasi padding dan garis tegak kanan
    print(" |")

# Fase 2: Poros titik pusat
print("|", end="")

for spasi_2009 in range(2 * n_2009 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_2009 in range(2 * n_2009 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bawah (baris 1 naik sampai N)
for baris_2009 in range(1, n_2009 + 1):

    # Garis tegak kiri dan satu spasi padding
    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_2009 in range(2 * (n_2009 - baris_2009)):
        print(" ", end="")

    # Angka menurun
    for angka_2009 in range(baris_2009, 0, -1):
        print(angka_2009, end=" ")

    # Poros kristal tengah
    print("<*>", end="")

    # Angka menaik (diawali spasi)
    for angka_2009 in range(1, baris_2009 + 1):
        print(" " + str(angka_2009), end="")

    # Spasi penyeimbang kanan
    for spasi_2009 in range(2 * (n_2009 - baris_2009)):
        print(" ", end="")

    # Satu spasi padding dan garis tegak kanan
    print(" |")

# Membuat garis bawah
print("#", end="")

for j_2009 in range(4 * n_2009 + 5):
    print("=", end="")

print("#")