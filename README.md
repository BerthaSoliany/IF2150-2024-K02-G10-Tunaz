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

### Modul 1: List Informasi Tanaman
List informasi tanaman menampilkan jenis tanaman, indeks tanaman, informasi perawatan tanaman, dan umur tanaman dari data tanaman.

### Modul 2: Kalender Perawatan
Kalender perawatan menampilkan kalender yang berisi jadwal penyiraman serta pemupukan sesuai data perawatan tanaman yang dimasukkan pengguna.

### Modul 3: Grafik Pertumbuhan Tanaman
Grafik pertumbuhan tanaman menampilkan tinggi tanaman dari waktu ke waktu berdasarkan data pertumbuhan tanaman.

### Modul 4: Notifikasi
Notifikasi muncul ketika terdapat jadwal perawatan tanaman sebagai pengingat bagi pengguna untuk melakukan perawatan.

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
- [Tabel Tracker Jenis](#tabel-tracker-jenis)
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

### Tabel Tracker Jenis
Tabel ini menyimpan indeks terakhir dari suatu jenis tanaman.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| jenis_tanaman | varchar(25) | - |
| last_tanaman_index | integer | - |

### Tabel Data Informasi Tanaman
Tabel ini menyimpan data informasi suatu tanaman untuk list informasi tanaman.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| id_informasi | integer | Primary Key, auto increment |
| jenis_tanaman | varchar(25) | Foreign Key dari Tabel Tanaman |
| index_tanaman | integer | Foreign Key dari Tabel Tanaman |
| waktu_tanam | text | - |
| kebutuhan_perawatan | varchar(200) | - |

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

### Tabel Grup Jadwal Perawatan
Tabel ini menyimpan indeks terakhir dari grup tanaman, yaitu kelompok tanaman yang memiliki jadwal perawatan pada suatu rentang waktu tertentu.
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| last_group_id | integer | - |
