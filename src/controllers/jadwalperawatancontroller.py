import sqlite3
from jadwalperawatan import JadwalPerawatan 

class JadwalPerawatanController:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.cursor = self.conn.cursor()

    def tambah_data_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dataJadwalPerawatan (jenis_tanaman, index_tanaman, frekuensi_penyiraman, frekuensi_pemupukan, waktu_penyiraman, waktu_pemupukan, pilihan_notifikasi) VALUES (?, ?, ?, ?, ?, ?, ?);", (jenis_tanaman, index_tanaman, jadwal_perawatan.get_frekuensi_penyiraman(), jadwal_perawatan.get_frekuensi_pemupukan(), jadwal_perawatan.get_waktu_penyiraman(), jadwal_perawatan.get_waktu_pemupukan(), jadwal_perawatan.get_pilihan_notifikasi()))
        conn.commit()
        cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        print(cursor.fetchall())
        conn.close()

    def ubah_data_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan_baru: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE dataJadwalPerawatan SET frekuensi_penyiraman = ?, frekuensi_pemupukan = ?, waktu_penyiraman = ?, waktu_pemupukan = ?, pilihan_notifikasi = ? WHERE jenis_tanaman = ? AND index_tanaman = ?;", (jadwal_perawatan_baru.get_frekuensi_penyiraman(), jadwal_perawatan_baru.get_frekuensi_pemupukan(), jadwal_perawatan_baru.get_waktu_penyiraman(), jadwal_perawatan_baru.get_waktu_pemupukan(), jadwal_perawatan_baru.get_pilihan_notifikasi(), jenis_tanaman, index_tanaman))
        conn.commit()
        cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        print(cursor.fetchall())
        conn.close()

    def hapus_data_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataJadwalPerawatan WHERE jenis_tanaman = ? AND index_tanaman = ?;", (jenis_tanaman, index_tanaman))
        conn.commit()
        cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        print(cursor.fetchall())
        conn.close()

    def susun_jadwal_penyiraman():
        pass #soon

    def susun_jadwal_pemupukan():
        pass #soon

# jadwal_perawatan = JadwalPerawatanController()
# jadwal_perawatan1 = JadwalPerawatan(3, 5, "07:00", "07:00", True)
# jadwal_perawatan.tambah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan1)
# jadwal_perawatan2 = JadwalPerawatan(2, 4, "08:00", "08:00", False)
# jadwal_perawatan.ubah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan2)
# jadwal_perawatan.hapus_data_jadwal_perawatan("JERUK", 2)