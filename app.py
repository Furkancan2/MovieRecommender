import streamlit as st
from src.data_loader import DataLoader
from src.recommender import MovieRecommender

# Sayfa Ayarları
st.set_page_config(page_title="Film Öneri Sistemi", layout="centered")

# --- BAŞLIK KISMI ---
st.title("🎬 Film Öneri Sistemi")
st.write("Sevdiğin bir filmi seç, yapay zeka sana benzerlerini önersin.")


# --- MODELİ HAZIRLAMA (HIZLANDIRICI İLE) ---
# st.cache_resource: Modeli her seferinde tekrar eğitmemesi için hafızada tutar.
# Böylece site donmaz, hızlı çalışır.
@st.cache_resource
def get_model():
    # Verileri yükle
    loader = DataLoader('data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
    df = loader.load_data()

    # Modeli kur ve eğit
    recommender = MovieRecommender(df)
    recommender.prepare_data()
    recommender.build_model()
    return recommender


# Yükleniyor yazısı gösterelim
with st.spinner('Yapay zeka modelleri yükleniyor...'):
    model = get_model()

# --- ARAYÜZ (KULLANICI ETKİLEŞİMİ) ---

# 1. Kullanıcıdan Film Seçmesini İste
film_listesi = model.df['title'].values
secilen_film = st.selectbox("Bir film seçin veya yazın:", film_listesi)

# 2. Butona Basılınca Öneri Yap
if st.button("Öneri Yap"):
    try:
        # Senin yazdığın recommend fonksiyonunu kullanıyoruz
        oneriler = model.recommend(secilen_film)

        st.success(f"'{secilen_film}' filmini sevenler bunları da sevdi:")

        # Sonuçları ekrana yazdır
        for film in oneriler:
            st.write(f"👉 {film}")

    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")