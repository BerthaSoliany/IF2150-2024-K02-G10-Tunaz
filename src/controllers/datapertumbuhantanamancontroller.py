import sqlite3
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman

class DataPertumbuhanTanamanController:

    def tambah_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        try:
            tinggi_tanaman = float(data_pertumbuhan_tanaman.get_tinggi_tanaman())  # Convert to float
            data_pertumbuhan_tanaman.set_tinggi_tanaman(tinggi_tanaman)
        except ValueError:
            raise ValueError("Tinggi tanaman must be a valid number (real).")

        cursor.execute("SELECT * FROM Tanaman WHERE jenis_tanaman = ? AND index_tanaman = ?;", (jenis_tanaman, index_tanaman))
        print(cursor.fetchall())
        cursor.execute("INSERT INTO dataPertumbuhanTanaman (jenis_tanaman, index_tanaman, status_tanaman, tinggi_tanaman, tanggal_catatan, kondisi_daun) VALUES (?, ?, ?, ?, ?, ?)", (jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_status_tanaman(), data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan(), data_pertumbuhan_tanaman.get_kondisi_daun()))
        conn.commit()
        cursor.execute("SELECT * FROM dataPertumbuhanTanaman;")
        print(cursor.fetchall())
        conn.close()

    def perbarui_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman, data_pertumbuhan_tanaman_baru: DataPertumbuhanTanaman):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("UPDATE dataPertumbuhanTanaman SET status_tanaman = ?, tinggi_tanaman = ?, tanggal_catatan = ?, kondisi_daun = ? WHERE jenis_tanaman = ? AND index_tanaman = ? AND status_tanaman = ? AND tinggi_tanaman = ? AND tanggal_catatan = ? AND kondisi_daun = ?", (data_pertumbuhan_tanaman_baru.get_status_tanaman(), data_pertumbuhan_tanaman_baru.get_tinggi_tanaman(), data_pertumbuhan_tanaman_baru.get_tanggal_catatan(), data_pertumbuhan_tanaman_baru.get_kondisi_daun(), jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_status_tanaman(), data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan(), data_pertumbuhan_tanaman.get_kondisi_daun()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataPertumbuhanTanaman;")
        # print(cursor.fetchall())
        conn.close()
        
    def hapus_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataPertumbuhanTanaman WHERE jenis_tanaman = ? AND index_tanaman = ? AND status_tanaman = ? AND tinggi_tanaman = ? AND tanggal_catatan = ? AND kondisi_daun = ?", (jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_status_tanaman(), data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan(), data_pertumbuhan_tanaman.get_kondisi_daun()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataPertumbuhanTanaman;")
        # print(cursor.fetchall())
        conn.close()

    def get_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int, data_pertumbuhan_tanaman: DataPertumbuhanTanaman):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataPertumbuhanTanaman WHERE jenis_tanaman = ? AND index_tanaman = ? AND tinggi_tanaman = ? AND tanggal_catatan = ?", (jenis_tanaman, index_tanaman, data_pertumbuhan_tanaman.get_tinggi_tanaman(), data_pertumbuhan_tanaman.get_tanggal_catatan()))
        x = cursor.fetchone()
        conn.close()
        x = DataPertumbuhanTanaman(status_tanaman=x[3], tinggi_tanaman=x[4], tanggal_catatan=x[5], kondisi_daun=x[6])
        return x
    
    def get_all_data_pertumbuhan(self, jenis_tanaman: str, index_tanaman: int):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataPertumbuhanTanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (jenis_tanaman, index_tanaman))
        x = cursor.fetchall()
        conn.close()
        data_pertumbuhan = []
        for data in x:
            data_pertumbuhan.append(DataPertumbuhanTanaman(status_tanaman=data[3], tinggi_tanaman=data[4], tanggal_catatan=data[5], kondisi_daun=data[6]))
        return data_pertumbuhan
# data_pertumbuhan_tanaman = DataPertumbuhanTanamanController()
# data_pertumbuhan_tanaman1 = DataPertumbuhanTanaman("Sehat", 5, "2024-12-12", "Daun berwarna hijau")
# data_pertumbuhan_tanaman.tambah_data_pertumbuhan("JERUK", 2, data_pertumbuhan_tanaman1)
# data_pertumbuhan_tanaman.hapus_data_pertumbuhan("JERUK", 2, data_pertumbuhan_tanaman1)

    