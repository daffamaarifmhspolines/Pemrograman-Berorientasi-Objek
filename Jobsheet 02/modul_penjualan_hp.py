class Handphone:
    def __init__(self, merk, tipe, harga, stok):
        self.merk = merk
        self.tipe = tipe
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"HP: {self.merk} {self.tipe}")
        print(f"Harga: Rp {self.harga}")
        print(f"Sisa Stok: {self.stok} unit")
        print("-" * 25)

    def jual_hp(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            total_harga = self.harga * jumlah
            print(f"Berhasil menjual {jumlah} unit {self.merk} {self.tipe}.")
            print(f"Total Pendapatan: Rp {total_harga}")
        else:
            print(f"Gagal! Stok {self.merk} {self.tipe} tidak mencukupi. (Sisa: {self.stok})")

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f"Stok {self.merk} {self.tipe} berhasil ditambahkan sebanyak {jumlah} unit.")
