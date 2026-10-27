def pangkat(x, y):
    if y == 0:  # BASE CASE
        return 1
    else:       # RECURSIVE CASE
        return x * pangkat(x, y-1)

# Contoh pemanggilan dan output
x = 10
y = 3
hasil = pangkat(x, y)
print(f"Masukan Nilai X : {x}")
print(f"Masukan Nilai Y : {y}")
print(f"{x} dipangkatkan {y} = {hasil}")