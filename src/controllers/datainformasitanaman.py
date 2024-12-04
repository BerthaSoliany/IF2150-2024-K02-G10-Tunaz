class DataInformasiTanaman:
    def __init__(self, waktu_tanam: str, kebutuhan_perawatan: str):
        self.waktu_tanam = waktu_tanam
        self.kebutuhan_perawatan = kebutuhan_perawatan

    def get_waktu_tanam(self):
        return self.waktu_tanam
    
    def get_kebutuhan_perawatan(self):
        return self.kebutuhan_perawatan
    
    def set_waktu_tanam(self, waktu_tanam):
        self.waktu_tanam = waktu_tanam

    def set_kebutuhan_perawatan(self, kebutuhan_perawatan):
        self.kebutuhan_perawatan = kebutuhan_perawatan

    def hapus_waktu_tanam(self):
        self.waktu_tanam = None
    
    def hapus_kebutuhan_perawatan(self):
        self.kebutuhan_perawatan = None