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


print("=== PENJUMLAHAN & PENGURANGAN MATRIKS ===")
baris = int(input("Masukkan jumlah baris : "))
kolom = int(input("Masukkan jumlah kolom : "))

if baris <= 0 or kolom <= 0:
    print("Ordo harus lebih dari 0!")
else:
    # Kedua matriks memiliki ordo yang sama
    A = input_matriks(baris, kolom, "A")
    B = input_matriks(baris, kolom, "B")

    jumlah = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    selisih = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]

    tampil_matriks(A, "Matriks A")
    tampil_matriks(B, "Matriks B")
    tampil_matriks(jumlah, "Hasil A + B")
    tampil_matriks(selisih, "Hasil A - B")