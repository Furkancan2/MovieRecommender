import streamlit as st
from src.data_loader import DataLoader
from src.recommender import MovieRecommender

# Page Settings
st.set_page_config(page_title="Movie Recommendation System", layout="centered")

# --- HEADER SECTION ---
st.title("🎬 Movie Recommendation System")
st.write("Choose a movie you like, and AI will suggest similar ones.")


# --- PREPARE MODEL (WITH CACHE) ---
# st.cache_resource: Keeps the model in memory to avoid retraining every time.
# So the site runs fast and doesn't freeze.
@st.cache_resource
def get_model():
    # Load data
    loader = DataLoader('data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
    df = loader.load_data()

    # Build and train the model
    recommender = MovieRecommender(df)
    recommender.prepare_data()
    recommender.build_model()
    return recommender


# Show a loading message
with st.spinner('Loading AI models...'):
    model = get_model()

# --- INTERFACE (USER INTERACTION) ---

# 1. Ask User to Select a Movie
film_listesi = model.df['title'].values
secilen_film = st.selectbox("Select or type a movie:", film_listesi)

# 2. Make Recommendation When Button Clicked
if st.button("Recommend"):
    try:
        # Using the recommend function you wrote
        oneriler = model.recommend(secilen_film)

        st.success(f"People who liked '{secilen_film}' also liked these:")

        # Print results to screen
        for film in oneriler:
            st.write(f"👉 {film}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
