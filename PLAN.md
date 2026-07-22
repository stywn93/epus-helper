# EPus-Helper: Automation Plan

## 1. Tujuan

Mengotomatiskan pendaftaran **Kunjungan Sehat** dan pengisian **rekam medis lengkap** pasien di ePuskesmas Situbondo.

Data pasien dibaca dari **file Excel (.xlsx)**, script berjalan secara **manual sekali jalan**, menggunakan **satu akun dedicated untuk loket**, dengan poli **KONSELING**.

---

## 2. Alur Sistem

```
1. Load konfigurasi (URL, akun, poli, dokter)
2. Baca file Excel → daftar pasien
3. Login ke ePuskesmas
4. Loop setiap pasien:
   a. Cari pasien berdasarkan nama
   b. Jika tidak ditemukan → catat error, lanjut ke pasien berikutnya
   c. Daftarkan Kunjungan Sehat
   d. Pilih dokter
   e. Simpan pendaftaran
   f. Buka menu Medis → buka data pasien
   g. Isi Anamnesa
   h. Isi Diagnosa
   i. Isi Tindakan
   j. Isi Resep
   k. Catat sukses/gagal
5. Tampilkan laporan akhir
```

---

## 3. Format File Excel (.xlsx)

| Kolom       | Keterangan                                   |
|-------------|----------------------------------------------|
| `nama`      | Nama pasien (wajib)                          |
| `no_rm`     | No. Rekam Medis (opsional, untuk fallback)   |
| `keluhan`   | Untuk anamnesa (opsional)                    |
| `diagnosa`  | Diagnosa (opsional)                          |
| `tindakan`  | Tindakan (opsional)                          |
| `resep`     | Catatan resep (opsional)                     |

Kolom akan disesuaikan lagi setelah field rekam medis di ePuskesmas di-inspect.

Library: **openpyxl**

---

## 4. Konfigurasi

Diatur tanpa mengubah kode (`config.py` atau `.env`):

| Variabel         | Contoh                                    |
|------------------|-------------------------------------------|
| `BASE_URL`       | `https://situbondo.epuskesmas.id`         |
| `EMAIL`          | `loket-pkm@test.go.id`                    |
| `PASSWORD`       | `1Sampai9_#`                              |
| `POLI`           | `KONSELING`                               |
| `DOKTER_DEFAULT` | `dr. ANDINI KARTIKA SARI`                 |
| `FILE_EXCEL`     | `data-pasien.xlsx`                        |

Library: **python-dotenv** atau config dict biasa.

---

## 5. Struktur Kode (Single File)

```
kunjungan-sehat.py
├── load_config()
├── load_patients_from_excel()
├── login()
├── register_visit()
├── fill_anamnesa()
├── fill_diagnosa()
├── fill_tindakan()
├── fill_resep()
└── main()
```

---

## 6. Teknologi

| Library            | Fungsi                          |
|--------------------|---------------------------------|
| `playwright`       | Otomasi browser                 |
| `openpyxl`         | Baca file Excel                 |
| `python-dotenv`    | Baca konfigurasi (.env)         |

---

## 7. Error Handling & Logging

- Jika pasien tidak ditemukan → skip & catat ke log error
- Jika login gagal → stop script & tampilkan pesan
- Jika element tidak ditemukan di halaman → timeout + skip pasien
- Output akhir: ringkasan jumlah sukses/gagal

---

## 8. Tahap Implementasi

### Tahap 1 — Refactor & Data Source
- Refactor script ke fungsi-fungsi modular
- Implementasi `load_config()` dan `load_patients_from_excel()`
- File Excel contoh dengan 1-2 baris data

### Tahap 2 — Pendaftaran Otomatis
- Login
- Cari pasien
- Daftar Kunjungan Sehat → KONSELING
- Pilih dokter
- Simpan pendaftaran

### Tahap 3 — Rekam Medis
- Inspect field di halaman Anamnesa, Diagnosa, Tindakan, Resep
- Implementasi `fill_anamnesa()`
- Implementasi `fill_diagnosa()`
- Implementasi `fill_tindakan()`
- Implementasi `fill_resep()`

### Tahap 4 — Finalisasi
- Error handling & logging
- Testing dengan data real
- Dokumentasi penggunaan
