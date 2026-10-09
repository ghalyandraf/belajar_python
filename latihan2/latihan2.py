print("=" * 35)
print("       PROGRAM KASIR TOKO MAINAN     ")
print("=" * 35)

# Input Data
nama_pembeli = input("Masukkan Nama Pembeli : ")
kode_barang = input("Masukkan Kode Mainan : ")
harga_satuan = int(input("Masukkan Harga (Rp) : "))
jumlah_pesanan = int(input("Masukkan Jumlah Beli : "))

# Proses Perhitungan
total_bayar = harga_satuan * jumlah_pesanan

# Output / Struk Transaksi
print("\n" + "=" * 35)
print("         STRUK PEMBELIAN            ")
print("=" * 35)
print(f"Nama Pembeli : {nama_pembeli}")
print(f"Kode Mainan  : {kode_barang}")
print(f"Harga Satuan : Rp {harga_satuan:,}")
print(f"Jumlah Beli  : {jumlah_pesanan} pcs")
print(f"Total Bayar  : Rp {total_bayar:,}")
print("=" * 35)