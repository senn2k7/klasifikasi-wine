# Klasifikasi Wine dengan Decision Tree

Nama: Husein Kurnia Waluyo  
NIM: 253307046

## 1. Masalah
Menebak kelas kultivar anggur (1, 2, atau 3) dari 13 hasil uji kimia.

## 2. Dataset
- Nama: Wine (UCI Machine Learning Repository), diambil dari salinan bawaan scikit-learn (`load_wine`)
- Sumber: https://archive.ics.uci.edu/dataset/109/wine
- Sitasi: Aeberhard, S. & Forina, M. (1992). Wine [Dataset]. https://doi.org/10.24432/C5PC7J
- Lisensi: CC BY 4.0
- Ukuran: 178 data, 13 fitur numerik. Kelas 1 = 59, kelas 2 = 71, kelas 3 = 48
- Perubahan: kolom target dinamai `kelas` dan nomornya diubah dari 0-2 menjadi 1-3

## 3. Metode
- Teknik: Machine Learning (supervised learning, klasifikasi)
- Algoritma: Decision Tree (`max_depth=3`, `random_state=42`)
- Preprocessing: pemeriksaan data kosong (hasil: 0). Tanpa scaling karena Decision Tree membandingkan satu fitur dengan satu ambang.
- Pembagian data: 80% latih (142), 20% uji (36), stratified, `random_state=42`

## 4. Hasil dan Evaluasi
- Akurasi latih: 99,30%
- Akurasi uji: 94,44% (34 dari 36 benar)

| Asli \ Prediksi | Kelas 1 | Kelas 2 | Kelas 3 |
|---|---|---|---|
| Kelas 1 | 11 | 1 | 0 |
| Kelas 2 | 0 | 14 | 0 |
| Kelas 3 | 0 | 1 | 9 |

| Kelas | Precision | Recall | F1 |
|---|---|---|---|
| 1 | 1,00 | 0,92 | 0,96 |
| 2 | 0,88 | 1,00 | 0,93 |
| 3 | 1,00 | 0,90 | 0,95 |

Dua kesalahan terjadi saat data kelas 1 dan kelas 3 ditebak sebagai kelas 2.

## 5. Cara Menjalankan
Aplikasi web memakai Django. Setelah server berjalan, buka http://127.0.0.1:8000 Aplikasi juga disiapkan untuk deploy di Vercel (Python 3.13).
```
python -m pip install -r requirements.txt
python train.py
python manage.py runserver
```

## 6. Refleksi
- Dataset kecil dan relatif mudah, sehingga akurasi tinggi belum tentu berlaku untuk data lain.
- Evaluasi hanya memakai satu kali pembagian data. Hasil bisa berubah jika pembagiannya berbeda.
- `max_depth=3` dipilih agar pohon mudah dijelaskan, belum dicari nilai terbaiknya.
- Input di aplikasi dibatasi pada rentang nilai dataset.
- Pengembangan: cross-validation dan perbandingan dengan algoritma lain.
- Proyek ini dibuat dengan bantuan AI.
