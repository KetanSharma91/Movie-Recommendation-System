import streamlit as st
import pickle

@st.cache_data
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model_data = load_model()

movies = model_data["movies"]
cosine_sim = model_data["cosine_sim"]
indices = model_data["indices"]

def recommend(movie_name):
    if movie_name not in indices:
        return ["Movie not found"]
    
    idx = indices[movie_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    
    movie_indices = [i[0] for i in sim_scores]
    
    return movies.iloc[movie_indices][['title', 'genres']]

st.title("🎬 Movie Recommender")

movie_name = st.text_input("Enter movie name:")

if st.button("Recommend"):
    results = recommend(movie_name)
    
    for i, row in enumerate(results.values, 1):
        st.write(f"{i}. {row[0]} → {row[1]}")
