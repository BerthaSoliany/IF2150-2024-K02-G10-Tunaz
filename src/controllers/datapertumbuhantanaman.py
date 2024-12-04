class DataPertumbuhanTanaman: 
    def __init__(self, status_tanaman: str, tinggi_tanaman: float, tanggal_catatan: str, kondisi_daun: str):
        self.status_tanaman = status_tanaman
        self.tinggi_tanaman = tinggi_tanaman
        self.tanggal_catatan = tanggal_catatan
        self.kondisi_daun = kondisi_daun

    def get_status_tanaman(self):
        return self.status_tanaman
    
    def get_tinggi_tanaman(self):
        return self.tinggi_tanaman
    
    def get_tanggal_catatan(self):
        return self.tanggal_catatan
    
    def get_kondisi_daun(self):
        return self.kondisi_daun
    
    def set_status_tanaman(self, status_tanaman):
        self.status_tanaman = status_tanaman

    def set_tinggi_tanaman(self, tinggi_tanaman):
        self.tinggi_tanaman = tinggi_tanaman
    
    def set_tanggal_catatan(self, tanggal_catatan):
        self.tanggal_catatan = tanggal_catatan
    
    def set_kondisi_daun(self, kondisi_daun):
        self.kondisi_daun = kondisi_daun
    
    def hapus_status_tanaman(self):
        self.status_tanaman = None
    
    def hapus_tinggi_tanaman(self):
        self.tinggi_tanaman = None

    def hapus_tanggal_catatan(self):
        self.tanggal_catatan = None

    def hapus_kondisi_daun(self):
        self.kondisi_daun = None
