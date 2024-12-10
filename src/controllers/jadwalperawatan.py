class JadwalPerawatan:
    def __init__(self, group_id: int, frekuensi_perawatan: int, waktu_perawatan: str, jenis_perawatan: str, pilihan_notifikasi: bool):
        self.group_id = group_id
        self.frekuensi_perawatan = frekuensi_perawatan
        self.waktu_perawatan = waktu_perawatan
        self.jenis_perawatan = jenis_perawatan
        self.pilihan_notifikasi = pilihan_notifikasi

    def get_group_id(self):
        return self.group_id
    
    def get_frekuensi_perawatan(self):
        return self.frekuensi_perawatan

    def get_waktu_perawatan(self):
        return self.waktu_perawatan
    
    def get_jenis_perawatan(self):
        return self.jenis_perawatan
    
    def get_pilihan_notifikasi(self):
        return self.pilihan_notifikasi
    
    def set_group_id(self, group_id):
        self.group_id = group_id

    def set_frekuensi_perawatan(self, frekuensi_perawatan):
        self.frekuensi_perawatan = frekuensi_perawatan

    def set_waktu_perawatan(self, waktu_perawatan):
        self.waktu_perawatan = waktu_perawatan

    def set_jenis_perawatan(self, jenis_perawatan):
        self.jenis_perawatan = jenis_perawatan
    
    def set_pilihan_notifikasi(self, pilihan_notifikasi):
        self.pilihan_notifikasi = pilihan_notifikasi
    
    def hapus_group_id(self):
        self.group_id = None
        
    def hapus_frekuensi_perawatan(self):
        self.frekuensi_perawatan = None
    
    def hapus_waktu_perawatan(self):
        self.waktu_perawatan = None
    
    def hapus_jenis_perawatan(self):
        self.jenis_perawatan = None
    
    def hapus_pilihan_notifikasi(self):
        self.pilihan_notifikasi = None
