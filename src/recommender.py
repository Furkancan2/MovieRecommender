import pandas as pd
import numpy as np
import ast  # To convert string lists into actual lists
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, df):
        """
        Receives the dataset at the start.
        df: Pandas DataFrame
        """
        self.df = df
        self.similarity = None  # We will calculate the similarity matrix later

    # --- HELPER FUNCTIONS (For Data Cleaning) ---

    def convert(self, obj):
        """
        Converts data from '[{"id": 28, "name": "Action"}]' format
        to ['Action'] list.
        """
        L = []
        # ast.literal_eval: Safely converts a string to a Python list
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return L

    def convert3(self, obj):
        """
        Takes only the first 3 main actors from the cast list.
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
        Finds and takes only the Director from the crew list.
        """
        L = []
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L

    # --- MAIN ENGINE ---

    def prepare_data(self):
        print("Cleaning data and creating tags...")

        # 1. Convert complex columns to clean lists
        self.df['genres'] = self.df['genres'].apply(self.convert)
        self.df['keywords'] = self.df['keywords'].apply(self.convert)
        self.df['cast'] = self.df['cast'].apply(self.convert3)  # Only first 3 actors
        self.df['crew'] = self.df['crew'].apply(self.fetch_director)  # Only director

        # 2. Convert Overview column to word list (String -> List)
        # Ex: "A movie set in future" -> ["A", "movie", "set", "in", "future"]
        self.df['overview'] = self.df['overview'].apply(lambda x: x.split())

        # 3. Remove spaces in names (Sam Worthington -> SamWorthington)
        # If we don't do this, it treats "Sam" and "Worthington" as separate words.
        # It might mix up with another "Sam" (e.g., Sam Mendes).
        self.df['genres'] = self.df['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.df['keywords'] = self.df['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.df['cast'] = self.df['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.df['crew'] = self.df['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

        # 4. Combine everything in the 'tags' column
        self.df['tags'] = self.df['overview'] + self.df['genres'] + self.df['keywords'] + self.df['cast'] + self.df[
            'crew']

        # 5. Create the final table with only what we need
        new_df = self.df[['movie_id', 'title', 'tags']]

        # Convert list back to string (Required for vectorization)
        # ["Action", "Future"] -> "Action Future"
        new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

        # Convert everything to lowercase to ignore case sensitivity
        new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

        # Update class data
        self.df = new_df
        return new_df

    def build_model(self):
        print("Training model (Vectorization)...")

        # --- MATH PART ---
        # CountVectorizer: Converts words to numerical vectors by counting them.
        # max_features=5000: Take top 5000 most used words (more slows down the system)
        # stop_words='english': Remove useless words like "the", "a", "is".
        cv = CountVectorizer(max_features=5000, stop_words='english')

        # Convert words to matrix (Every movie becomes a vector)
        vectors = cv.fit_transform(self.df['tags']).toarray()

        # Cosine Similarity: Calculate the angle (similarity) between vectors
        # We will find other movies with the closest angle to the target movie.
        self.similarity = cosine_similarity(vectors)

        print("Model is ready!")

    def recommend(self, movie_title):
        """
        Takes movie title, returns top 5 similar movies.
        """
        # 1. Find movie index (Where is it in the dataset?)
        try:
            movie_index = self.df[self.df['title'] == movie_title].index[0]
        except IndexError:
            return ["Movie not found! Please check the name."]

        # 2. Get similarity scores of that movie
        distances = self.similarity[movie_index]

        # 3. Sort scores (High to low) and take top 5 (excluding itself)
        # enumerate: Used to keep index information
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        # 4. Convert indices to movie titles and return
        recommendations = []
        for i in movies_list:
            recommendations.append(self.df.iloc[i[0]].title)

        return recommendations
