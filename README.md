# Monorepo: Data Analytics & Data Science Showcase 📊

Selamat datang di repositori pusat showcase proyek analisis data dan data science oleh **Ari Rahmat Romadhon** ([@arighmt67-bit](https://github.com/arighmt67-bit)). Repositori ini mengompilasi proyek analitik end-to-end, mulai dari pemrosesan data mentah (*data wrangling*), eksplorasi statistik deskriptif (*EDA*), analisis lanjutan (*clustering* & segmentasi), hingga pembuatan dashboard interaktif dan pelaporan bisnis berbasis metode **SMART**.

---

## 🗂️ Daftar Proyek

| No | Modul / Proyek | Deskripsi & Domain | Teknologi & Library | Status | Tautan Folder |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **01** | **Bike Sharing Analytics** | Analisis performa operasional sistem *bike sharing* (Capital Bikeshare): pengaruh cuaca, pola waktu komuter vs libur, serta segmentasi waktu dan temperatur. | Python, Pandas, Matplotlib, Seaborn, Streamlit | Selesai (Bintang 5) | [Lihat Proyek](./01-bike-sharing-analysis/) |

---

## 🚀 Proyek Unggulan

### 01. Bike Sharing Business Analytics Dashboard
* **Direktori:** [`01-bike-sharing-analysis/`](./01-bike-sharing-analysis/)
* **Live Demo Dashboard:** [Streamlit Community Cloud](https://bike-sharing-analysis-arighmt.streamlit.app/)
* **Ringkasan Analisis:**
  - **Dampak Cuaca:** Menemukan penurunan drastis peminjaman sepeda harian hingga **-63%** saat cuaca memburuk menjadi hujan/salju dibandingkan cuaca cerah (rata-rata 4,877 vs 1,803 unit/hari).
  - **Pola Komuter vs Rekreasi:** Hari kerja memiliki dua puncak (*bimodal*) pada jam sibuk komuter (08:00 dan 17:00–18:00) yang 85–90% digerakkan oleh pengguna terdaftar (*registered*). Sebaliknya, akhir pekan membentuk puncak tunggal santai di siang hari yang didominasi pengguna kasual (*casual*).
  - **Analisis Lanjutan:** Segmentasi 4 klaster waktu (*Morning Commute*, *Midday Leisure*, *Evening Commute*, *Night Off-Peak*) dan *binning* temperatur (<12°C, 12–22°C, >22°C) tanpa algoritma machine learning.
  - **Rekomendasi Bisnis:** Penjadwalan *dock rebalancing* sebelum jam 07:30 & 16:30, tarif dinamis cuaca mendung, serta pemeliharaan preventif armada pada musim dingin.

---

## 🛠️ Lingkungan Pengembangan & Panduan Menjalankan

Setiap subfolder proyek memiliki berkas `requirements.txt` dan `README.md` tersendiri dengan instruksi rinci. Untuk menjalankan proyek `01-bike-sharing-analysis`:

```bash
# Clone repositori
git clone https://github.com/arighmt67-bit/data-analytics.git
cd data-analytics/01-bike-sharing-analysis

# Pasang virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Pasang pustaka dependensi
pip install -r requirements.txt

# Jalankan dashboard interaktif
streamlit run dashboard/dashboard.py
```

---

## 👤 Profil Penulis
* **Nama:** Ari Rahmat Romadhon
* **Email:** arirahmatromadhon@gmail.com
* **GitHub:** [arighmt67-bit](https://github.com/arighmt67-bit)
* **Spesialisasi:** Cloud Architecture, DevOps/SRE, & Data Analytics
