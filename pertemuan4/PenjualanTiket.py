#Input
pembeli=input("Input Nama Pembeli : ")
no_hp=input("Input No. Handphone : ")
jurusan=input("Input Jurusan [SBY/BL/LMP] : ")

#Proses
if jurusan=="SBY" or jurusan=="sby" :
    namajurusan="Surabaya"
    harga=300000
elif jurusan=="BL" or jurusan=="bl":
    namajurusan="Bali"
    harga=350000
elif jurusan=="LMP" or jurusan=="lmp":
    namajurusan="Lampung"
    harga=500000
else:
    namajurusan="Jurusan Tidak Valid"
    harga=0

#Input Jumlah Beli
jumlah=int(input("Masukkan Jumlah Beli : "))
#proses potongan
if jumlah>=3 :
    potongan=(jumlah*harga)*0.1
else:
    potongan=0

#Cetak Hasil
print("------------------------------------")
print(" PENJUALAN TIKET BUS")
print(" XYZ")
print("------------------------------------")
print("Nama Pembeli : "+str(pembeli))
print("No. Handphone : "+str(no_hp))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(namajurusan))
print("Harga : ",+(harga))
print("Jumlah Beli : ",+(jumlah))
print("------------------------------------")
print("potongan yang didapat : ",+(potongan))
total=(jumlah*harga)-potongan
print("Total Bayar : ",+(total))

ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali : ",+uangkembali)