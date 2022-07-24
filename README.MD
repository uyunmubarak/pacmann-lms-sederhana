# Library Management System (LMS) Sederhana

---

**Tujuan Pengerjaan Project**

Membuat sebuah aplikasi manajemen perpustakaan sederhana yang dapat melakukan pendaftaran anggota perpustakaan, pendaftaran buku baru, peminjaman, menampilkan data anggota, buku, dan daftar peminjaman serta melakukan pencarian buku.

**Detail/deskripi task**
1. Membuat fungsi *create_server_connection*, fungsi ini membuat koneksi ke server MySQL.
2. Membuat fungsi *create_database*, fungsi tersebut digunakan untuk membuat database baru.
3. Membuat fungsi *create_connect*, fungsi ini digunakan untuk memodifikasi fungsi create_server_connection untuk terhubung langsung ke database.
4. Membuat fungsi *execute_query*, digunakan untuk mengeksekusi query.
5. Membuat fungsi *read_query*, fungsi ini berfungsi untuk membaca data dari database.
6. Membuat fungsi *main*, yang digunakan untuk menampilkan menu utama dari program.
7. Membuat fungsi *tambah_user*, fungsi ini digunakan untuk menambahkan data anggota perpustakaan ke dalam database.
8. Membuat fungsi *tambah_buku*, fungsi ini berguna untuk menambahkan data buku perpustakaan ke dalam database.
9. Membuat fungsi *pinjam_buku*, fungsi ini digunakan untuk menambahkan data peminjaman buku ke dalam database.
10. Membuat fungsi *tampil_buku* yang digunakan untuk menampilkan daftar buku yang ada di perpustakaan.
11. Membuat fungsi *tampil_user* yang digunakan untuk menampilkan daftar anggota perpustakaan.
12. Membuat fungsi *tampil_peminjam* yang digunakan untuk menampilkan data peminjaman buku.
13. Membuat fungsi *cari_buku*, fungsi ini digunakan untuk melakukan pencarian buku perpustakaan.
14. Membuat fungsi *kembali_buku*, fungsi ini digunakan untuk menghapus data peminjaman buku.

**Cara Running/Penggunaan Program**

Jalankan file main.py di jupyterLab dengan menggunakan perintah `python main.py`. Setelah itu menu utama dari program akan muncul, pilih nomor tugas sesuai kebutuhan anda.

**Hasil Test Case**
1. Pendaftaran user baru
<img src="img/pendaftaran_user_baru.png" width="1000"/>

2. Pendaftaran buku baru
<img src="img/pendaftaran_buku_baru.png" width="1000"/>

3. Menampilkan data user
<img src="img/tampil_daftar_user.png" width="1000"/>

4. Menampilkan daftar buku
<img src="img/tampil_daftar_buku.png" width="1000"/>

5. Peminjaman buku
<img src="img/peminjaman.png" width="1000"/>

6. Menampilkan daftar peminjam
<img src="img/tampil_daftar_peminjam.png" width="1000"/>

7. Menampilkan daftar buku (pada bagian buku *supernova* jumlah stocknya berkurang setelah dilakukan peminjaman)
<img src="img/stok_buku_berkurang_setelah_dipinjam.png" width="1000"/>

8. Menampilkan pengembalian buku
<img src="img/pengembalian.png" width="1000"/>

9. Menampilkan daftar buku (pada bagian buku *supernova* jumlah stocknya bertambah setelah dilakukan pengembalian)
<img src="img/stok_bertambah_setelah_pengembalian.png" width="1000"/>

10. Menampilkan pencarian buku
<img src="img/pencarian_nama_buku.png" width="1000"/>

11. Keluar dari program
<img src="img/exit.png" width="1000"/>

**Saran/Perbaikan**
1. Program dibuat lebih banyak *exception handling* untuk menghindari adanya human error saat penginputan.
2. Fungsi-fungsi yang ada pada program sebaiknya di buat pada file python yang berbeda untuk mempermudah menemukan kesalahan jika terjadi error.
3. Program alangkah baiknya di buat menggunakan konsep OOP.
