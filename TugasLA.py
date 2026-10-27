total = 0

for i in range(1, 6):
    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i}: "))
    total = total + nilai

rata_rata = total / 5

print("Jumlah seluruh nilai:", total)
print("Rata-rata nilai kelas:", rata_rata)
