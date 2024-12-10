from src.controllers.datainformasitanaman import DataInformasiTanaman
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
from src.controllers.jadwalperawatan import JadwalPerawatan

class Tanaman:
    def __init__(self, jenis_tanaman: str, index_tanaman: int, data_informasi_tanaman: DataInformasiTanaman, data_pertumbuhan_tanaman: DataPertumbuhanTanaman, data_jadwal_perawatan: JadwalPerawatan):
        self.jenis_tanaman = jenis_tanaman
        self.index_tanaman = index_tanaman
        self.data_informasi_tanaman = data_informasi_tanaman
        self.data_pertumbuhan_tanaman = data_pertumbuhan_tanaman
        self.data_jadwal_perawatan = data_jadwal_perawatan
        
    def get_jenis(self):
        return self.jenis_tanaman

    def get_index(self):
        return self.index_tanaman
    
    def get_data_informasi_tanaman(self):
        return self.data_informasi_tanaman
    
    def get_data_pertumbuhan_tanaman(self):
        return self.data_pertumbuhan_tanaman
    
    def get_data_jadwal_perawatan(self):
        return self.data_jadwal_perawatan
    
    def set_jenis(self, jenis_tanaman):
        self.jenis_tanaman = jenis_tanaman

    def set_index(self, index_tanaman):
        self.index_tanaman = index_tanaman

    def set_data_informasi_tanaman(self, data_informasi_tanaman):
        self.data_informasi_tanaman = data_informasi_tanaman

    def set_data_pertumbuhan_tanaman(self, data_pertumbuhan_tanaman):
        self.data_pertumbuhan_tanaman = data_pertumbuhan_tanaman

    def set_data_jadwal_perawatan(self, data_jadwal_perawatan):
        self.data_jadwal_perawatan = data_jadwal_perawatan