import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set page config
st.set_page_config(
    page_title="Bike Sharing Analytics Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #3B82F6;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load data
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    day_path = os.path.join(current_dir, "day_clean.csv")
    hour_path = os.path.join(current_dir, "hour_clean.csv")
    
    # Fallback to data dir if clean files not found
    if not os.path.exists(day_path):
        day_path = os.path.join(current_dir, "../data/day.csv")
        hour_path = os.path.join(current_dir, "../data/hour.csv")
        
    day_df = pd.read_csv(day_path)
    hour_df = pd.read_csv(hour_path)
    
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar Filters
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=90)
st.sidebar.title("🚲 Filter Analisis")

min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()

start_date, end_date = st.sidebar.date_input(
    label="Pilih Rentang Tanggal",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Multi-select Season filter
all_seasons = day_df['season_name'].unique().tolist()
selected_seasons = st.sidebar.multiselect(
    label="Pilih Musim",
    options=all_seasons,
    default=all_seasons
)

# Multi-select Weather filter
all_weathers = day_df['weather_name'].dropna().unique().tolist()
selected_weathers = st.sidebar.multiselect(
    label="Pilih Kondisi Cuaca",
    options=all_weathers,
    default=all_weathers
)

# Filter DataFrames
filtered_day_df = day_df[
    (day_df['dteday'].dt.date >= start_date) &
    (day_df['dteday'].dt.date <= end_date) &
    (day_df['season_name'].isin(selected_seasons)) &
    (day_df['weather_name'].isin(selected_weathers))
]

filtered_hour_df = hour_df[
    (hour_df['dteday'].dt.date >= start_date) &
    (hour_df['dteday'].dt.date <= end_date) &
    (hour_df['season_name'].isin(selected_seasons)) &
    (hour_df['weather_name'].isin(selected_weathers))
]

# Header Section
st.markdown('<div class="main-title">🚲 Bike Sharing Business Performance Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Dashboard Analisis Interaktif Pengaruh Cuaca, Pola Waktu Operasional, dan Segmentasi Pengguna Sepeda (Capital Bikeshare)</div>', unsafe_allow_html=True)

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
total_rentals = filtered_day_df['cnt'].sum()
total_registered = filtered_day_df['registered'].sum()
total_casual = filtered_day_df['casual'].sum()
avg_daily_rentals = filtered_day_df['cnt'].mean() if len(filtered_day_df) > 0 else 0

with col1:
    st.metric("Total Peminjaman", f"{total_rentals:,}")
with col2:
    st.metric("Pengguna Terdaftar (Registered)", f"{total_registered:,}", f"{(total_registered/total_rentals*100):.1f}%" if total_rentals > 0 else "0%")
with col3:
    st.metric("Pengguna Kasual (Casual)", f"{total_casual:,}", f"{(total_casual/total_rentals*100):.1f}%" if total_rentals > 0 else "0%")
with col4:
    st.metric("Rata-Rata Peminjaman/Hari", f"{avg_daily_rentals:,.0f} unit")

st.markdown("---")

# Main Charts - Row 1
tab1, tab2, tab3 = st.tabs(["📊 Pertanyaan Bisnis", "🔍 Analisis Lanjutan (Clustering)", "📈 Tren & Komparasi Musiman"])

with tab1:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("1. Pengaruh Kondisi Cuaca terhadap Peminjaman")
        weather_summary = filtered_day_df.groupby('weather_name').agg(
            avg_rentals=('cnt', 'mean'),
            total_days=('cnt', 'count')
        ).reset_index().sort_values('avg_rentals', ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        palette = ["#2563EB", "#60A5FA", "#93C5FD"]
        sns.barplot(
            data=weather_summary,
            x='weather_name',
            y='avg_rentals',
            palette=palette[:len(weather_summary)],
            ax=ax
        )
        ax.set_title("Rata-Rata Peminjaman Harian Berdasarkan Cuaca", fontsize=13, pad=12, fontweight='bold')
        ax.set_xlabel("Kondisi Cuaca", fontsize=11)
        ax.set_ylabel("Rata-Rata Peminjaman (Unit)", fontsize=11)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        
        # Data labels on bars
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{height:,.0f}',
                            xy=(p.get_x() + p.get_width() / 2, height),
                            xytext=(0, 4),
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=10, fontweight='bold')
                            
        st.pyplot(fig)
        plt.close(fig)
        st.caption("💡 **Insight:** Cuaca Clear/Partly Cloudy mencatat peminjaman tertinggi (~4,877 unit/hari), sedangkan kondisi Light Snow/Rain anjlok hingga 63% (~1,803 unit/hari).")

    with col_b:
        st.subheader("2. Pola Jam Sibuk: Hari Kerja vs Hari Libur")
        hourly_split = filtered_hour_df.groupby(['workingday', 'hr'])['cnt'].mean().reset_index()
        hourly_split['Tipe Hari'] = hourly_split['workingday'].map({1: 'Hari Kerja (Working Day)', 0: 'Hari Libur/Akhir Pekan'})
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(
            data=hourly_split,
            x='hr',
            y='cnt',
            hue='Tipe Hari',
            palette=['#EF4444', '#10B981'],
            marker='o',
            linewidth=2.2,
            ax=ax
        )
        ax.set_title("Distribusi Peminjaman per Jam (Pola Komuter vs Rekreasi)", fontsize=13, pad=12, fontweight='bold')
        ax.set_xlabel("Jam Operasional (00:00 - 23:00)", fontsize=11)
        ax.set_ylabel("Rata-Rata Unit Terpinjam", fontsize=11)
        ax.set_xticks(range(0, 24, 2))
        ax.grid(axis='both', linestyle='--', alpha=0.5)
        ax.legend(title="", frameon=True)
        
        st.pyplot(fig)
        plt.close(fig)
        st.caption("💡 **Insight:** Hari kerja membentuk pola bimodal khas komuter (puncak 08:00 & 17:00-18:00). Sebaliknya, hari libur memiliki puncak tunggal di siang hari (12:00-14:00) yang didominasi rekreasi.")

with tab2:
    st.subheader("Segmentasi Lanjutan Tanpa Machine Learning (Manual Grouping & Binning)")
    col_c, col_d = st.columns(2)
    
    with col_c:
        st.markdown("#### A. Time-of-Day Clustering (Manual Grouping)")
        time_cluster = filtered_hour_df.groupby('time_segment').agg(
            total_rentals=('cnt', 'sum'),
            casual_rentals=('casual', 'sum'),
            registered_rentals=('registered', 'sum')
        ).reset_index().sort_values('total_rentals', ascending=False)
        
        time_cluster_melted = pd.melt(
            time_cluster, 
            id_vars=['time_segment'], 
            value_vars=['registered_rentals', 'casual_rentals'],
            var_name='User Type', 
            value_name='Rentals'
        )
        time_cluster_melted['User Type'] = time_cluster_melted['User Type'].map({
            'registered_rentals': 'Registered (Komuter)',
            'casual_rentals': 'Casual (Turis/Fleksibel)'
        })
        
        fig, ax = plt.subplots(figsize=(8, 5.2))
        sns.barplot(
            data=time_cluster_melted,
            x='time_segment',
            y='Rentals',
            hue='User Type',
            palette=['#1E3A8A', '#F59E0B'],
            ax=ax
        )
        ax.set_title("Volume Peminjaman Berdasarkan Klaster Waktu", fontsize=13, pad=12, fontweight='bold')
        ax.set_xlabel("Klaster Jam Operasional", fontsize=10)
        ax.set_ylabel("Total Unit", fontsize=10)
        ax.tick_params(axis='x', rotation=15)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        ax.legend(title="", loc='upper right')
        
        st.pyplot(fig)
        plt.close(fig)
        st.caption("Klaster Evening Rush (16:00-19:00) menyumbang volume sewa terbesar dengan dominasi pengguna terdaftar (registered).")
        
    with col_d:
        st.markdown("#### B. Temperature Binning (Interval Grouping)")
        temp_bins = filtered_day_df.groupby('temp_group', observed=False).agg(
            avg_cnt=('cnt', 'mean'),
            total_days=('cnt', 'count')
        ).reset_index()
        
        fig, ax = plt.subplots(figsize=(8, 5.2))
        palette_temp = ["#38BDF8", "#34D399", "#FB923C"]
        sns.barplot(
            data=temp_bins,
            x='temp_group',
            y='avg_cnt',
            palette=palette_temp,
            ax=ax
        )
        ax.set_title("Rata-Rata Peminjaman Harian Berdasarkan Kategori Suhu", fontsize=13, pad=12, fontweight='bold')
        ax.set_xlabel("Kategori Suhu Aktual", fontsize=10)
        ax.set_ylabel("Rata-Rata Peminjaman (Unit)", fontsize=10)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        
        for p in ax.patches:
            h = p.get_height()
            if h > 0:
                ax.annotate(f'{h:,.0f}',
                            xy=(p.get_x() + p.get_width() / 2, h),
                            xytext=(0, 4),
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=10, fontweight='bold')
                            
        st.pyplot(fig)
        plt.close(fig)
        st.caption("Pengguna sepeda sangat responsif terhadap suhu hangat (>22°C) dengan rata-rata 5,651 unit/hari, dua kali lipat lebih tinggi dari cuaca dingin (<12°C).")

with tab3:
    st.subheader("Tren Peminjaman Bulanan & Pertumbuhan Tahunan (2011 vs 2012)")
    
    monthly_trend = filtered_day_df.groupby(['yr', 'mnth']).agg(
        total_rentals=('cnt', 'sum'),
        registered=('registered', 'sum'),
        casual=('casual', 'sum')
    ).reset_index()
    monthly_trend['Tahun'] = monthly_trend['yr'].map({0: '2011', 1: '2012'})
    
    month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun',
                   7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    monthly_trend['Bulan'] = monthly_trend['mnth'].map(month_names)
    
    fig, ax = plt.subplots(figsize=(11, 4.5))
    sns.lineplot(
        data=monthly_trend,
        x='Bulan',
        y='total_rentals',
        hue='Tahun',
        palette=['#64748B', '#0284C7'],
        marker='o',
        linewidth=2.5,
        ax=ax
    )
    ax.set_title("Pertumbuhan Peminjaman Bulanan: 2011 vs 2012 (YoY +64.9%)", fontsize=13, pad=12, fontweight='bold')
    ax.set_xlabel("Bulan", fontsize=11)
    ax.set_ylabel("Total Unit Terpinjam", fontsize=11)
    ax.grid(axis='both', linestyle='--', alpha=0.5)
    ax.legend(title="Tahun", frameon=True)
    
    st.pyplot(fig)
    plt.close(fig)
    
    # Table comparison
    st.dataframe(
        filtered_day_df.groupby(['year_name', 'season_name']).agg(
            Total_Peminjaman=('cnt', 'sum'),
            Rata_Rata_Harian=('cnt', 'mean'),
            Pengguna_Registered=('registered', 'sum'),
            Pengguna_Casual=('casual', 'sum')
        ).round(0),
        use_container_width=True
    )

st.markdown("---")
st.markdown("### 📋 Kesimpulan & Rekomendasi Bisnis")
c_left, c_right = st.columns(2)

with c_left:
    st.success("""
    **Kesimpulan:**
    1. **Sensitivitas Cuaca**: Kondisi cuaca cerah/berawan merupakan pendorong utama pemanfaatan armada (rata-rata 4,877 peminjaman/hari). Kondisi hujan/salju menurunkan drastis permintaan hingga 63% (1,803 peminjaman/hari).
    2. **Segmentasi Perilaku Waktu**: Hari kerja digerakkan oleh komuter reguler dengan lonjakan tajam pada jam berangkat (08:00) dan pulang kerja (17:00–18:00). Sementara akhir pekan mencerminkan aktivitas rekreasi kasual yang terdistribusi santai pada siang hingga sore hari.
    """)

with c_right:
    st.info("""
    **Rekomendasi Aksi (Action Items):**
    1. **Dynamic Fleet Rebalancing**: Realokasi armada sepeda antar stasiun secara intensif sebelum pukul 07:30 dan 16:30 pada stasiun residensial dan pusat perkantoran untuk mencegah stasiun kosong/penuh.
    2. **Weather-Adaptive Promotion & Maintenance**: Luncurkan insentif tarif dinamis (*surge discounts*) saat cuaca mendung/hujan ringan, dan jadwalkan inspeksi/pemeliharaan berkala armada sepeda pada hari-hari dengan prakiraan cuaca buruk atau musim dingin.
    """)

st.caption("Dashboard Proyek Analisis Data - Dicoding Collection | Author: Ari Rahmat Romadhon")
