def input_matriks(baris, kolom, nama):
    print(f"\nInput elemen matriks {nama}:")
    matriks = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(int(input(f"{nama}[{i + 1}][{j + 1}] = ")))
        matriks.append(row)
    return matriks


def tampil_matriks(matriks, judul):
    print(f"\n{judul}:")
    for row in matriks:
        print("\t".join(str(x) for x in row))


print("=== PERKALIAN MATRIKS ===")

print("\nOrdo matriks A")
baris_a = int(input("Jumlah baris : "))
kolom_a = int(input("Jumlah kolom : "))

print("\nOrdo matriks B")
baris_b = int(input("Jumlah baris : "))
kolom_b = int(input("Jumlah kolom : "))

if min(baris_a, kolom_a, baris_b, kolom_b) <= 0:
    print("\nOrdo harus lebih dari 0!")
# VALIDASI: jumlah kolom matriks pertama HARUS SAMA DENGAN jumlah baris matriks kedua
elif kolom_a != baris_b:
    print("\nPerkalian TIDAK DAPAT dilakukan!")
    print(f"Jumlah kolom matriks A ({kolom_a}) harus sama dengan "
          f"jumlah baris matriks B ({baris_b}).")
else:
    A = input_matriks(baris_a, kolom_a, "A")
    B = input_matriks(baris_b, kolom_b, "B")

    # Hasil berordo baris_a x kolom_b
    C = [[0] * kolom_b for _ in range(baris_a)]
    for i in range(baris_a):
        for j in range(kolom_b):
            for k in range(kolom_a):
                C[i][j] += A[i][k] * B[k][j]

    tampil_matriks(A, "Matriks A")
    tampil_matriks(B, "Matriks B")
    tampil_matriks(C, "Hasil A x B")