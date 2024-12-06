import sqlite3
from tanaman import Tanaman

class GrafikPertumbuhan:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.cursor = self.conn.cursor()
    
    def tinggi_terhadap_waktu(self, tanaman: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT tanggal_catatan, tinggi_tanaman FROM dataPertumbuhanTanaman WHERE jenis_tanaman = ? AND index_tanaman = ?", (tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        x = cursor.fetchall()
        conn.close()
        return x

# graph = GrafikPertumbuhan()
# x = graph.tinggi_terhadap_waktu(Tanaman(jenis_tanaman="JERUK", index_tanaman=2, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None))
# print(x)
