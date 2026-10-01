print("PROGRAM PENJUALAN BARANG")
print("-----------------------------")

#Input
kode = input("Masukkan kode barang : ")
nama = input("Masukkan nama barang : ")
harga = input("Masukkan harga barang : ")
jumlah = input("Masukkan jumlah beli : ")

print("-----------------------------")

#Output
print("STRUK PEMBAYARAN BARANG")
print("Kode Barang : " + str(kode))
print("Nama Barang : " + str(nama))
print("Harga Barang : " + str(harga))
print("Jumlah Beli : " + str(jumlah))
print("Total Harga : " + str(int(harga) * int(jumlah)))
print("-----------------------------")