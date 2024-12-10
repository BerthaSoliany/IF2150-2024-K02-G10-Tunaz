import sqlite3
from src.controllers.tanaman import Tanaman

class GrafikPertumbuhan:
    
    def tinggi_terhadap_waktu(self, tanaman: Tanaman):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT tanggal_catatan, tinggi_tanaman FROM dataPertumbuhanTanaman WHERE jenis_tanaman = ? AND index_tanaman = ? ORDER BY tanggal_catatan ASC", (tanaman.get_jenis(), tanaman.get_index()))
        conn.commit()
        x = cursor.fetchall()
        tinggi_tanaman = []
        for tinggi in x:
            tinggi_tanaman.append(tinggi[1])
        tanggal_catatan = []
        for tanggal in x:
            tanggal_catatan.append(tanggal[0])
        conn.close()
        return tinggi_tanaman, tanggal_catatan

# graph = GrafikPertumbuhan()
# x = graph.tinggi_terhadap_waktu(Tanaman(jenis_tanaman="JERUK", index_tanaman=2, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None))
# print(x)
