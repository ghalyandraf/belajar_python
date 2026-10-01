print("PROGRAM PENJUALAN BARANG")
print("-----------------------------")

# Input
dbw = input("Uang dibawa : ")
berat = input("Masukkan berat telur (kg) : ")
telur = input("Biaya telur per kg : ")
angkot = input("Biaya angkot : ")
brp = input("Berapa kali angkot : ")

print("-----------------------------")

# Perhitungan
total_telur = int(berat) * int(telur)
total_angkot = int(angkot) * int(brp)
total_pengeluaran = total_telur + total_angkot
sisa_uang = int(dbw) - total_pengeluaran

# Output
print("HASIL PERHITUNGAN")
print("Uang dibawa : " + str(dbw))
print("Berat telur : " + str(berat) + " kg")
print("Biaya telur : " + str(total_telur))
print("Berapa kali angkot : " + str(brp))
print("Biaya angkot : " + str(total_angkot))
print("Total pengeluaran : " + str(total_pengeluaran))
print("Sisa uang : " + str(sisa_uang))
print("-----------------------------")