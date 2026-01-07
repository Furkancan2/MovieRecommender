import pandas as pd
import os


class DataLoader:
    def __init__(self, movies_path, credits_path):
        # Dosya yollarını sınıfın hafızasına atıyoruz
        self.movies_path = movies_path
        self.credits_path = credits_path

    def load_data(self):
        """
        CSV dosyalarını okur, birleştirir ve temizler.
        Döndürdüğü değer: Temizlenmiş Pandas DataFrame
        """
        print("Veriler yükleniyor...")

        # 1. Dosyaların var olup olmadığını kontrol et (Hata yönetimi)
        if not os.path.exists(self.movies_path):
            raise FileNotFoundError(f"Dosya bulunamadı: {self.movies_path}")
        if not os.path.exists(self.credits_path):
            raise FileNotFoundError(f"Dosya bulunamadı: {self.credits_path}")

        # 2. CSV dosyalarını oku
        movies = pd.read_csv(self.movies_path)
        credits = pd.read_csv(self.credits_path)

        print(f"Movies tablosu boyutu: {movies.shape}")
        print(f"Credits tablosu boyutu: {credits.shape}")

        # 3. İki tabloyu birleştir (Merge)
        # movies tablosundaki 'title' ile credits tablosundaki 'title' eşleşince satırları birleştir.
        movies = movies.merge(credits, on='title')

        # 4. Sadece işimize yarayacak sütunları seç
        # id, başlık, özet, türler, anahtar kelimeler, oyuncular, ekip
        movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

        # 5. Eksik verileri (NaN) temizle
        # Özeti veya başlığı olmayan filmleri tablodan atıyoruz.
        movies.dropna(inplace=True)

        print(f"Birleştirme ve temizleme sonrası boyut: {movies.shape}")
        return movies


# Bu dosya tek başına çalıştırılırsa test amaçlı burası çalışır
if __name__ == "__main__":
    # Dosya yollarını vererek sınıfı başlatıyoruz
    # ../data/ diyerek bir üst klasöre çıkıp data klasörüne giriyoruz
    loader = DataLoader('../data/tmdb_5000_movies.csv', '../data/tmdb_5000_credits.csv')

    try:
        df = loader.load_data()
        print("\nİlk 5 film örneği:")
        print(df[['title', 'overview']].head())  # Sadece başlık ve özeti göster
    except Exception as e:
        print(f"Bir hata oluştu: {e}")