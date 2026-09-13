# Monorepo: Data Analytics & Data Science Showcase 📊

Selamat datang di repositori pusat showcase proyek analisis data dan pemrosesan data (data engineering/analytics) oleh **Ari Rahmat Romadhon** ([@arighmt67-bit](https://github.com/arighmt67-bit)). Repositori ini mengompilasi portofolio data end-to-end: mulai dari arsitektur otomatisasi pipeline data (*ETL Pipeline, Web Scraping, PostgreSQL, Google Sheets API*), eksplorasi statistik deskriptif (*EDA, Data Wrangling*), analisis lanjutan (*Clustering* & Segmentasi Waktu/Suhu), hingga pengembangan dashboard analitik interaktif berbasis **Streamlit**.

---

## 🗂️ Daftar Proyek

| No | Modul / Proyek | Deskripsi & Domain | Teknologi & Pustaka | Status | Tautan Folder |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **01** | **Bike Sharing Analytics** | Analisis performa operasional sistem *bike sharing* (Capital Bikeshare): pengaruh cuaca, pola waktu komuter vs libur, serta segmentasi waktu dan temperatur. | Python, Pandas, Matplotlib, Seaborn, Streamlit | Selesai (Bintang 5) | [Lihat Proyek](./01-bike-sharing-analysis/) |
| **02** | **Fundamental Pemrosesan Data (ETL)** | Arsitektur pipeline data ETL otomatis: web scraping data e-commerce, transformasi data bisnis, penyimpanan multi-target (PostgreSQL, Google Sheets, CSV), dan unit test 100% coverage. | Python, Pandas, BeautifulSoup, SQLAlchemy, Pytest, Pytest-Mock | Selesai (Bintang 5) | [Lihat Proyek](./02-fundamental-pemrosesan-data-etl/) |

---

## 🚀 Rincian Proyek Unggulan

### 01. Bike Sharing Business Analytics Dashboard
* **Direktori:** [`01-bike-sharing-analysis/`](./01-bike-sharing-analysis/)
* **Live Demo Dashboard:** [Streamlit Community Cloud](https://bike-sharing-analysis-arighmt.streamlit.app/)
* **Ringkasan Analisis:**
  - **Dampak Cuaca:** Menemukan penurunan drastis peminjaman sepeda harian hingga **-63%** saat cuaca memburuk menjadi hujan/salju dibandingkan cuaca cerah (rata-rata 4,877 vs 1,803 unit/hari).
  - **Pola Komuter vs Rekreasi:** Hari kerja memiliki dua puncak (*bimodal*) pada jam sibuk komuter (08:00 dan 17:00–18:00) yang 85–92% digerakkan oleh pengguna terdaftar (*registered*). Sebaliknya, akhir pekan membentuk puncak tunggal santai di siang hari yang didominasi pengguna kasual (*casual*).
  - **Analisis Lanjutan:** Segmentasi 4 klaster waktu (*Morning Commute*, *Midday Leisure*, *Evening Commute*, *Night Off-Peak*) dan *binning* temperatur (<12°C, 12–22°C, >22°C) tanpa algoritma machine learning.
  - **Rekomendasi Bisnis:** Penjadwalan *dock rebalancing* sebelum jam 07:30 & 16:30, tarif dinamis cuaca mendung, serta pemeliharaan preventif armada pada musim dingin.

### 02. Automated ETL Data Pipeline & Unit Testing
* **Direktori:** [`02-fundamental-pemrosesan-data-etl/`](./02-fundamental-pemrosesan-data-etl/)
* **Ringkasan Analisis:**
  - **Ekstraksi Tangguh (Extract):** Web scraping data produk fesyen menggunakan BeautifulSoup dengan mekanisme penanganan galat dan validasi status respons HTTP.
  - **Transformasi & Validasi (Transform):** Pembersihan string harga/rating non-numerik, konversi tipe data numerik, penanganan *missing values*, dan validasi aturan bisnis.
  - **Pemuatan Multi-Target (Load):** Menyimpan hasil agregasi ke basis data PostgreSQL (SQLAlchemy), integrasi API Google Sheets Spreadsheet v4 dengan kredensial service account, dan penyimpanan cadangan CSV lokal.
  - **Pengujian Unit Ketat:** Diuji secara deterministik menggunakan `pytest` dan `pytest-mock` dengan cakupan kode (*code coverage*) 100%.

---

## 🛠️ Lingkungan Pengembangan & Panduan Menjalankan

Setiap subfolder proyek memiliki berkas `requirements.txt` dan `README.md` tersendiri dengan instruksi rinci.

### Menjalankan Proyek 01 (Bike Sharing Analytics Dashboard):
```bash
git clone https://github.com/arighmt67-bit/data-analytics.git
cd data-analytics/01-bike-sharing-analysis
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

### Menjalankan Proyek 02 (ETL Pipeline & Unit Test):
```bash
cd data-analytics/02-fundamental-pemrosesan-data-etl
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest --cov=utils tests/
python main.py
```

---

## 👤 Profil Penulis
* **Nama:** Ari Rahmat Romadhon
* **Email:** arirahmatromadhon@gmail.com
* **GitHub:** [arighmt67-bit](https://github.com/arighmt67-bit)
* **Spesialisasi:** Cloud Architecture, DevOps/SRE, & Data Analytics
