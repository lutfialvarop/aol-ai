# Hasil dan Temuan

## Berdasarkan laporan yang diberikan, berikut adalah hasil dan temuan utamanya:
### Permasalahan yang Diatasi:
Permasalahan pengelolaan sampah di Indonesia masih menjadi tantangan besar. Tercatat bahwa dari 31,9 juta ton timbunan sampah nasional, hanya 63,3% yang dapat terkelola, menyisakan 11,3 juta ton atau 35,67% yang belum tertangani dengan baik per 24 Juli 2024. Hal ini menunjukkan rendahnya efisiensi pengelolaan sampah, terutama dalam proses pemilahan sejak dari sumbernya.
### Solusi yang Dikembangkan:
Sebuah sistem pemilah sampah otomatis berbasis kecerdasan buatan (AI) yang terintegrasi dengan perangkat mekanik berupa katup servo telah dikembangkan. Sistem ini dirancang untuk membantu proses pemilahan sampah secara efisien, dengan kemampuan membedakan sampah organik dan anorganik secara otomatis.

## Komponen Teknologi:
- Model AI: Menggunakan teknologi computer vision  untuk mendeteksi dan mengklasifikasikan sampah menjadi dua kategori utama, yaitu organik dan anorganik. Proses ini mengandalkan deep learning, khususnya algoritma convolutional neural network (CNN). Model AI berasal dari pre-trained model di platform Hugging Face, kemudian dilatih ulang (retraining atau fine-tuning) menggunakan framework PyTorch  atau TensorFlow.
- Perangkat Keras: Meliputi modul ESP32-CAM sebagai perangkat akuisisi gambar , mikrokontroler ESP32 untuk menerima hasil klasifikasi dan mengendalikan pergerakan katup servo , dan katup servo sebagai katup mekanik yang membuka jalur pembuangan sampah sesuai kategori yang dikenali.
- Komunikasi: Hasil klasifikasi dari model AI akan diteruskan melalui protokol HTTP menggunakan komunikasi berbasis IP untuk mengaktifkan katup servo.
- Integrasi: Seluruh komponen diintegrasikan menggunakan Printed Circuit Board (PCB) untuk menjaga keteraturan, efisiensi, serta menghasilkan alat yang lebih ringkas, stabil, dan mudah diproduksi ulang.
- Antarmuka Pengguna: Antarmuka berbasis web dikembangkan menggunakan Streamlit untuk memudahkan visualisasi dan interaksi pengguna secara real-time.

## Manfaat yang Diprediksi (Luaran):
- Prototipe Alat Pemilah Sampah Otomatis: Tersedianya prototipe fungsional berupa alat pemilah sampah berbasis AI dengan mekanisme katup servo.
- Peningkatan Proporsi Sampah Terpilah: Diharapkan terjadi peningkatan volume sampah yang telah dipilah sejak dari sumber, yang akan meningkatkan efektivitas proses daur ulang dan mengurangi beban timbunan sampah di TPA.
- Peningkatan Kesadaran dan Partisipasi Masyarakat: Terbentuknya kesadaran dan partisipasi aktif masyarakat dalam pemilahan sampah, serta membentuk budaya hidup bersih dan sehat.
- Peluang Pengembangan Ekonomi Sirkular: Terbukanya peluang ekonomi baru bagi pelaku usaha di bidang pengelolaan limbah dan daur ulang melalui peningkatan ketersediaan bahan daur ulang yang bersih dan terpisah.

## Tahap Pelaksanaan:
1. Pengumpulan dan Persiapan Data: Pengumpulan dataset gambar sampah dari berbagai sumber (Kaggle dan pengambilan langsung di lapangan) dan pra-pemrosesan (pengubahan ukuran gambar, normalisasi warna, augmentasi data).
2. Pelatihan dan Penyesuaian Model AI: Melakukan fine-tuning terhadap model pre-trained dengan dataset yang telah disiapkan untuk meningkatkan akurasi dalam mengenali sampah organik dan anorganik.
3. Pengembangan Antarmuka Pengguna: Pembuatan antarmuka pengguna berbasis web menggunakan Streamlit.
4. Integrasi Sistem: Mengintegrasikan model AI dengan perangkat keras (ESP32-CAM, mikrokontroler ESP32, katup servo, dan perancangan PCB).
5. Pengujian dan Evaluasi: Meliputi uji fungsionalitas, uji akurasi klasifikasi (menggunakan dataset uji dan sampah nyata), uji respons sistem, evaluasi ketepatan pemilahan, dan analisis statistik (termasuk confusion matrix, presisi, recall, F1-score, dan akurasi).

## Anggaran Biaya: 
Total biaya yang dianggarkan adalah Rp 6.918.000. Rinciannya meliputi bahan habis pakai (Rp 1.300.000), sewa dan jasa (Rp 4.438.000), transportasi lokal (Rp 200.000), dan lain-lain (Rp 980.000).

## Tim dan Pembagian Tugas:
Lutfi Alvaro Pratama (Ketua Tim): Merancang sistem IoT, membuat skematik alat, dan membuat kode untuk alat.
Darren Makmur (Anggota 1): Menguji prototipe, membuat desain PCB, dan menulis proposal.
Happy Victor Jayata Karundeng (Anggota 2): Membuat model AI dan mengintegrasikan AI ke dalam sistem IoT.

