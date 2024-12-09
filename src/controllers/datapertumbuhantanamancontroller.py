import sqlite3
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman

class DataPertumbuhanTanamanController:

    def tambah_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        if not isinstance(data_pertumbuhan_tanaman.get_tinggi_tanaman(), (int, float)):
            print("HOI")
            raise ValueError("Tinggi tanaman must be a number (real).")

        cursor.execute("SELECT * FROM Tanaman WHERE jenis_tanaman = ? AND index_tanaman = ?;", (jenis_tanaman, index_tanaman))
        print(cursor.fetchall())
        cursor.execute("INSERT INTO dataPertumbuhanTanaman (jenis_tanaman, index_tanaman, status_tanaman, tinggi_tanaman, tanggal_catatan, kondisi_daun) VALUES (?, ?, ?, ?, ?, ?)", (jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_status_tanaman(), data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan(), data_pertumbuhan_tanaman.get_kondisi_daun()))
        conn.commit()
        cursor.execute("SELECT * FROM dataPertumbuhanTanaman;")
        print(cursor.fetchall())
        conn.close()

    def perbarui_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman, data_pertumbuhan_tanaman_baru: DataPertumbuhanTanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("UPDATE dataPertumbuhanTanaman SET status_tanaman = ?, tinggi_tanaman = ?, tanggal_catatan = ?, kondisi_daun = ? WHERE jenis_tanaman = ? AND index_tanaman = ? AND status_tanaman = ? AND tinggi_tanaman = ? AND tanggal_catatan = ? AND kondisi_daun = ?", (data_pertumbuhan_tanaman_baru.get_status_tanaman(), data_pertumbuhan_tanaman_baru.get_tinggi_tanaman(), data_pertumbuhan_tanaman_baru.get_tanggal_catatan(), data_pertumbuhan_tanaman_baru.get_kondisi_daun(), jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_status_tanaman(), data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan(), data_pertumbuhan_tanaman.get_kondisi_daun()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataPertumbuhanTanaman;")
        # print(cursor.fetchall())
        conn.close()
        
    def hapus_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataPertumbuhanTanaman WHERE jenis_tanaman = ? AND index_tanaman = ? AND status_tanaman = ? AND tinggi_tanaman = ? AND tanggal_catatan = ? AND kondisi_daun = ?", (jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_status_tanaman(), data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan(), data_pertumbuhan_tanaman.get_kondisi_daun()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataPertumbuhanTanaman;")
        # print(cursor.fetchall())
        conn.close()

# data_pertumbuhan_tanaman = DataPertumbuhanTanamanController()
# data_pertumbuhan_tanaman1 = DataPertumbuhanTanaman("Sehat", 20, "2021-01-01", "Daun berwarna hijau")
# data_pertumbuhan_tanaman.tambah_data_pertumbuhan("JERUK", 2, data_pertumbuhan_tanaman1)
# data_pertumbuhan_tanaman.hapus_data_pertumbuhan("JERUK", 2, data_pertumbuhan_tanaman1)

    