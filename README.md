# Tunaz: Tugas Besar IF2150 Rekayasa Perangkat Lunak
![logo1](https://github.com/user-attachments/assets/f2fbcae9-f95b-4962-9288-dcf4b0097f09)

## Daftar Isi
1. [Tentang Tunaz](#tentang-tunaz)
2. [Contributors](#contributors)
3. [Cara Menjalankan](#cara-menjalankan)
4. [Daftar Modul](#daftar-modul)
5. [Tabel Basis Data](#tabel-basis-data)

## Tentang Tunaz
Tumbuhan Azul atau Tunaz adalah P/L manajemen taman atau kebun berbasis desktop yang membantu pengguna merencanakan, merawat, dan mengelola berbagai jenis tanaman serta melacak pertumbuhan tanaman dari waktu ke waktu. P/L ini tidak memerlukan akses internet sehingga P/L dapat diakses kapan saja dan di mana saja. Pengguna dapat memasukkan data tanaman, data perawatan berupa jadwal penyiraman serta pemupukan, dan data pertumbuhan tanaman terdiri atas tinggi tanaman, kondisi daun, dan informasi pertumbuhan tanaman lainnya yang ingin dimasukkan oleh pengguna. Semua data ini, dapat disesuaikan oleh pengguna dengan cara memperbaharui, menghapus, atau menambahkan informasi. P/L mengolah data yang dimasukkan pengguna menjadi tiga fitur utama dari Tunaz, yakni list informasi tanaman, kalender perawatan yang dilengkapi dengan notifikasi jadwal perawatan, serta grafik pertumbuhan tanaman. 

## Contributors
| NIM | Nama |
|-----|------|
| Clarissa Nethania Tambunan | 13523016 |
| Bertha Soliany Frandi | 13523026 |
| Aloisius Adrian Stevan Gunawan | 13523054 |
| Michael Alexander Angkawijaya | 13523102 |
| Naomi Risaka Sitorus | 13523122 |

## Cara Menjalankan
1. Clone repository ini dengan menjalankan perintah di bawah ini pada terminal IDE yang mendukung Python serta virtual environment:
   ```sh
   git clone https://github.com/BerthaSoliany/IF2150-2024-K02-G10-Tunaz.git

2. Buka folder hasil clone di IDE.

3. Buat virtual environment:
   ```sh
   python -m venv venv
   
4. Aktivasi virtual environment yang sudah dibuat:<br>
   Untuk Windows: ```venv\Scripts\activate```<br> 
   Untuk Unix-like Shell (bash): ```source venv/bin/activate```
> [!NOTE]
> Sesuaikan kembali path dari activate sesuai dengan venv masing-masing

5. Instal dependencies:
    ```sh
    pip install -r requirements.txt

6. Jalankan perangkat lunak:
    ```sh
    flet run app.py

## Daftar Modul
- [Modul 1: List Informasi Tanaman](#modul-1-list-informasi-tanaman)
- [Modul 2: Kalender Perawatan](#modul-2-kalender-perawatan)
- [Modul 3: Grafik Pertumbuhan Tanaman](#modul-3-grafik-pertumbuhan-tanaman)
- [Modul 4: Notifikasi](#modul-4-notifikasi)
- [Pembagian Tugas](#pembagian-tugas)

### Modul 1: Informasi Tanaman
Informasi tanaman menampilkan daftar jenis tanaman, indeks tanaman, informasi perawatan tanaman, dan umur tanaman dari data tanaman.
![page_info_tanaman](https://github.com/user-attachments/assets/6b4156eb-3c92-4665-b9c6-61c38260fb53)

### Modul 2: Kalender Perawatan
Kalender perawatan menampilkan kalender yang berisi jadwal penyiraman serta pemupukan sesuai data perawatan tanaman yang dimasukkan pengguna.
![page_kalender_perawatan](https://github.com/user-attachments/assets/268d4021-aae0-4cee-a6d9-367a5fa79d79)

### Modul 3: Grafik Pertumbuhan Tanaman
Grafik pertumbuhan tanaman menampilkan tinggi tanaman dari waktu ke waktu berdasarkan data pertumbuhan tanaman.
![page_grafik_pertumbuhan](https://github.com/user-attachments/assets/3ebea800-809f-4c61-84e3-9aa0a3b195d0)

### Modul 4: Notifikasi
Notifikasi muncul ketika terdapat jadwal perawatan tanaman sebagai pengingat bagi pengguna untuk melakukan perawatan.
![notification](https://github.com/user-attachments/assets/bdaedd27-db75-46b8-9fc5-f23a8ff7d817)

### Pembagian Tugas
| Tugas | NIM |
|-------|-----|
| List Informasi Tanaman | 13523122 |
| Kalender Perawatan | 13523026 |
| Grafik Pertumbuhan Tanaman | 13523026 |
| Notifikasi | 13523016 |
| Komponen | 13523054 |
| Kontroler | 13523102 |

## Tabel Basis Data
- [Tabel Tanaman](#tabel-tanaman)
- [Tabel Data Informasi Tanaman](#tabel-data-informasi-tanaman)
- [Tabel Data Pertumbuhan Tanaman](#tabel-data-informasi-tanaman)
- [Tabel Data Jadwal Perawatan](#tabel-data-jadwal-perawatan)
- [Tabel Grup Jadwal Perawatan](#tabel-grup-jadwal-perawatan)

### Tabel Tanaman
Tabel ini menyimpan informasi dasar mengenai suatu tanaman.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| id | integer | Primary Key, auto increment |
| jenis_tanaman | varchar(25) | - |
| index_tanaman | integer | - |
| icon_tanaman | text | - |
<br>
<img width="514" alt="sample_tanaman_database_table" src="https://github.com/user-attachments/assets/437af802-1ac3-4044-83a1-ff3ca0af560c" />

### Tabel Data Informasi Tanaman
Tabel ini menyimpan data informasi suatu tanaman untuk list informasi tanaman.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| id_informasi | integer | Primary Key, auto increment |
| jenis_tanaman | varchar(25) | Foreign Key dari Tabel Tanaman |
| index_tanaman | integer | Foreign Key dari Tabel Tanaman |
| waktu_tanam | text | - |
| kebutuhan_perawatan | varchar(200) | - |
<img width="622" alt="sample_datainformasitanaman_database_table" src="https://github.com/user-attachments/assets/b26dce2c-ddb1-47a3-ad13-e227b15348ad" />


### Tabel Data Pertumbuhan Tanaman
Tabel ini menyimpan data pertumbuhan suatu tanaman untuk grafik pertumbuhan tanaman.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| id_pertumbuhan | integer | Primary Key, auto increment |
| jenis_tanaman | varchar(25) | Foreign Key dari Tabel Tanaman |
| index_tanaman | integer | Foreign Key dari Tabel Tanaman |
| status_tanaman | varchar(25) | - |
| tinggi_tanaman| real | - |
| tanggal_catatan | text | - |
| kondisi_daun | varchar(25) | - |
<img width="806" alt="sample_datapertumbuhantanaman_database_table" src="https://github.com/user-attachments/assets/49cf4bec-7c49-4572-9840-9bddeb7882dc" />

### Tabel Data Jadwal Perawatan
Tabel ini menyimpan data jadwal perawatan suatu tanaman untuk kalender perawatan.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| id_perawatan | integer | Primary Key, auto increment |
| jenis_tanaman | varchar(25) | Foreign Key dari Tabel Tanaman |
| index_tanaman | integer | Foreign Key dari Tabel Tanaman |
| group_id | integer | - |
| frekuensi_perawatan | integer | - |
| waktu_perawatan | text | - |
| jenis_perawatan | varchar(25) | - |
| pilihan_notifikasi | boolean | default = True |
<img width="803" alt="sample_datajadwalperawatan_database_table" src="https://github.com/user-attachments/assets/c9b9c1dc-5200-42ff-b3f1-f8879ffb1e15" />

**<p align="center">Terima kasih!</p>**
