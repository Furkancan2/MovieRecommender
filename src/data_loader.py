import pandas as pd
import os

class DataLoader:
    def __init__(self, movies_path, credits_path):
        # Save file paths to the class
        self.movies_path = movies_path
        self.credits_path = credits_path

    def load_data(self):
        """
        Reads, merges, and cleans CSV files.
        Returns: Cleaned Pandas DataFrame
        """
        print("Loading data...")

        # 1. Check if files exist (Error handling)
        if not os.path.exists(self.movies_path):
            raise FileNotFoundError(f"File not found: {self.movies_path}")
        if not os.path.exists(self.credits_path):
            raise FileNotFoundError(f"File not found: {self.credits_path}")

        # 2. Read CSV files
        movies = pd.read_csv(self.movies_path)
        credits = pd.read_csv(self.credits_path)

        print(f"Movies table size: {movies.shape}")
        print(f"Credits table size: {credits.shape}")

        # 3. Merge the two tables
        # Merge rows when 'title' in movies matches 'title' in credits
        movies = movies.merge(credits, on='title')

        # 4. Select only useful columns
        # id, title, overview, genres, keywords, cast, crew
        movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

        # 5. Clean missing data (NaN)
        # Drop movies without an overview or title
        movies.dropna(inplace=True)

        print(f"Size after merging and cleaning: {movies.shape}")
        return movies


# If this file runs alone, this part runs for testing
if __name__ == "__main__":
    # Start the class with file paths
    # Use ../data/ to go up one folder and enter data folder
    loader = DataLoader('../data/tmdb_5000_movies.csv', '../data/tmdb_5000_credits.csv')

    try:
        df = loader.load_data()
        print("\nFirst 5 movie examples:")
        print(df[['title', 'overview']].head())  # Show only title and overview
    except Exception as e:
        print(f"An error occurred: {e}")
