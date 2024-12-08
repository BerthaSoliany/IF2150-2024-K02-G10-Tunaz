import sqlite3
from jadwalperawatan import JadwalPerawatan 
from datetime import datetime, timedelta

class JadwalPerawatanController:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def tambah_data_satu_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT last_group_id FROM groupJadwalPerawatan;")
        group_id = cursor.fetchone()[0]+1
        cursor.execute("UPDATE groupJadwalPerawatan SET last_group_id = ?;", (group_id,))

        cursor.execute("INSERT INTO dataJadwalPerawatan (jenis_tanaman, index_tanaman, group_id, frekuensi_perawatan, waktu_perawatan, jenis_perawatan, pilihan_notifikasi) VALUES (?, ?, ?, ?, ?, ?, ?);", (jenis_tanaman, index_tanaman, group_id, jadwal_perawatan.get_frekuensi_perawatan(), jadwal_perawatan.get_waktu_perawatan(), jadwal_perawatan.get_jenis_perawatan(), jadwal_perawatan.get_pilihan_notifikasi()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        conn.close()

    def tambah_data_group_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT last_group_id FROM groupJadwalPerawatan;")
        group_id = cursor.fetchone()[0]+1
        cursor.execute("UPDATE groupJadwalPerawatan SET last_group_id = ?;", (group_id,))

        waktu_akhir_perawatan = datetime.strptime(jadwal_perawatan.get_waktu_perawatan(), "%Y-%m-%d %H:%M:%S") # awalnya, waktu_perawatan bukan waktu_perawatan beneran, tapi waktu_akhir_perawatan
        waktu_perawatan = datetime.now()

        while waktu_perawatan <= waktu_akhir_perawatan:
            cursor.execute("INSERT INTO dataJadwalPerawatan (jenis_tanaman, index_tanaman, group_id, frekuensi_perawatan, waktu_perawatan, jenis_perawatan, pilihan_notifikasi) VALUES (?, ?, ?, ?, ?, ?, ?);", (jenis_tanaman, index_tanaman, group_id, jadwal_perawatan.get_frekuensi_perawatan(), jadwal_perawatan.get_waktu_perawatan(), jadwal_perawatan.get_jenis_perawatan(), jadwal_perawatan.get_pilihan_notifikasi()))
            waktu_perawatan = waktu_perawatan + timedelta(days = jadwal_perawatan.get_frekuensi_perawatan())
            jadwal_perawatan.set_waktu_perawatan(waktu_perawatan) # update waktu_perawatan yang sudah dihitung
        conn.commit()
        conn.close()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())

    def ubah_data_satu_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan_lama: JadwalPerawatan, jadwal_perawatan_baru: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT last_group_id FROM groupJadwalPerawatan;")
        group_id = cursor.fetchone()[0]+1
        cursor.execute("UPDATE groupJadwalPerawatan SET last_group_id = ?;", (group_id,))
        cursor.execute("UPDATE dataJadwalPerawatan SET group_id = ?, frekuensi_perawatan = ?, waktu_perawatan = ?, jenis_perawatan = ?, pilihan_notifikasi = ? WHERE jenis_tanaman = ? AND index_tanaman = ? AND group_id = ? AND waktu_perawatan = ? AND jenis_perawatan = ?;", (group_id, jadwal_perawatan_baru.get_frekuensi_perawatan(), jadwal_perawatan_baru.get_waktu_perawatan(), jadwal_perawatan_baru.get_jenis_perawatan(), jadwal_perawatan_baru.get_pilihan_notifikasi(), jenis_tanaman, index_tanaman, jadwal_perawatan_lama.get_group_id(), jadwal_perawatan_lama.get_waktu_perawatan(), jadwal_perawatan_lama.get_jenis_perawatan()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        conn.close()
    
    def ubah_data_group_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan_baru: JadwalPerawatan):
        self.hapus_data_group_jadwal_perawatan(jadwal_perawatan_baru.get_group_id())
        self.tambah_data_group_jadwal_perawatan(jenis_tanaman, index_tanaman, jadwal_perawatan_baru)
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())

    def hapus_data_satu_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataJadwalPerawatan WHERE jenis_tanaman = ? AND index_tanaman = ? AND group_id = ? AND waktu_perawatan = ? AND jenis_perawatan = ?;", (jenis_tanaman, index_tanaman, jadwal_perawatan.get_group_id(), jadwal_perawatan.get_waktu_perawatan(), jadwal_perawatan.get_jenis_perawatan()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        conn.close()
    
    def hapus_data_group_jadwal_perawatan(self, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataJadwalPerawatan WHERE group_id = ?;", (jadwal_perawatan.get_group_id(),))
        conn.commit()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        conn.close()

# jadwal_perawatan = JadwalPerawatanController()
# jadwal_perawatan1 = JadwalPerawatan(3, 5, "07:00", "07:00", True)
# jadwal_perawatan.tambah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan1)
# jadwal_perawatan2 = JadwalPerawatan(2, 4, "08:00", "08:00", False)
# jadwal_perawatan.ubah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan2)
# jadwal_perawatan.hapus_data_jadwal_perawatan("JERUK", 2)