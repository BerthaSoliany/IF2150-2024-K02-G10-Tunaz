import sqlite3

def init_db():
    conn = sqlite3.connect("src/database/tunaz.db")
    cursor = conn.cursor()

    # Tabel Tanaman
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tanaman (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        icon_tanaman TEXT,
        UNIQUE (index_tanaman, jenis_tanaman)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jenisTracker (
        jenis_tanaman VARCHAR(25) NOT NULL,
        last_tanaman_index INTEGER
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
        ON DELETE CASCADE
        ON UPDATE CASCADE
    )
    """)

    # Tabel DataPertumbuhanTanaman (status_tanaman, tinggi_tanaman, tanggal_catatan, kondisi_daun)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dataPertumbuhanTanaman (
        id_pertumbuhan INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        status_tanaman VARCHAR(25) NOT NULL,
        tinggi_tanaman REAL NOT NULL,
        tanggal_catatan TEXT NOT NULL,
        kondisi_daun VARCHAR(25),
        UNIQUE (jenis_tanaman, index_tanaman, tanggal_catatan),
        FOREIGN KEY (index_tanaman, jenis_tanaman) REFERENCES tanaman (index_tanaman, jenis_tanaman)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    )
    """)

    # Tabel DataJadwalPerawatan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dataJadwalPerawatan (
        id_perawatan INTEGER PRIMARY KEY AUTOINCREMENT,
        jenis_tanaman VARCHAR(25) NOT NULL,
        index_tanaman INTEGER NOT NULL,
        group_id INTEGER,
        frekuensi_perawatan INTEGER, 
        waktu_perawatan TEXT NOT NULL, 
        jenis_perawatan VARCHAR(25),
        pilihan_notifikasi BOOLEAN DEFAULT TRUE,
        FOREIGN KEY (index_tanaman, jenis_tanaman) REFERENCES tanaman (index_tanaman, jenis_tanaman)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groupJadwalPerawatan (
        last_group_id INTEGER
    )
    """)
    cursor.execute("INSERT INTO groupJadwalPerawatan (last_group_id) VALUES (0)")
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    
    init_db()
    print("Database initialized")
