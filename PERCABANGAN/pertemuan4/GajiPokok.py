gaji_pokok = 300000

print("====================================")
print("       PROGRAM HITUNG GAJI")
print("====================================")

nama = input("Nama Karyawan       : ")
golongan = int(input("Golongan Jabatan (1-3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Jumlah Jam Kerja    : "))

if golongan == 1:
    persen_jabatan = 5
elif golongan == 2:
    persen_jabatan = 10
elif golongan == 3:
    persen_jabatan = 15
else:
    persen_jabatan = 0
    print("Golongan tidak valid!")

tunjangan_jabatan = gaji_pokok * persen_jabatan / 100

if pendidikan == "SMA":
    persen_pendidikan = 2.5
elif pendidikan == "D1":
    persen_pendidikan = 5
elif pendidikan == "D3":
    persen_pendidikan = 20
elif pendidikan == "S1":
    persen_pendidikan = 30
else:
    persen_pendidikan = 0
    print("Pendidikan tidak valid!")

tunjangan_pendidikan = gaji_pokok * persen_pendidikan / 100

if jam_kerja > 8:
    jam_lembur = jam_kerja - 8
else:
    jam_lembur = 0

honor_lembur = jam_lembur * 3500

total_gaji = (
    gaji_pokok
    + tunjangan_jabatan
    + tunjangan_pendidikan
    + honor_lembur
)

print("\n====================================")
print("          LAYAR KELUARAN")
print("====================================")
print("Karyawan yang bernama :", nama)
print("Honor yang diterima:")
print("------------------------------------")
print(f"Gaji Pokok            : Rp {gaji_pokok:,.0f}")
print(f"Tunjangan Jabatan     : Rp {tunjangan_jabatan:,.0f}")
print(f"Tunjangan Pendidikan  : Rp {tunjangan_pendidikan:,.0f}")
print(f"Honor Lembur           : Rp {honor_lembur:,.0f}")
print("------------------------------------")
print(f"TOTAL GAJI             : Rp {total_gaji:,.0f}")
print("====================================")