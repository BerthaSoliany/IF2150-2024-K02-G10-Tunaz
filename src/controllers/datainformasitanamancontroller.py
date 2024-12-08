import sqlite3
from datainformasitanaman import DataInformasiTanaman

class DataInformasiTanamanController:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def tambah_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int, data_informasi_tanaman: DataInformasiTanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dataInformasiTanaman (jenis_tanaman, index_tanaman, waktu_tanam, kebutuhan_perawatan) VALUES (?, ?, ?, ?)", (jenis_tanaman, index_tanaman, data_informasi_tanaman.get_waktu_tanam(), data_informasi_tanaman.get_kebutuhan_perawatan()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataInformasiTanaman;")
        # print(cursor.fetchall())
        conn.close()

    def perbarui_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int, data_informasi_tanaman_baru: DataInformasiTanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("UPDATE dataInformasiTanaman SET kebutuhan_perawatan = ? WHERE jenis_tanaman = ? AND index_tanaman = ?", (data_informasi_tanaman_baru.get_kebutuhan_perawatan(), jenis_tanaman, index_tanaman))
        conn.commit()
        # cursor.execute("SELECT * FROM dataInformasiTanaman;")
        # print(cursor.fetchall())
        conn.close()

    def hapus_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataInformasiTanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (jenis_tanaman, index_tanaman))
        conn.commit()
        # cursor.execute("SELECT * FROM dataInformasiTanaman;")
        # print(cursor.fetchall())
        conn.close()

# data_informasi_tanaman = DataInformasiTanamanController()
# data_informasi_tanaman1 = DataInformasiTanaman("2021-01-01", "Pemupukan setiap 2 minggu sekali")
# data_informasi_tanaman.tambah_data_informasi_tanaman("JERUK", 2, data_informasi_tanaman1)
# data_informasi_tanaman.hapus_data_informasi_tanaman("JERUK", 2)