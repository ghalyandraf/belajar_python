def data(nama, usia=17):
    print("Halo, saya ", nama)
    print("Usia saya ", usia)

nama=input("Nama Saya : ")
data(nama)

total=0
def nilai(absen, tugas, uts, uas=70):
    total=(absen+tugas+uts+uas)/4
    print("Mendapatkan Nilai sebagai berikut")
    print("Nilai Absen Anda        : ",absen)
    print("Nilai tugas Anda        : ",tugas)
    print("Nilai UTS Anda          : ",uts)
    print("Nilai UAS Anda          : ",uas)

    print("Total Nilai Anda        : ",total)
    return total

nilai (90, 70, 90, 80)