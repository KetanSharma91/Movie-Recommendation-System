import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model_data = load_model()

movies = model_data["movies"]
tfidf = model_data["tfidf"]
tfidf_matrix = model_data["tfidf_matrix"]
indices = model_data["indices"]

def recommend(movie_name):
    if movie_name not in indices:
        return ["Movie not found"]
    
    idx = indices[movie_name]
    
    # compute similarity on demand
    sim_scores = cosine_similarity(
        tfidf_matrix[idx], tfidf_matrix
    ).flatten()
    
    # get top 5 similar movies
    similar_indices = sim_scores.argsort()[::-1][1:6]
    
    return movies.iloc[similar_indices][['title', 'genres']]

st.title("🎬 Movie Recommender")

movie_name = st.text_input("Enter movie name:")

if st.button("Recommend"):
    results = recommend(movie_name)
    
    if isinstance(results, list):
        st.write(results[0])
    else:
        for i, row in enumerate(results.values, 1):
            st.write(f"{i}. {row[0]} → {row[1]}")