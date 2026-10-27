def faktorial(n):
    if n == 0:  # BASE CASE
        return 1
    else:       # RECURSIVE CASE
        return n * faktorial(n - 1)

# Contoh pemanggilan fungsi untuk 5! (5 faktorial)
hasil = faktorial(5)
print(f"Hasil faktorial dari 5 adalah: {hasil}")