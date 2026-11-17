def data(nama, usia=17):
    print("Halo, saya", nama)
    print("Usia saya", usia)


def nilai(absen, tugas, uts, uas=70):
    total = (absen + tugas + uts + uas) / 4
    print("\nMendapatkan Nilai sebagai berikut")
    print("Nilai Absen Anda        :", absen)
    print("Nilai tugas Anda        :", tugas)
    print("Nilai UTS Anda          :", uts)
    print("Nilai UAS Anda          :", uas)
    print("Total Nilai Anda        :", total)
    return total


nama = input("Nama Saya : ")
data(nama)

absen = float(input("Nilai Absen : "))
tugas = float(input("Nilai Tugas : "))
uts = float(input("Nilai UTS   : "))
uas = float(input("Nilai UAS   : "))

nilai(absen, tugas, uts, uas)