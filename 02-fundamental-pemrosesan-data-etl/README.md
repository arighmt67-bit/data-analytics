# Fundamental Pemrosesan Data: ETL Pipeline & Unit Testing 🔄

Sub-modul ini memuat implementasi proyek akhir kelas **Belajar Fundamental Pemrosesan Data** dari Dicoding Academy. Proyek ini berfokus pada arsitektur pipeline **ETL (Extract, Transform, Load)** otomatis menggunakan Python dengan scraping data, transformasi bisnis komprehensif, penyimpanan multi-target, dan pengujian unit (*unit testing*) dengan cakupan kode (*code coverage*) 100%.

---

## 📌 Ruang Lingkup Proyek & Arsitektur ETL

Pipeline dirancang secara modular dan mematuhi prinsip *Clean Code*:

1. **Extract (`utils/extract.py`):**
   * Mengambil data mentah produk fesyen secara otomatis melalui teknik web scraping (BeautifulSoup) dari situs e-commerce target.
   * Dilengkapi penanganan error (*resilience error handling*) untuk mencegah kegagalan pipeline saat situs mengalami timeout atau perubahan struktur HTML.
2. **Transform (`utils/transform.py`):**
   * **Pembersihan Data:** Menghapus karakter non-numerik pada harga dan rating, konversi tipe data numerik (`float`/`int`), serta standardisasi format teks.
   * **Filter & Validasi:** Memvalidasi batas kelayakan data (misal rentang rating 0.0 - 5.0 dan harga > 0).
3. **Load (`utils/load.py`):**
   * **Target 1 (PostgreSQL):** Menyimpan tabel hasil transformasi ke dalam basis data relasional PostgreSQL menggunakan SQLAlchemy ORM.
   * **Target 2 (Google Sheets):** Mengekspor data terstruktur secara otomatis ke Google Sheets spreadsheet via Google Sheets API v4 & Google Service Account credentials.
   * **Target 3 (CSV Backup):** Menyimpan salinan lokal berformat CSV (`products.csv`) sebagai arsip deterministik.

---

## 🧪 Pengujian Unit (Unit Testing & Coverage)

Seluruh fungsi ETL diuji secara ketat menggunakan framework `pytest` dan `pytest-mock` untuk memastikan keandalan fungsi:
* **`tests/test_extract.py`:** Menguji skenario pengambilan data sukses, respon status non-200, dan parsing elemen tag HTML.
* **`tests/test_transform.py`:** Menguji transformasi harga, validasi tipe data, filter batas rating, serta penanganan nilai kosong (*null/missing*).
* **`tests/test_load.py`:** Memverifikasi interaksi database PostgreSQL, mocking Google Sheets API, dan integritas penulisan file CSV.
* **Target Kualitas:** **100% Code Coverage** pada seluruh modul di direktori `utils/`.

---

## 📁 Struktur Direktori

```text
02-fundamental-pemrosesan-data-etl/
├── utils/
│   ├── extract.py                   # Modul ekstraksi data (web scraping)
│   ├── transform.py                 # Modul transformasi & validasi bisnis
│   └── load.py                      # Modul pemuatan multi-target (PostgreSQL, Sheets, CSV)
├── tests/
│   ├── test_extract.py              # Unit test fungsi ekstraksi
│   ├── test_transform.py            # Unit test transformasi data
│   └── test_load.py                 # Unit test operasi penyimpanan & mocking
├── google-sheets-api.example.json   # Template kredensial service account Google
├── main.py                          # Entry point eksekusi pipeline ETL utama
├── products.csv                     # Hasil dataset terarsip
├── pytest.ini                       # Konfigurasi pengujian pytest
├── requirements.txt                 # Dependensi pustaka Python
└── submission.txt                   # Catatan submission resmi Dicoding
```

---

## ⚙️ Panduan Menjalankan

### 1. Setup Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Menjalankan Unit Testing & Coverage
```bash
pytest --cov=utils tests/
```

### 3. Menjalankan Pipeline ETL
```bash
python main.py
```

---

## 👤 Author
* **Nama:** Ari Rahmat Romadhon
* **Email:** arirahmatromadhon@gmail.com
* **GitHub:** [arighmt67-bit](https://github.com/arighmt67-bit)
