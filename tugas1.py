import os

# Konstanta nama file
NAMA_FILE = 'stok_barang.txt'

def baca_data():
    """
    Membaca data dari file teks saat program dimulai.
    Data disimpan ke dalam dictionary dengan format:
    Key: KodeBarang
    Value: {'nama': NamaBarang, 'stok': JumlahStok}
    Ref: Ketentuan Program poin 1 & 2
    """
    data_barang = {}
    
    # Cek apakah file ada sebelum membaca
    if not os.path.exists(NAMA_FILE):
        print(f"File {NAMA_FILE} belum ada. Memulai dengan data kosong.")
        return data_barang

    try:
        with open(NAMA_FILE, 'r') as file:
            for baris in file:
                baris = baris.strip()
                if baris:  # Pastikan baris tidak kosong
                    parts = baris.split(',')
                    if len(parts) == 3:
                        kode = parts[0]
                        nama = parts[1]
                        stok = int(parts[2])
                        # Menyimpan ke dictionary
                        data_barang[kode] = {'nama': nama, 'stok': stok}
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")
    
    return data_barang

def simpan_data(data_barang):
    """
    Menu 5: Simpan ke file.
    Menyimpan seluruh data terbaru dari dictionary ke stok_barang.txt.
    Ref: Menu Minimal poin 5
    """
    try:
        with open(NAMA_FILE, 'w') as file:
            for kode, info in data_barang.items():
                line = f"{kode},{info['nama']},{info['stok']}\n"
                file.write(line)
        print("Data berhasil disimpan ke file.")
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")

def tampilkan_semua(data_barang):
    """
    Menu 1: Tampilkan semua barang.
    Menampilkan seluruh data stok barang (kode, nama, stok).
    Ref: Menu Minimal poin 1
    """
    print("\n=== DAFTAR STOK BARANG ===")
    if not data_barang:
        print("Data kosong.")
    else:
        print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok':<5}")
        print("-" * 36)
        for kode, info in data_barang.items():
            print(f"{kode:<10} | {info['nama']:<15} | {info['stok']:<5}")

def cari_barang(data_barang):
    """
    Menu 2: Cari barang berdasarkan kode.
    Ref: Menu Minimal poin 2
    """
    kode = input("Masukkan Kode Barang: ")
    if kode in data_barang:
        info = data_barang[kode]
        print(f"Ditemukan: {kode} - {info['nama']} - Stok: {info['stok']}")
    else:
        print("Barang tidak ditemukan")  # Sesuai instruksi gambar

def tambah_barang(data_barang):
    """
    Menu 3: Tambah barang baru.
    Ref: Menu Minimal poin 3
    """
    kode = input("Masukkan Kode Baru: ")
    if kode in data_barang:
        print("Kode sudah digunakan")  # Sesuai instruksi gambar
        return

    nama = input("Masukkan Nama Barang: ")
    try:
        stok = int(input("Masukkan Stok Awal: "))
        # Update dictionary di memori
        data_barang[kode] = {'nama': nama, 'stok': stok}
        print("Barang berhasil ditambahkan.")
    except ValueError:
        print("Error: Stok harus berupa angka.")

def update_stok(data_barang):
    """
    Menu 4: Update stok barang (tambah/kurang).
    Stok tidak boleh negatif.
    Ref: Menu Minimal poin 4
    """
    kode = input("Masukkan Kode Barang: ")
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    print(f"Barang: {data_barang[kode]['nama']} | Stok saat ini: {data_barang[kode]['stok']}")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    pilihan = input("Pilih aksi: ")

    try:
        jumlah = int(input("Masukkan jumlah: "))
        stok_sekarang = data_barang[kode]['stok']

        if pilihan == '1':
            data_barang[kode]['stok'] += jumlah
            print("Stok berhasil ditambah.")
        elif pilihan == '2':
            if stok_sekarang - jumlah < 0:
                print("Gagal: Stok tidak boleh negatif.")  # Validasi sesuai instruksi
            else:
                data_barang[kode]['stok'] -= jumlah
                print("Stok berhasil dikurangi.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Error: Input harus angka.")

def main():
    """
    Fungsi Utama (Main Loop).
    Mengatur alur program dan menu interaktif.
    Ref: Ketentuan Program poin 3
    """
    # Load data ke dictionary saat program mulai
    stok_kantin = baca_data()

    while True:
        print("\n=== MENU APLIKASI KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_semua(stok_kantin)
        elif pilihan == '2':
            cari_barang(stok_kantin)
        elif pilihan == '3':
            tambah_barang(stok_kantin)
        elif pilihan == '4':
            update_stok(stok_kantin)
        elif pilihan == '5':
            simpan_data(stok_kantin)
        elif pilihan == '0':
            print("Program selesai.")  # Ref: Menu 0
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()