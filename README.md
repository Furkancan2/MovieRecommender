# 🎬 Movie Recommendation System

Bu proje, Makine Öğrenmesi (Machine Learning) ve Doğal Dil İşleme (NLP) teknikleri kullanılarak geliştirilmiş, **İçerik Tabanlı (Content-Based)** bir film öneri sistemidir.

Kullanıcı bir film ismi girdiğinde, sistem filmin **özeti, türü, oyuncu kadrosu ve yönetmeni** arasındaki anlamsal benzerlikleri analiz eder ve en uygun 5 filmi önerir.

## 🛠 Kullanılan Teknolojiler

* **Python 3.x**
* **Pandas:** Veri manipülasyonu ve temizliği için.
* **Scikit-Learn:** `CountVectorizer` ve `Cosine Similarity` algoritmaları için.
* **Numpy:** Vektörel hesaplamalar için.

## 📂 Proje Yapısı

* `src/data_loader.py`: Ham veriyi (CSV) yükler, birleştirir ve temizler.
* `src/recommender.py`: Metin işleme (NLP) ve benzerlik matrisi hesaplamalarını yapar.
* `main.py`: Projenin ana giriş noktasıdır.

## 🚀 Kurulum ve Çalıştırma

1.  **Repoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/MovieRecommender.git](https://github.com/KULLANICI_ADIN/MovieRecommender.git)
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

5.  **Başlatın:**
    ```bash
    python3 main.py
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
