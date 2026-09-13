# Proyek Analisis Data: Bike Sharing Dataset 🚲

Repositori ini memuat submission akhir kelas **Belajar Analisis Data dengan Python** dari Dicoding Academy. Proyek ini mencakup analisis eksplorasi data secara komprehensif, visualisasi berorientasi bisnis (metode SMART), teknik analisis lanjutan (*manual grouping* dan *binning*), serta dashboard interaktif menggunakan **Streamlit**.

---

## 📌 Domain Proyek & Pertanyaan Bisnis (SMART Framework)

Proyek ini menganalisis dataset operasional sistem penyewaan sepeda (*Capital Bikeshare*) periode 2011–2012 untuk menjawab pertanyaan bisnis berikut:

1. **Pertanyaan 1 (Weather Impact):**
   * *Bagaimana variasi kondisi cuaca (Clear/Partly Cloudy, Mist/Cloudy, Light Snow/Rain) memengaruhi rata-rata volume peminjaman sepeda harian selama periode 2011–2012?*
2. **Pertanyaan 2 (Commuter vs Leisure Pattern):**
   * *Bagaimana disparitas pola penggunaan sepeda per jam antara hari kerja (working day) dan hari libur/akhir pekan (non-working day) pada pengguna kasual (casual) dibandingkan pengguna terdaftar (registered)?*

---

## 🚀 Analisis Lanjutan (Advanced Analysis)

Mengimplementasikan teknik segmentasi lanjutan tanpa algoritma machine learning sesuai anjuran rubrik:
* **Time-of-Day Clustering (Manual Grouping):** Mengelompokkan 24 jam operasional ke dalam 4 klaster aktivitas bisnis: *Morning Commute (06:00–09:00)*, *Midday Leisure (10:00–15:00)*, *Evening Commute (16:00–19:00)*, dan *Night/Off-Peak (20:00–05:00)*.
* **Temperature Binning:** Mengelompokkan temperatur aktual (°C) ke dalam interval interval objektif: *Cold (<12°C)*, *Mild (12–22°C)*, dan *Warm (>22°C)* menggunakan fungsi `pd.cut`.

---

## 📁 Struktur Direktori

```text
01-bike-sharing-analysis/
├── dashboard/
│   ├── dashboard.py         # Skrip aplikasi Streamlit dashboard
│   ├── day_clean.csv        # Dataset agregat harian siap pakai
│   └── hour_clean.csv       # Dataset agregat per jam siap pakai
├── data/
│   ├── Readme.txt           # Dokumentasi dataset asli Capital Bikeshare
│   ├── day.csv              # Dataset harian mentah
│   └── hour.csv             # Dataset per jam mentah
├── notebook.ipynb           # Jupyter Notebook analisis data lengkap (37 cells berurutan)
├── README.md                # Dokumentasi petunjuk setup & ringkasan proyek
├── requirements.txt         # Daftar dependensi library Python
└── url.txt                  # Tautan deployment Streamlit Community Cloud
```

---

## ⚙️ Panduan Menjalankan Dashboard Secara Lokal

### 1. Prasyarat Lingkungan
Pastikan Anda telah memasang **Python 3.9+** pada sistem Anda.

### 2. Setup Virtual Environment

#### Menggunakan Terminal / Bash / Command Prompt:
```bash
# Clone repositori (jika dari remote GitHub)
git clone https://github.com/arighmt67-bit/data-analytics.git
cd data-analytics/01-bike-sharing-analysis

# Buat dan aktifkan virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Di Windows: .venv\Scripts\activate

# Pasang dependensi
pip install -r requirements.txt
```

#### Menggunakan Conda:
```bash
conda create --name bike-ds python=3.9 -y
conda activate bike-ds
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi Streamlit
Jalankan perintah berikut dari root direktori proyek:
```bash
streamlit run dashboard/dashboard.py
```
Aplikasi dashboard akan terbuka otomatis di browser Anda pada alamat `http://localhost:8501`.

---

## 🌐 Live Demo Streamlit Cloud
Dashboard interaktif dapat diakses secara publik melalui tautan:
🔗 **[Bike Sharing Analytics Live Dashboard](https://bike-sharing-analysis-arighmt.streamlit.app/)** *(Dicantumkan pula di `url.txt`)*.

---

## 👤 Author
* **Nama:** Ari Rahmat Romadhon
* **Email:** arirahmatromadhon@gmail.com
* **Akun GitHub:** [arighmt67-bit](https://github.com/arighmt67-bit)
* **Profil Dicoding:** Ari Rahmat Romadhon
