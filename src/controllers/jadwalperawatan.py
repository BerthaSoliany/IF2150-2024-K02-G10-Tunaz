class JadwalPerawatan:
    def __init__(self, frekuensi_penyiraman: int, frekuensi_pemupukan: int, waktu_penyiraman: str, waktu_pemupukan: str, pilihan_notifikasi: bool):
        self.frekuensi_penyiraman = frekuensi_penyiraman
        self.frekuensi_pemupukan = frekuensi_pemupukan
        self.waktu_penyiraman = waktu_penyiraman
        self.waktu_pemupukan = waktu_pemupukan
        self.pilihan_notifikasi = pilihan_notifikasi

    def get_frekuensi_penyiraman(self):
        return self.frekuensi_penyiraman
    
    def get_frekuensi_pemupukan(self):
        return self.frekuensi_pemupukan
    
    def get_waktu_penyiraman(self):
        return self.waktu_penyiraman
    
    def get_waktu_pemupukan(self):
        return self.waktu_pemupukan
    
    def get_pilihan_notifikasi(self):
        return self.pilihan_notifikasi
    
    def set_frekuensi_penyiraman(self, frekuensi_penyiraman):
        self.frekuensi_penyiraman = frekuensi_penyiraman

    def set_frekuensi_pemupukan(self, frekuensi_pemupukan):
        self.frekuensi_pemupukan = frekuensi_pemupukan

    def set_waktu_penyiraman(self, waktu_penyiraman):
        self.waktu_penyiraman = waktu_penyiraman

    def set_waktu_pemupukan(self, waktu_pemupukan):
        self.waktu_pemupukan = waktu_pemupukan
    
    def set_pilihan_notifikasi(self, pilihan_notifikasi):
        self.pilihan_notifikasi = pilihan_notifikasi
    
    def hapus_frekuensi_penyiraman(self):
        self.frekuensi_penyiraman = None
    
    def hapus_frekuensi_pemupukan(self):
        self.frekuensi_pemupukan = None
    
    def hapus_waktu_penyiraman(self):
        self.waktu_penyiraman = None
    
    def hapus_waktu_pemupukan(self):
        self.waktu_pemupukan = None
    
    def hapus_pilihan_notifikasi(self):
        self.pilihan_notifikasi = None
