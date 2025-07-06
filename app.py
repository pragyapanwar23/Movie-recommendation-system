import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from recommend import recommend  
import requests

import pickle
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp {
    margin-top: -4rem;
}
.stApp img {
    width: 200px;
    display: flex;
    margin-left: auto;
    margin-right: auto;
}
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.image("https://is5-ssl.mzstatic.com/image/thumb/Purple112/v4/fc/fe/36/fcfe363e-fd08-cc5f-c85c-f3d16367bb79/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg", width=150)
st.markdown("<h1>Movie Recommendation System</h1>", unsafe_allow_html=True)

movie_name = st.selectbox("Type in the movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(movie_name)

    if recommendations:
        for movie in recommendations:
            st.subheader(movie['title'])
            st.write(movie['overview'])
            st.markdown("---")
    else:
        st.warning("No recommendations found. Try another movie.")
# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Or load from a ZIP if you're using that

# TMDB API function
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY_HERE&language=en-US"
    response = requests.get(url)
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data.get("poster_path") else ""

# Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title, fetch_poster(movie_id)))
    return recommended_movies

# Page config
st.set_page_config(layout="centered")

# Header image (icon)
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <img src='https://raw.githubusercontent.com/pragyapanwar23/Movie-recommendation-system/main/movie-icon.png' width='150'/>
    </div>
    """,
    unsafe_allow_html=True
)

    for name, poster_url in recommendations:
        st.markdown(f"### {name}")
        if poster_url:
            st.image(poster_url)
