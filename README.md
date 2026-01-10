[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-ai-project.streamlit.app/)

> **🔴 Live Demo:** [Click to try the project](https://movie-ai-project.streamlit.app/)

# 🎬 Movie Recommendation System

This project is a **Content-Based** movie recommendation system developed using Machine Learning and Natural Language Processing (NLP) techniques.

When the user enters a movie title, the system analyzes the semantic similarities between the movie's **overview, genre, cast, and director** and suggests the top 5 most suitable movies.

## 🛠 Technologies Used

* **Python 3.x**
* **Streamlit:** For web interface and deployment.
* **Pandas:** For data manipulation and cleaning.
* **Scikit-Learn:** For `CountVectorizer` and `Cosine Similarity` algorithms.
* **Numpy:** For vector calculations.

## 📂 Project Structure

* `src/data_loader.py`: Loads, merges, and cleans raw data (CSV).
* `src/recommender.py`: Handles text processing (NLP) and similarity matrix calculations.
* `app.py`: Streamlit-based web interface codes.
* `main.py`: Main file to run via terminal.

## 🚀 Installation and Usage

If you want to run it on your own computer:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Furkancan2/MovieRecommender.git](https://github.com/Furkancan2/MovieRecommender.git)
    cd MovieRecommender
    ```

2.  **Set Up and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare the Dataset:**
    * Download the dataset from [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    * Put the `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` files into the `data/` folder.

5.  **Start the Interface:**
    ```bash
    streamlit run app.py
    ```

## 📊 Example Scenario

```text
Input: The Dark Knight
System Recommendation:
1. The Dark Knight Rises
2. Batman Begins
3. Batman Returns
4. Batman & Robin
5. Batman Forever
