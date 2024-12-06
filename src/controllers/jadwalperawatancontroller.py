import sqlite3
from jadwalperawatan import JadwalPerawatan 
from datetime import datetime, timedelta
class JadwalPerawatanController:
    def __init__(self):
        self.conn = sqlite3.connect("tunaz.db")
        self.cursor = self.conn.cursor()

    def lihatsemua(self):
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataJadwalPerawatan;")
        print(cursor.fetchall())
        conn.close()

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

    # I.S. frekuensi_penyiraman dan waktu_penyiraman tanaman terdefinisi, tidak ada jadwal_penyiraman pada bulan yang ingin ditampilkan di kalender.
    # F.S. Jadwal penyiraman untuk setiap tanaman telah dibuat berdasarkan frekuensi dan waktu penyiraman untuk bulan yang diminta.
    # Algoritma:
    # CREATE TEMPORARY TABLE JadwalPenyiraman ( 
    #     id_tanaman INT NOT NULL, 
    #     tanggal_penyiraman DATE NOT NULL);
    # CREATE TEMPORARY TABLE TempJadwalPerawatan AS
    # SELECT *
    # FROM DataJadwalPerawatan 
    # WHERE waktu_tanam >= {bulan_tahun_kalender} 
    # FOR jadwal in TempJadwalPerawatan DO
    #     SET selisih_hari ={bulan_tahun_kalender} - jadwal.waktu_penyiraman
    #     SET tanggal_penyiraman = jadwal.waktu_penyiraman + selisih_hari - selisih_hari %   
    #     jadwal.frekuensi_penyiraman
    #     WHILE tanggal_penyiraman IS within bulan_tahun_kalender DO
    #         INSERT INTO JadwalPenyiraman (index_tanaman, tanggal_penyiraman)
    #         VALUES (jadwal.index_tanaman, tanggal_penyiraman);
    #         tanggal_penyiraman = tanggal_penyiraman + frekuensi_penyiraman

    def susun_jadwal_penyiraman(self, bulan_tahun_kalender: str):
        bulan_tahun_kalender = datetime(2024, 12, 1)
        conn = sqlite3.connect("tunaz.db")
        cursor = conn.cursor() 
        cursor.execute("CREATE TEMPORARY TABLE IF NOT EXISTS JadwalPenyiraman (id_tanaman INT NOT NULL, tanggal_penyiraman DATE NOT NULL);")
        cursor.execute("CREATE TEMPORARY TABLE IF NOT EXISTS TempJadwalPerawatan AS SELECT * FROM DataJadwalPerawatan;")
        cursor.execute("SELECT * FROM TempJadwalPerawatan;")
        jadwal_perawatan = cursor.fetchall()
        for jadwal in jadwal_perawatan:
            waktu_siram = datetime.strptime(jadwal[5], "%Y-%m-%d")
            selisih_hari = (bulan_tahun_kalender - waktu_siram).days
            tanggal_penyiraman = waktu_siram + timedelta(days=selisih_hari - (selisih_hari % jadwal[3]))
            while tanggal_penyiraman.month == bulan_tahun_kalender.month:
                output_tanggal = tanggal_penyiraman.strftime("%Y-%m-%d")
                id_tanaman = jadwal[2]
                cursor.execute("INSERT INTO JadwalPenyiraman (id_tanaman, tanggal_penyiraman) VALUES (?,?);", (id_tanaman, output_tanggal))
                tanggal_penyiraman = tanggal_penyiraman + timedelta(days = jadwal[3])
        conn.commit()
        cursor.execute("SELECT * FROM JadwalPenyiraman;")
        print(cursor.fetchall())
        conn.close()

    def susun_jadwal_pemupukan():
        pass #soon

jadwal_perawatan = JadwalPerawatanController()
jadwal_perawatan1 = JadwalPerawatan(3, 5, "2024-12-04", "2024-12-04", True)
# jadwal_perawatan.tambah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan1)
# jadwal_perawatan2 = JadwalPerawatan(2, 4, "08:00", "08:00", False)
# jadwal_perawatan.ubah_data_jadwal_perawatan("JERUK", 2, jadwal_perawatan2)
# jadwal_perawatan.hapus_data_jadwal_perawatan("JERUK", 2)
# jadwal_perawatan.lihatsemua()
jadwal_perawatan.susun_jadwal_penyiraman("2024-12-01")