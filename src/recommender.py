import pandas as pd
import numpy as np
import ast  # Metin olarak duran listeleri gerçek listeye çevirmek için
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, df):
        """
        Başlangıçta veri setini alır.
        df: Pandas DataFrame
        """
        self.df = df
        self.similarity = None  # Benzerlik matrisini sonra hesaplayacağız

    # --- YARDIMCI FONKSİYONLAR (Veri Temizliği İçin) ---

    def convert(self, obj):
        """
        '[{"id": 28, "name": "Action"}]' formatındaki veriyi
        ['Action'] listesine çevirir.
        """
        L = []
        # ast.literal_eval: String'i güvenli bir şekilde Python listesine çevirir
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return L

    def convert3(self, obj):
        """
        Oyuncular listesinden sadece ilk 3 başrolü alır.
        """
        L = []
        counter = 0
        for i in ast.literal_eval(obj):
            if counter != 3:
                L.append(i['name'])
                counter += 1
            else:
                break
        return L

    def fetch_director(self, obj):
        """
        Ekip (crew) içinden sadece Yönetmeni (Director) bulur ve alır.
        """
        L = []
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L

    # --- ANA MOTOR ---

    def prepare_data(self):
        print("Veri temizleniyor ve etiketler oluşturuluyor...")

        # 1. Karmaşık sütunları temiz listelere dönüştür
        self.df['genres'] = self.df['genres'].apply(self.convert)
        self.df['keywords'] = self.df['keywords'].apply(self.convert)
        self.df['cast'] = self.df['cast'].apply(self.convert3)  # Sadece ilk 3 oyuncu
        self.df['crew'] = self.df['crew'].apply(self.fetch_director)  # Sadece yönetmen

        # 2. Özet (Overview) sütununu kelime listesine çevir (String -> List)
        # Örn: "Gelecekte geçen bir film" -> ["Gelecekte", "geçen", "bir", "film"]
        self.df['overview'] = self.df['overview'].apply(lambda x: x.split())

        # 3. İsimlerdeki boşlukları kaldır (Sam Worthington -> SamWorthington)
        # Bunu yapmazsak "Sam" ismini ayrı, "Worthington" soyadını ayrı algılar.
        # Başka "Sam" (örn: Sam Mendes) ile karışabilir.
        self.df['genres'] = self.df['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.df['keywords'] = self.df['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.df['cast'] = self.df['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.df['crew'] = self.df['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

        # 4. Hepsini 'tags' sütununda birleştir
        self.df['tags'] = self.df['overview'] + self.df['genres'] + self.df['keywords'] + self.df['cast'] + self.df[
            'crew']

        # 5. Sadece ihtiyacımız olan son tabloyu oluştur
        new_df = self.df[['movie_id', 'title', 'tags']]

        # Listeyi tekrar string'e çevir (Vektörleştirmek için gerekli)
        # ["Action", "Future"] -> "Action Future"
        new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

        # Büyük küçük harf duyarlılığını kaldırmak için hepsini küçük harf yap
        new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

        # Sınıfın verisini güncelleyelim
        self.df = new_df
        return new_df

    def build_model(self):
        print("Model eğitiliyor (Vektörleştirme)...")

        # --- MATEMATİK KISMI ---
        # CountVectorizer: Kelimeleri sayarak sayısal vektörlere çevirir.
        # max_features=5000: En çok kullanılan 5000 kelimeyi al (fazlası sistemi yorar)
        # stop_words='english': "the", "a", "is" gibi gereksiz kelimeleri at.
        cv = CountVectorizer(max_features=5000, stop_words='english')

        # Kelimeleri matrise çevir (Her film bir vektör olur)
        vectors = cv.fit_transform(self.df['tags']).toarray()

        # Cosine Similarity: Vektörler arasındaki açıyı (benzerliği) hesapla
        # Matrix filmine en yakın açısı olan diğer filmleri bulacağız.
        self.similarity = cosine_similarity(vectors)

        print("Model hazır!")

    def recommend(self, movie_title):
        """
        Film ismini alır, en benzer 5 filmi döndürür.
        """
        # 1. Filmin index'ini bul (Veri setinde kaçıncı sırada?)
        try:
            movie_index = self.df[self.df['title'] == movie_title].index[0]
        except IndexError:
            return ["Film bulunamadı! Lütfen tam adını doğru yazdığınızdan emin olun."]

        # 2. O filmin benzerlik skorlarını al
        distances = self.similarity[movie_index]

        # 3. Skorları sırala (En yüksekten düşüğe) ve ilk 5'i al (kendisi hariç)
        # enumerate: index bilgisini kaybetmemek için kullanılır
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        # 4. İndeksleri film isimlerine çevirip döndür
        recommendations = []
        for i in movies_list:
            recommendations.append(self.df.iloc[i[0]].title)

        return recommendations