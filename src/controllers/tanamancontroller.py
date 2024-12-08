import sqlite3
from tanaman import Tanaman

class TanamanController:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def tambah_tanaman(self, tanaman: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO jenisTracker (jenis_tanaman, last_tanaman_index) VALUES (?, ?)", (tanaman.get_jenis(), 0))  
        cursor.execute("UPDATE jenisTracker SET last_tanaman_index = (last_tanaman_index + 1) WHERE jenis_tanaman = ?", (tanaman.get_jenis(),))
        cursor.execute("SELECT last_tanaman_index FROM jenisTracker WHERE jenis_tanaman = ?", (tanaman.get_jenis(),))
        index_tanaman = cursor.fetchone()[0]
        cursor.execute("INSERT INTO tanaman (jenis_tanaman, index_tanaman) VALUES (?, ?)", (tanaman.get_jenis(), index_tanaman))
        conn.commit()
        # cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        conn.close()

    def perbarui_tanaman(self, tanaman: Tanaman, tanaman_baru: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO jenisTracker (jenis_tanaman, last_tanaman_index) VALUES (?, ?)", (tanaman.get_jenis(), 0))  
        cursor.execute("UPDATE jenisTracker SET last_tanaman_index = (last_tanaman_index + 1) WHERE jenis_tanaman = ?", (tanaman.get_jenis(),))
        cursor.execute("SELECT last_tanaman_index FROM jenisTracker WHERE jenis_tanaman = ?", (tanaman.get_jenis(),))
        index_tanaman = cursor.fetchone()[0]
        cursor.execute("UPDATE tanaman SET jenis_tanaman = ?, index_tanaman = ? WHERE jenis_tanaman = ? AND index_tanaman = ?", (tanaman_baru.get_jenis(), index_tanaman, tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        # cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        conn.close()
    
    def hapus_tanaman(self, tanaman: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        # cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        conn.close()

# tanaman_controller = TanamanController()
# tanaman1 = Tanaman(jenis_tanaman="JERUKkkzz", index_tanaman=1, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None)
# tanaman_controller.tambah_tanaman(tanaman1)