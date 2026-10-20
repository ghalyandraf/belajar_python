print("GEROBAK FRIED CHICKEN")
print("D = Dada  Rp. 2500")
print("P = Paha  Rp. 2000")
print("S = Sayap  Rp. 1500")

n = int(input("Banyak Jenis: "))
total = 0

for i in range(n):
    kode = input("Kode Potong (D/P/S): ").upper()
    beli = int(input("Banyak Beli: "))

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
        print("Kode salah!")
        continue

    jumlah = harga * beli
    total += jumlah

    print(jenis, "Rp.", jumlah)

pajak = total * 10 / 100
bayar = total + pajak

print("----------------------")
print("Jumlah Bayar: Rp.", total)
print("Pajak 10%   : Rp.", pajak)
print("Total Bayar : Rp.", bayar)