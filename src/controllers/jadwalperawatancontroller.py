import sqlite3
from src.controllers.jadwalperawatan import JadwalPerawatan 
from datetime import datetime, timedelta, time

class JadwalPerawatanController:

    def tambah_data_satu_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("src/database/tunaz.db")
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
        return group_id

    def tambah_data_group_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan, waktu_akhir_perawatan: str):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT last_group_id FROM groupJadwalPerawatan;")
        group_id = cursor.fetchone()[0]+1
        cursor.execute("UPDATE groupJadwalPerawatan SET last_group_id = ?;", (group_id,))

        waktu_akhir_perawatan = datetime.strptime(waktu_akhir_perawatan, "%Y-%m-%d")
        waktu_perawatan_datetime = datetime.strptime(jadwal_perawatan.get_waktu_perawatan(), "%Y-%m-%d %H:%M:%S")
        waktu_akhir_perawatan = datetime.combine(waktu_akhir_perawatan, waktu_perawatan_datetime.time())
        # waktu_perawatan = waktu_perawatan_datetime.date()
        while waktu_perawatan_datetime <= waktu_akhir_perawatan:
            print("halo")
            print("1", waktu_perawatan_datetime)
            print("2", waktu_akhir_perawatan)
            cursor.execute("INSERT INTO dataJadwalPerawatan (jenis_tanaman, index_tanaman, group_id, frekuensi_perawatan, waktu_perawatan, jenis_perawatan, pilihan_notifikasi) VALUES (?, ?, ?, ?, ?, ?, ?);", (jenis_tanaman, index_tanaman, group_id, jadwal_perawatan.get_frekuensi_perawatan(), jadwal_perawatan.get_waktu_perawatan(), jadwal_perawatan.get_jenis_perawatan(), jadwal_perawatan.get_pilihan_notifikasi()))
            waktu_perawatan_datetime = waktu_perawatan_datetime + timedelta(days = int(jadwal_perawatan.get_frekuensi_perawatan()))
            # waktu_perawatan = waktu_perawatan_datetime.date()
            jadwal_perawatan.set_waktu_perawatan(waktu_perawatan_datetime) # update waktu_perawatan yang sudah dihitung
        conn.commit()
        conn.close()
        return group_id
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())

    def ubah_data_satu_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan_lama: JadwalPerawatan, jadwal_perawatan_baru: JadwalPerawatan):
        # print("jadwal perawatan lama: ", jadwal_perawatan_lama.get_group_id(), jadwal_perawatan_lama.get_waktu_perawatan(), jadwal_perawatan_lama.get_jenis_perawatan(), jadwal_perawatan_lama.get_pilihan_notifikasi(), jadwal_perawatan_lama.get_frekuensi_perawatan())
        # print("jadwal perawatan baru: ", jadwal_perawatan_baru.get_group_id(), jadwal_perawatan_baru.get_waktu_perawatan(), jadwal_perawatan_baru.get_jenis_perawatan(), jadwal_perawatan_baru.get_pilihan_notifikasi(), jadwal_perawatan_baru.get_frekuensi_perawatan())
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT last_group_id FROM groupJadwalPerawatan;")
        group_id = cursor.fetchone()[0]+1
        cursor.execute("UPDATE groupJadwalPerawatan SET last_group_id = ?;", (group_id,))
        cursor.execute("UPDATE dataJadwalPerawatan SET group_id = ?, frekuensi_perawatan = ?, waktu_perawatan = ?, jenis_perawatan = ?, pilihan_notifikasi = ? WHERE jenis_tanaman = ? AND index_tanaman = ? AND group_id = ? AND waktu_perawatan = ? AND jenis_perawatan = ?;", (group_id, jadwal_perawatan_baru.get_frekuensi_perawatan(), jadwal_perawatan_baru.get_waktu_perawatan(), jadwal_perawatan_baru.get_jenis_perawatan(), jadwal_perawatan_baru.get_pilihan_notifikasi(), jenis_tanaman, index_tanaman, jadwal_perawatan_lama.get_group_id(), jadwal_perawatan_lama.get_waktu_perawatan(), jadwal_perawatan_lama.get_jenis_perawatan()))
        conn.commit()
        print("ini dari controller")
        cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        print(cursor.fetchall())
        conn.close()
        return group_id
    
    def ubah_data_group_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan_baru: JadwalPerawatan, waktu_akhir_perawaatan: str):
        self.hapus_data_group_jadwal_perawatan(jadwal_perawatan_baru.get_group_id())
        group_id = self.tambah_data_group_jadwal_perawatan(jenis_tanaman, index_tanaman, jadwal_perawatan_baru, waktu_akhir_perawaatan)
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        return group_id

    def hapus_data_satu_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataJadwalPerawatan WHERE jenis_tanaman = ? AND index_tanaman = ? AND group_id = ? AND waktu_perawatan = ? AND jenis_perawatan = ?;", (jenis_tanaman, index_tanaman, jadwal_perawatan.get_group_id(), jadwal_perawatan.get_waktu_perawatan(), jadwal_perawatan.get_jenis_perawatan()))
        conn.commit()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        conn.close()
    
    def hapus_data_group_jadwal_perawatan(self, group_id):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataJadwalPerawatan WHERE group_id = ?;", (group_id,))
        conn.commit()
        # cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        # print(cursor.fetchall())
        conn.close()

    def get_all_jadwal_perawatan_by_date(self, waktu_perawatan: str):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataJadwalPerawatan WHERE waktu_perawatan LIKE ?;", (waktu_perawatan + '%',))
        data = cursor.fetchall()
        conn.close()
        if(data == None):
            return None
        # if(len(data) == 1):

        data = [list(row) for row in data]
        sorted_data = sorted(data, key=lambda x: x[5].split(" ")[1])
        return sorted_data
    
    def get_all_jadwal_perawatan_by_month(self, waktu_perawatan: str):
        waktu_perawatan = waktu_perawatan.split("-")
        waktu_perawatan = waktu_perawatan[0] + "-" + waktu_perawatan[1]
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataJadwalPerawatan WHERE waktu_perawatan LIKE ?;", (waktu_perawatan + '%',))
        data = cursor.fetchall()
        conn.close()
        if(data == None):
            return None
        data = [list(row) for row in data]
        # sort by date, not time
        sorted_data = sorted(data, key=lambda x: x[5].split(" ")[0])
        return sorted_data

    def get_one_jadwal_perawatan(self, jenis_tanaman: str, index_tanaman: int, jadwal_perawatan: JadwalPerawatan):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataJadwalPerawatan WHERE jenis_tanaman = ? AND index_tanaman = ? AND waktu_perawatan = ? AND jenis_perawatan = ?;", (jenis_tanaman, index_tanaman, jadwal_perawatan.get_waktu_perawatan(), jadwal_perawatan.get_jenis_perawatan()))
        data = cursor.fetchone()
        conn.close()
        return data

    def get_sampai_tanggal_by_group_id(self, group_id: int):
        # get the last date of the group_id
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT waktu_perawatan FROM dataJadwalPerawatan WHERE group_id = ? ORDER BY waktu_perawatan DESC;", (group_id,))
        data = cursor.fetchone()
        conn.close()
        data = data[0].split(" ")[0]
        return data
    
    def get_all_jadwal_perawatan(self):
        conn = sqlite3.connect("src/database/tunaz.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        data = cursor.fetchall()
        print(data)
        conn.close()
        # return data

# jadwal_perawatan = JadwalPerawatanController()
# jadwal_perawatan.get_all_jadwal_perawatan()
# jadwal_perawatan1 = JadwalPerawatan(1, 3, "2024-12-19 07:00:00", "Siram", True)
# jadwal_perawatan.tambah_data_satu_jadwal_perawatan("JERUK", 1, jadwal_perawatan1)
# jadwal_perawatan1 = JadwalPerawatan(3, 5, "07:00", "07:00", True)
# jadwal_perawatan.tambah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan1)
# jadwal_perawatan2 = JadwalPerawatan(2, 4, "08:00", "08:00", False)
# jadwal_perawatan.ubah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan2)
# jadwal_perawatan.hapus_data_jadwal_perawatan("JERUK", 2)