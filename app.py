import streamlit as st
import pickle
import pandas as pd
import requests
import zipfile
import os

# Extract similarity.pkl from zip if needed
if not os.path.exists("similarity.pkl"):
    with zipfile.ZipFile("similarity.zip", 'r') as zip_ref:
        zip_ref.extractall()

# Load movie data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Load similarity matrix
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Fetch movie poster from TMDB API
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

# Streamlit page setup
st.set_page_config(layout="centered")

# Display local icon (filmicon.png)
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <img src='filmicon.png' width='150'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Title and instructions
st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Please select from the existing library</p>", unsafe_allow_html=True)

# Dropdown for selecting a movie
selected_movie = st.selectbox("Type in the movie to get recommendations:", movies['title'].values)

# Recommendation display
if st.button('Recommend'):
    recommendations = recommend(selected_movie)

    for name, poster_url in recommendations:
        st.markdown(f"### {name}")
        if poster_url:
            st.image(poster_url)
