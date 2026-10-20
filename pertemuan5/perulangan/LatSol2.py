
print("=" * 55)
print("              GEROBAK FRIED CHICKEN")
print("=" * 55)

print("Kode   Jenis Potong   Harga")
print("-" * 35)
print("D      Dada           Rp. 2500")
print("P      Paha           Rp. 2000")
print("S      Sayap          Rp. 1500")
print("-" * 35)

# Input banyak jenis
banyak_jenis = int(input("\nBanyak Jenis: "))

# Data transaksi
data_pembelian = []
jumlah_bayar = 0

# Perulangan untuk setiap jenis potongan
for i in range(banyak_jenis):
    print(f"\nJenis Ke-{i + 1}")

    kode = input("Kode Potong [D/P/S]: ").upper()
    banyak_potong = int(input("Banyak Potong: "))

    # Menentukan jenis dan harga
    if kode == "D":
        jenis = "Dada"
        harga = 2500
    elif kode == "P":
        jenis = "Paha"
        harga = 2000
    elif kode == "S":
        jenis = "Sayap"
        harga = 1500
    else:
        print("Kode potong tidak valid!")
        continue

    # Menghitung jumlah harga
    jumlah_harga = harga * banyak_potong
    jumlah_bayar += jumlah_harga

    data_pembelian.append([
        jenis, harga, banyak_potong, jumlah_harga
    ])

# Menghitung pajak dan total
pajak = jumlah_bayar * 10 / 100
total_bayar = jumlah_bayar + pajak

# Menampilkan output
print("\n" + "=" * 65)
print("                 GEROBAK FRIED CHICKEN")
print("=" * 65)
print(f"{'No.':<5}{'Jenis':<12}{'Harga':>10}{'Banyak':>10}{'Jumlah':>15}")
print(f"{'':<17}{'Satuan':>8}{'Beli':>10}{'Harga':>15}")
print("-" * 65)

for i, data in enumerate(data_pembelian, start=1):
    jenis, harga, banyak_potong, jumlah_harga = data

    print(
        f"{i:<5}{jenis:<12}"
        f"{harga:>10,}{banyak_potong:>10}"
        f"{'Rp ' + format(jumlah_harga, ','):>15}"
    )

print("-" * 65)
print(f"{'Jumlah Bayar':>43} Rp {jumlah_bayar:>10,}")
print(f"{'Pajak 10%':>43} Rp {pajak:>10,.0f}")
print(f"{'Total Bayar':>43} Rp {total_bayar:>10,.0f}")
print("=" * 65)
