from prettytable import PrettyTable

# Inisialisasi daftar produk
produk = [
    {"nama": "Yakuza 0", "harga": 70000.00},
    {"nama": "Yakuza Kiwami", "harga": 85000.00},
    {"nama": "L.A Noire", "harga": 60000.00},
    {"nama": "Stardew Valley", "harga": 55000.00},
    {"nama": "Halo Infinite", "harga": 70000.00},
    {"nama": "Fallout 4", "harga": 30000.000},
    {"nama": "Project Zomboid", "harga": 80000.00},
    {"nama": "Payday 2", "harga": 60000.00},
    {"nama": "The Crew 2", "harga": 115000.00},
    {"nama": "Life is Strange", "harga": 75000.00},
]

# Inisialisasi keranjang belanja
keranjang_belanja = {}

# Fungsi untuk menampilkan daftar produk
def tampilkan_daftar_produk():
    if not produk:
        print("Daftar produk kosong.")
        return
    
    tabel_produk = PrettyTable()
    tabel_produk.field_names = ["No.", "Nama Produk", "Harga"]
    
    for i, item in enumerate(produk, start=1):
        harga_produk = "{:.2f}".format(item["harga"])
        harga_produk = harga_produk.rjust(9)
        tabel_produk.add_row([i, item["nama"], harga_produk])
    
    print(tabel_produk)

# Fungsi untuk menambahkan produk baru
def tambahkan_produk():
    nama_produk = input("Masukkan nama produk: ")
    harga_produk = float(input("Masukkan harga produk: "))
    produk_baru = {"nama": nama_produk, "harga": harga_produk}
    produk.append(produk_baru)
    print(f"Produk '{nama_produk}' berhasil ditambahkan.")

# Fungsi untuk mengedit produk
def edit_produk():
    tampilkan_daftar_produk()
    nomor_produk = int(input("Masukkan nomor produk yang ingin diedit: ")) - 1
    if nomor_produk >= 0 and nomor_produk < len(produk):
        nama_produk = input("Masukkan nama produk baru: ")
        harga_produk = float(input("Masukkan harga produk baru: "))
        produk[nomor_produk]["nama"] = nama_produk
        produk[nomor_produk]["harga"] = harga_produk
        print("Produk berhasil diedit.")
    else:
        print("Nomor produk tidak valid.")

# Fungsi untuk menghapus produk
def hapus_produk():
    tampilkan_daftar_produk()
    nomor_produk = int(input("Masukkan nomor produk yang ingin dihapus: ")) - 1
    if nomor_produk >= 0 and nomor_produk < len(produk):
        produk_terhapus = produk.pop(nomor_produk)
        print(f"Produk '{produk_terhapus['nama']}' berhasil dihapus.")
    else:
        print("Nomor produk tidak valid.")

# Fungsi untuk membeli barang
def beli_barang():
    tampilkan_daftar_produk()
    nomor_barang = int(input("Masukkan nomor barang yang ingin dibeli: ")) - 1
    if nomor_barang >= 0 and nomor_barang < len(produk):
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        if jumlah > 0:
            barang_terpilih = produk[nomor_barang]["nama"]
            harga_barang = produk[nomor_barang]["harga"]
            subtotal = harga_barang * jumlah
            if barang_terpilih in keranjang_belanja:
                keranjang_belanja[barang_terpilih]["jumlah"] += jumlah
                keranjang_belanja[barang_terpilih]["subtotal"] += subtotal
            else:
                keranjang_belanja[barang_terpilih] = {"jumlah": jumlah, "subtotal": subtotal}
            print(f"{jumlah} {barang_terpilih} berhasil ditambahkan ke keranjang belanja.")
        else:
            print("Jumlah harus lebih dari 0.")
    else:
        print("Nomor barang tidak valid.")

# Fungsi untuk menampilkan keranjang belanja
def tampilkan_keranjang_belanja():
    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
        return

    tabel_keranjang = PrettyTable()
    tabel_keranjang.field_names = ["Nama Barang", "Jumlah", "Harga Satuan", "Subtotal"]
    total_belanja = 0

    for barang_terpilih, data in keranjang_belanja.items():
        jumlah = data["jumlah"]
        harga_satuan = [item["harga"] for item in produk if item["nama"] == barang_terpilih][0]
        subtotal = harga_satuan * jumlah

        harga_satuan = "{:.2f}".format(harga_satuan)
        harga_satuan = harga_satuan.rjust(9)

        tabel_keranjang.add_row([barang_terpilih, jumlah, harga_satuan, subtotal])
        total_belanja += subtotal

    print(tabel_keranjang)
    print(f"Total Belanja: {total_belanja:.2f}")

# Fungsi untuk pembayaran
def pembayaran():
    tampilkan_keranjang_belanja()
    total_belanja = sum([data["subtotal"] for data in keranjang_belanja.values()])
    print(f"Total Belanja: {total_belanja:.2f}")
    jumlah_pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: "))
    if jumlah_pembayaran >= total_belanja:
        kembalian = jumlah_pembayaran - total_belanja
        print(f"Kembalian Anda: {kembalian:.2f}")
        keranjang_belanja.clear()
    else:
        print("Jumlah uang yang dibayarkan kurang dari total belanja.")

# Fungsi utama program
def main():
    peran = input("Masukkan peran Anda (admin/pembeli): ").lower()

    if peran == "admin":
        while True:
            print("\n=== Selamat datang, Admin ===")
            print("1. Tampilkan Daftar Produk")
            print("2. Tambahkan Produk")
            print("3. Edit Produk")
            print("4. Hapus Produk")
            print("5. Keluar dari Mode Admin")

            pilihan_admin = input("Pilih menu: ")

            if pilihan_admin == "1":
                tampilkan_daftar_produk()
            elif pilihan_admin == "2":
                tambahkan_produk()
            elif pilihan_admin == "3":
                edit_produk()
            elif pilihan_admin == "4":
                hapus_produk()
            elif pilihan_admin == "5":
                print("Anda telah keluar dari mode Admin.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

    elif peran == "pembeli":
        while True:
            print("\n=== Selamat datang, Pembeli ===")
            print("1. Tampilkan Daftar Produk")
            print("2. Beli Barang")
            print("3. Tampilkan Keranjang Belanja")
            print("4. Pembayaran")
            print("5. Keluar dari Mode Pembeli")

            pilihan_pembeli = input("Pilih menu: ")

            if pilihan_pembeli == "1":
                tampilkan_daftar_produk()
            elif pilihan_pembeli == "2":
                beli_barang()
            elif pilihan_pembeli == "3":
                tampilkan_keranjang_belanja()
            elif pilihan_pembeli == "4":
                pembayaran()
            elif pilihan_pembeli == "5":
                print("Anda telah keluar dari mode Pembeli.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
    else:
        print("Peran tidak valid. Silakan masukkan 'admin' atau 'pembeli'.")

if __name__ == "__main__":
    main()

