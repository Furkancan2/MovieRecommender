[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-ai-project.streamlit.app/)

> **🔴 Canlı Demo:** [Projeyi denemek için tıklayın](https://movie-ai-project.streamlit.app/)

# 🎬 Movie Recommendation System

Bu proje, Makine Öğrenmesi (Machine Learning) ve Doğal Dil İşleme (NLP) teknikleri kullanılarak geliştirilmiş, **İçerik Tabanlı (Content-Based)** bir film öneri sistemidir.

Kullanıcı bir film ismi girdiğinde, sistem filmin **özeti, türü, oyuncu kadrosu ve yönetmeni** arasındaki anlamsal benzerlikleri analiz eder ve en uygun 5 filmi önerir.

## 🛠 Kullanılan Teknolojiler

* **Python 3.x**
* **Streamlit:** Web arayüzü ve deployment için.
* **Pandas:** Veri manipülasyonu ve temizliği için.
* **Scikit-Learn:** `CountVectorizer` ve `Cosine Similarity` algoritmaları için.
* **Numpy:** Vektörel hesaplamalar için.

## 📂 Proje Yapısı

* `src/data_loader.py`: Ham veriyi (CSV) yükler, birleştirir ve temizler.
* `src/recommender.py`: Metin işleme (NLP) ve benzerlik matrisi hesaplamalarını yapar.
* `app.py`: Streamlit tabanlı web arayüz kodları.
* `main.py`: Terminal üzerinden çalıştırmak için ana dosya.

## 🚀 Kurulum ve Çalıştırma

Kendi bilgisayarınızda çalıştırmak isterseniz:

1.  **Repoyu Klonlayın:**
    ```bash
    git clone [https://github.com/Furkancan2/MovieRecommender.git](https://github.com/Furkancan2/MovieRecommender.git)
    cd MovieRecommender
    ```

2.  **Sanal Ortamı Kurun ve Aktif Edin:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Gereksinimleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Veri Setini Hazırlayın:**
    * [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) adresinden veri setini indirin.
    * `tmdb_5000_movies.csv` ve `tmdb_5000_credits.csv` dosyalarını `data/` klasörüne atın.

5.  **Arayüzü Başlatın:**
    ```bash
    streamlit run app.py
    ```

## 📊 Örnek Senaryo

```text
Giriş: The Dark Knight
Sistem Önerisi:
1. The Dark Knight Rises
2. Batman Begins
3. Batman Returns
4. Batman & Robin
5. Batman Forever
<img width="969" height="991" alt="Ekran Resmi 2026-01-07 21 48 41" src="https://github.com/user-attachments/assets/4c17b81c-fcbc-4094-91ea-636f221730a1" />

