import sqlite3

def init_db():
    conn = sqlite3.connect("tunaz.db")
    cursor = conn.cursor()

    # Tabel Tanaman
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tanaman (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        UNIQUE (index_tanaman, jenis_tanaman)
    )
    """)

    # Tabel DataInformasiTanaman
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dataInformasiTanaman (
        id_informasi INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        waktu_tanam TEXT,
        kebutuhan_perawatan VARCHAR(200),
        FOREIGN KEY (index_tanaman, jenis_tanaman) REFERENCES tanaman (index_tanaman, jenis_tanaman)
    )
    """)

    # Tabel DataPertumbuhanTanaman (status_tanaman, tinggi_tanaman, tanggal_catatan, kondisi_daun)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dataPertumbuhanTanaman (
        id_pertumbuhan INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        status_tanaman VARCHAR(25) NOT NULL,
        tinggi_tanaman REAL,
        tanggal_catatan TEXT,
        kondisi_daun VARCHAR(25),
        FOREIGN KEY (index_tanaman, jenis_tanaman) REFERENCES tanaman (index_tanaman, jenis_tanaman)
    )
    """)

    # Tabel DataJadwalPerawatan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dataJadwalPerawatan (
        id_perawatan INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        frekuensi_penyiraman INTEGER,
        frekuensi_pemupukan INTEGER,
        waktu_penyiraman TEXT, 
        waktu_pemupukan TEXT,
        pilihan_notifikasi BOOLEAN DEFAULT TRUE,
        FOREIGN KEY (index_tanaman, jenis_tanaman) REFERENCES tanaman (index_tanaman, jenis_tanaman)
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
