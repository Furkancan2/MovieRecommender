from src.data_loader import DataLoader
from src.recommender import MovieRecommender


def main():
    # 1. Veriyi Yükle
    print("--- ADIM 1: Veri Yükleniyor ---")
    # Dosya yollarına dikkat: main.py ana klasörde olduğu için data/ klasörüne direkt erişir.
    loader = DataLoader('data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
    df = loader.load_data()

    # 2. Modeli Hazırla
    print("\n--- ADIM 2: Model Hazırlanıyor ---")
    recommender = MovieRecommender(df)
    recommender.prepare_data()  # Temizlik
    recommender.build_model()  # Matematik/Vektör

    # 3. Kullanıcıdan Film İsteme ve Öneri Yapma
    print("\n--- SİSTEM HAZIR ---")
    while True:
        user_input = input("\nBir film ismi girin (Çıkmak için 'q'): ")

        if user_input.lower() == 'q':
            print("Güle güle!")
            break

        recommendations = recommender.recommend(user_input)

        print(f"\n'{user_input}' filmini sevenler bunları da sevdi:")
        for movie in recommendations:
            print(f"- {movie}")


if __name__ == "__main__":
    main()