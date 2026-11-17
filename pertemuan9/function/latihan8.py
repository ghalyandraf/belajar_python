def garis(panjang=40):
    print("-" * panjang)


def hitung_subtotal(harga, jumlah):
    return harga * jumlah


def hitung_diskon(total_belanja):
    # Percabangan (If-Else) untuk menentukan persentase diskon
    if total_belanja >= 500000:
        diskon = 0.075
    elif total_belanja >= 300000:
        diskon = 0.05
    elif total_belanja >= 100000:
        diskon = 0.025
    else:
        diskon = 0
    return total_belanja * diskon, diskon


def tampilkan_struk(nama, total_belanja, diskon, total_bayar):
    print()
    print("-" * 12 + " STRUK PEMBELIAN " + "-" * 12)
    print(f"Nama Pembeli  : {nama}")
    print(f"Total Belanja : Rp {total_belanja:,.0f}".replace(",", "."))
    print(f"Diskon        : Rp {diskon:,.0f}".replace(",", "."))
    print(f"Total Bayar   : Rp {total_bayar:,.0f}".replace(",", "."))
    garis()


def main():
    # 1. Input data pembeli
    garis()
    nama = input("Masukkan nama pembeli: ")
    jumlah_jenis = 2
    print(f"Jumlah barang: {jumlah_jenis}")

    total_belanja = 0

    # 2. Input data barang
    for i in range(1, jumlah_jenis + 1):
        print(f"\nBarang ke-{i}")
        nama_barang = input("Nama barang: ")
        harga = float(input("Harga barang: "))
        jumlah_beli = int(input("Jumlah beli: "))

        subtotal = hitung_subtotal(harga, jumlah_beli)
        print(f"Subtotal: Rp {subtotal:,.0f}".replace(",", "."))
        total_belanja += subtotal

    # 3. Hitung diskon
    diskon, persen = hitung_diskon(total_belanja)
    total_bayar = total_belanja - diskon

    print()
    if diskon > 0:
        print("Selamat! Anda mendapatkan diskon.")
    else:
        print("Maaf, belum ada diskon untuk belanja ini.")

    # 4. Tampilkan struk
    tampilkan_struk(nama, total_belanja, diskon, total_bayar)


main()