## Jadwal Kegiatan:
Proyek ini direncanakan berlangsung selama empat bulan.

Laporan ini memberikan gambaran komprehensif mengenai ruang lingkup proyek, metodologi, hasil yang diharapkan, dan anggaran, menjadi dasar yang kuat untuk pengembangan dan implementasi sistem klasifikasi sampah berbasis AI.

1. Penempatan Alat: Perangkat pemilah fisik harus ditempatkan di lokasi di mana sampah biasa dibuang, seperti rumah, sekolah, atau fasilitas umum. Desainnya mempertimbangkan kemudahan pemasangan di berbagai lokasi.
2. Menyalakan Daya: Pastikan sistem menyala. Komponen elektronik diintegrasikan menggunakan Printed Circuit Board (PCB) atau menggunakan circuit board untuk stabilitas dan koneksi yang disederhanakan.
3. Memasukkan Sampah: Letakkan item sampah yang akan dipilah di area yang ditentukan di mana modul kamera ESP32-CAM dapat menangkap gambarnya.
4. Klasifikasi Otomatis:
ESP32-CAM akan mengambil gambar sampah.
5. Gambar ini kemudian dikirim ke model AI untuk dianalisis.
Model AI, yang telah disesuaikan (fine-tuned) menggunakan dataset sampah organik dan anorganik, akan mengklasifikasikan sampah tersebut.
6. Pemilahan Otomatis:
7. Hasil klasifikasi dikirimkan melalui REST API ke mikrokontroler ESP32.
ESP32 selanjutnya mengontrol pergerakan katup servo.
Katup akan terbuka sesuai dengan kategori sampah yang dikenali oleh model (organik atau anorganik), memungkinkan pemilahan otomatis ke jalur pembuangan yang sesuai.
8. Pemantauan dan Interaksi (Opsional):
Sistem ini dilengkapi dengan antarmuka berbasis web yang dikembangkan menggunakan Streamlit.
Melalui antarmuka ini, proses klasifikasi dapat diakses secara interaktif, memberikan informasi yang mudah dipahami oleh pengguna.



## Penyiapan Awal (sebelum menjalankan program):
Pastikan perangkat keras (ESP32-CAM, ESP32, katup servo) telah terhubung dan terintegrasi dengan benar menggunakan PCB yang telah dirancang.
Pastikan modul ESP32-CAM terhubung ke jaringan Wi-Fi yang sama dengan perangkat yang menjalankan model AI.

1. Pastikan path ke folder "Computer Vision" di komputer Anda sudah diketahui, contohnya C:\Users\YourUser\Documents\Computer Vision.
2. Menjalankan Program (melalui Command Prompt):
Buka Command Prompt (CMD) di komputer Anda.
Navigasikan ke direktori tempat folder "Computer Vision" berada. Anda dapat melakukan ini dengan mengetikkan perintah berikut dan menekan Enter:
cd C:\<path>\Computer Vision 
Ganti <path> dengan jalur yang sesuai di komputer Anda (misalnya, cd C:\Users\NamaAnda\Documents\Computer Vision).
Aktifkan virtual environment Anda. Ketikkan perintah berikut dan tekan Enter:
my_yolov5_env\Scripts\activate 
Ini akan mengaktifkan virtual environment bernama my_yolov5_env yang berisi dependensi yang dibutuhkan oleh program Anda.
Jalankan skrip Python utama untuk ESPCAMIP.py(untuk kamera) atau app.py(untuk streamlit) Ketikkan perintah berikut dan tekan Enter:
python ESPCAMIP.py atau app.py
Perintah ini akan memulai program utama yang mengelola interaksi antara kamera ESP32-CAM, model AI, dan kontrol servo.
3. Penggunaan Alat Pemilah Sampah:
Setelah program berjalan, tempatkan item sampah yang akan dipilah di area yang dapat dilihat oleh kamera ESP32-CAM.
Kamera akan menangkap gambar sampah, yang kemudian akan dikirim ke model AI untuk diklasifikasikan sebagai organik atau anorganik.
Hasil klasifikasi akan diteruskan ke mikrokontroler ESP32, yang kemudian akan mengendalikan katup servo untuk membuka jalur pembuangan yang sesuai.
Anda dapat memantau proses klasifikasi secara interaktif melalui antarmuka web yang dikembangkan menggunakan Streamlit, jika antarmuka tersebut diakses di browser Anda.
4. Pengujian dan Evaluasi:
Lakukan pengujian fungsionalitas untuk memastikan setiap komponen perangkat keras dan perangkat lunak berfungsi sesuai perancangan.
Uji akurasi klasifikasi dengan berbagai skenario pemilahan sampah untuk mengevaluasi keandalan dan akurasi sistem.
Evaluasi kecepatan respons sistem dan ketepatan pemilahan sampah.

### Link full version: https://drive.google.com/drive/folders/1_6aP6wkIUe4W78gYwEYkotTYuUILi1vs?usp=drive_link
