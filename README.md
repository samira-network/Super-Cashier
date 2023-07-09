# Super Cashier Project 
Ini adalah program yang menjalankan perhitungan kasir yag modern dengan tingkat akurasi tinggi dan mudah digunakan dalam situasi tertentu. Bahasa pemrograma yang digunakan yaitu bahasa python. 

# Latar Belakang 
Pada sebuah toko Otomotif di daerah Batam yaitu toko Nadim masih menerapkan sistem tatap muka selama transaksi namun seiring perkembangan zaman sistem IoT hedak diterapkan maka pemiliki toko otomatif tersebut memiliki konsep toko dengan melakukan pembelian jarak jauh menggunakan aplikasi yang sudah terintegrasi maka pemilik toko memutuskan untuk melakukan perubahan mengadapatasi self-service cashier oriented  

# Tujuan pengerjaan Project 
Saya telah membuat sistem kasir sederhana yang memenuhi persyaratan berikut:

-Sistem ini memungkinkan pengguna untuk membuat inputan seperti nama pesanan, jumlah pesanan, dan harga pesanan.
-Pengguna juga dapat melakukan pengecekan pesanan dengan opsi untuk menambahkan, mengganti, atau membatalkan pesanan.
-Sistem juga memungkinkan pengguna untuk mengoreksi pesanan dengan menghapus satu baris atau lebih berdasarkan indeks.
-Jika pengguna ingin membatalkan atau memesan ulang semua pesanan, sistem memungkinkan pengguna untuk menghapus semua pesanan.
-Pengguna dapat melihat pesanan yang telah dibuat.
-Sistem juga melakukan pengecekan diskon yang didapatkan oleh pengguna.

# Flow chart program 

<img width="1364" alt="Flowchart Super Cashier" src="https://github.com/samira-network/Super-Cashier/assets/137299240/72f92849-bc2c-4c93-9846-feba49bb58ed">

# Penjelasan Program 

Tabulate : ini digunakan untuk menghasilkan penyimpanan data dalam bentuk table

Code ini menggunakan class yang mana menampung isi class dictionaries kosong, digunakan untuk menampung item, quantity dan price per item 
memasukan ataupun menambah pesanan dengan fungsi dan dipadukan dengan branching. Jika berhasil menambahkan akan muncul "Added item to the tansaction" jika tidak  "Item xx is already added. To update the quantity, use the 'update' option." . Maka lakukan update 
![1 class](https://github.com/samira-network/Super-Cashier/assets/137299240/3caf81f4-d16b-4e79-8aad-063d1f2f6640)

Update :

Metode ini (`update_item_quantity` dan `update_item_price` update_item_price ) memperbarui jumlah atau harga item tertentu dalam transaksi. Memeriksa apakah item tersebut ada dalam daftar item transaksi. Jika barang ditemukan, mereka memperbarui jumlah atau harga yang sesuai dengan nilai baru yang diberikan.
Jika item tidak ditemukan, maka menampilkan pesan yang menunjukkan bahwa item tersebut tidak ditambahkan ke transaksi.
![update 2](https://github.com/samira-network/Super-Cashier/assets/137299240/674c3370-71e1-4a96-9a00-ec5dfd795997)

Delete item, calculate total price
Metode delete digunakan untuk menghapun item pesanan namun tidak menghapus seluruh item yang masih ingin dipesan. Setelah menghapus item, pesan konfirmasi bahwa item yg dihapus telah diperbarui dan hanya menampilkan yang tersimpan transaksi 

![3 delete calculate](https://github.com/samira-network/Super-Cashier/assets/137299240/e94e48e1-00a2-4117-8408-7de8ed93b958)

Apply discount 

Melakukan perhitungan diskon berdasarkan requirement

![4 appl diskon](https://github.com/samira-network/Super-Cashier/assets/137299240/2be37ca4-a726-42ae-9363-1dd4196c9d51)

Check dan Reset

Melakukan check detail pesanan apakah pesanan sudah masuk semua dan melakukan reset untuk membatakan seluruh pesanan
![5555](https://github.com/samira-network/Super-Cashier/assets/137299240/e5e77022-3a21-43d2-97f9-8ee594beb4c1)


# Test Code

1. Melakukan memasukan item dan check detail item yag sudah dimasukan 
![ccceekScreenshot 2023-07-09 161913](https://github.com/samira-network/Super-Cashier/assets/137299240/1a57fe7b-e439-4978-a9dd-e2fda121354b)

2. melakukan delete item yang tidak diinginkan
![delete pasta](https://github.com/samira-network/Super-Cashier/assets/137299240/90bff3ce-52c3-4f98-82fc-6f88505b397e)

4. Melakukan cancel semua order
![cancel](https://github.com/samira-network/Super-Cashier/assets/137299240/e250fd09-e244-4267-b547-78cf206a967e)

5. Melakuka perhitungan akhir
![image](https://github.com/samira-network/Super-Cashier/assets/137299240/accccef9-b765-4fd3-bc2e-c1a23b1cf319)

# Kesimpulan 
- User dapat melakukan menambahkan item 
- user dapat menambahkan banyak item 
- program mampu menjalankan perintah perhitungan total harga per item saat melakkan check detail transaksi
- user mampu melakukan update pada keranjang belanja 
- user bisa menghapus item yang sudah masuk ke keranjang tanpa menghapuskan seluruh item di keranjang 
- user bisa membatalkan seluruh belanjaannya dan secara otomatis di-reset transaksiya
- pemrograman mampu menjalankan perintah ketika total harga mendapatkan diskon dari seluruh belanjaan dan menghitung harga setelah diskon 

# Saran 
-Program tidak mampu mendeteksi apakah item itu tersedia atau tidak di toko sebaiknya dibuat data list untuk item yg available beserta harga 
-Program menggantungkan hanya pada terminal yang berjalan di platform sebaiknya integrasi menggunakan Web supaya user friendly 
-Program tidak mampu menunjukan katalog yang tersedia di toko online sebaiknya dibuat item apa saja yang dijual 

# Penjelasan video 

https://youtu.be/v7HxK5Fpz8Av
