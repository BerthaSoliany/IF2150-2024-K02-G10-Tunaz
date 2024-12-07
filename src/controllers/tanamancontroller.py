import sqlite3
from src.controllers.tanaman import Tanaman

class TanamanController:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.cursor = self.conn.cursor()

    def tambah_tanaman(self, tanaman: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tanaman (jenis_tanaman, index_tanaman) VALUES (?, ?)", (tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        # cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        conn.close()

    def perbarui_tanaman(self, tanaman: Tanaman, tanaman_baru: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE tanaman SET jenis_tanaman = ?, index_tanaman = ? WHERE jenis_tanaman = ? AND index_tanaman = ?", (tanaman_baru.get_jenis(), tanaman_baru.get_index(), tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        # cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        conn.close()
    
    def hapus_tanaman(self, tanaman: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        # cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        conn.close()

    def lihat_tanaman(self):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tanaman;")
        # print(cursor.fetchall())
        # x = cursor.fetchall()
        # print(len(x))
        # print(x[0])
        # print(x[0][0])
        # print(x[0][1])
        # print(x[0][2])
        conn.close()

    def get_all_jenis_tanaman(self):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT jenis_tanaman FROM tanaman;")
        # make it unique (delete if theres same value)
        x = cursor.fetchall()
        y = []
        for i in x:
            if i[0] not in y:
                y.append(i[0])
        conn.close()
        return y

    def get_all_index_tanaman(self, jenis_tanaman):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT index_tanaman FROM tanaman WHERE jenis_tanaman = ?", (jenis_tanaman,))
        x = cursor.fetchall()
        y = []
        for i in x:
            y.append(i[0])
        conn.close()
        return y

# tanaman_controller = TanamanController()
# tanaman_controller.get_all_jenis_tanaman()
# tanaman1 = Tanaman(jenis_tanaman="JERUKkkzz", index_tanaman=1, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None)
# tanaman_controller.tambah_tanaman(tanaman1)
# tanaman_controller.lihat_tanaman()
