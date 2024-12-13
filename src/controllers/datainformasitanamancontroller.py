import sqlite3
from src.controllers.datainformasitanaman import DataInformasiTanaman

class DataInformasiTanamanController:

    def tambah_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int, data_informasi_tanaman: DataInformasiTanaman):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dataInformasiTanaman (jenis_tanaman, index_tanaman, waktu_tanam, kebutuhan_perawatan) VALUES (?, ?, ?, ?)", (jenis_tanaman, index_tanaman, data_informasi_tanaman.get_waktu_tanam(), data_informasi_tanaman.get_kebutuhan_perawatan()))
        conn.commit()
        cursor.execute("SELECT * FROM dataInformasiTanaman;")
        print(cursor.fetchall())
        conn.close()

    def perbarui_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int, data_informasi_tanaman_baru: DataInformasiTanaman):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("UPDATE dataInformasiTanaman SET kebutuhan_perawatan = ? WHERE jenis_tanaman = ? AND index_tanaman = ?", (data_informasi_tanaman_baru.get_kebutuhan_perawatan(), jenis_tanaman, index_tanaman))
        conn.commit()
        # cursor.execute("SELECT * FROM dataInformasiTanaman;")
        # print(cursor.fetchall())
        conn.close()

    def hapus_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataInformasiTanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (jenis_tanaman, index_tanaman))
        conn.commit()
        # cursor.execute("SELECT * FROM dataInformasiTanaman;")
        # print(cursor.fetchall())
        conn.close()

    def get_all_informasi_tanaman(self):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataInformasiTanaman;")
        x = cursor.fetchall()
        # print(cursor.fetchall())
        conn.close()
        return x
    
    def sort_by_jenis_tanaman_ascending(self):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataInformasiTanaman ORDER BY jenis_tanaman ASC;")
        x = cursor.fetchall()
        # print(cursor.fetchall())
        conn.close()
        return x

    def sort_by_jenis_tanaman_descending(self):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataInformasiTanaman ORDER BY jenis_tanaman DESC;")
        x = cursor.fetchall()
        # print(cursor.fetchall())
        conn.close()
        return x
    
    def sort_by_waktu_tanam_ascending(self):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataInformasiTanaman ORDER BY waktu_tanam ASC;")
        x = cursor.fetchall()
        # print(cursor.fetchall())
        conn.close()
        return x

    def sort_by_waktu_tanam_descending(self):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataInformasiTanaman ORDER BY waktu_tanam DESC;")
        x = cursor.fetchall()
        # print(cursor.fetchall())
        conn.close()
        return x
    
    def get_data_informasi_tanaman(self, jenis_tanaman: str, index_tanaman: int):
        conn = sqlite3.connect("src/database/tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataInformasiTanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (jenis_tanaman, index_tanaman))
        x = cursor.fetchone()
        # print(cursor.fetchall())
        conn.close()
        return x
    
    def search_database(self, keyword: str, opt_sortby: str):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        search_keyword = f"%{keyword}%"  # Wildcard for partial matching

        if opt_sortby == "Jenis Tanaman (asc)":
            cursor.execute("SELECT * FROM dataInformasiTanaman WHERE jenis_tanaman LIKE ? OR index_tanaman LIKE ? ORDER BY jenis_tanaman ASC;", (search_keyword, search_keyword))
        elif opt_sortby == "Jenis Tanaman (desc)":
            cursor.execute("SELECT * FROM dataInformasiTanaman WHERE jenis_tanaman LIKE ? OR index_tanaman LIKE ? ORDER BY jenis_tanaman DESC;", (search_keyword, search_keyword))
        elif opt_sortby == "Tanggal Penanaman (asc)":
            cursor.execute("SELECT * FROM dataInformasiTanaman WHERE jenis_tanaman LIKE ? OR index_tanaman LIKE ? ORDER BY waktu_tanam ASC;", (search_keyword, search_keyword))
        elif opt_sortby == "Tanggal Penanaman (desc)":
            cursor.execute("SELECT * FROM dataInformasiTanaman WHERE jenis_tanaman LIKE ? OR index_tanaman LIKE ? ORDER BY waktu_tanam DESC;", (search_keyword, search_keyword))
        else:
            cursor.execute("SELECT * FROM dataInformasiTanaman WHERE jenis_tanaman LIKE ? OR index_tanaman LIKE ?", (search_keyword, search_keyword))
        results = cursor.fetchall() 
        conn.close()
        return results
# data_informasi_tanaman = DataInformasiTanamanController()
# print(data_informasi_tanaman.get_all_informasi_tanaman())
# data_informasi_tanaman1 = DataInformasiTanaman("2024-12-10", "Ini Kaktus")
# data_informasi_tanaman.tambah_data_informasi_tanaman("KAKTUS", 1, data_informasi_tanaman1)
# data_informasi_tanaman.hapus_data_informasi_tanaman("JERUK", 2)