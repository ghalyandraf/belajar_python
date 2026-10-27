bahan = ["beras", "telur", "minyak goreng", "gula", "garam"]
stok = [5, 2, 0, 1, 3]

perlu_dibeli = []

print("--- LAPORAN STOK BAHAN DAPUR ---")

for i, b in enumerate(bahan):
    jumlah = stok[i]
    
    if jumlah == 0:
        keterangan = "Habis, perlu beli!"
        perlu_dibeli.append(b)
    elif 1 <= jumlah <= 2:
        keterangan = "Menipis"
    else:
        keterangan = "Aman"
        
    print(f"{b.capitalize():<15}: {jumlah} ({keterangan})")

print("\n--------------------------------")
print("Daftar bahan yang harus dibeli:", perlu_dibeli)
print("Jumlah item yang habis:", len(perlu_dibeli))