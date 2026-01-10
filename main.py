from src.data_loader import DataLoader
from src.recommender import MovieRecommender


def main():
    # 1. Load Data
    print("--- STEP 1: Loading Data ---")
    # Note on file paths: since main.py is in the main folder, it accesses data/ directly.
    loader = DataLoader('data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
    df = loader.load_data()

    # 2. Prepare Model
    print("\n--- STEP 2: Preparing Model ---")
    recommender = MovieRecommender(df)
    recommender.prepare_data()  # Cleaning
    recommender.build_model()  # Math/Vector

    # 3. Ask User for Movie and Make Recommendations
    print("\n--- SYSTEM READY ---")
    while True:
        user_input = input("\nEnter a movie name (Press 'q' to exit): ")

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        recommendations = recommender.recommend(user_input)

        print(f"\nPeople who liked '{user_input}' also liked these:")
        for movie in recommendations:
            print(f"- {movie}")


if __name__ == "__main__":
    main()
