import streamlit as st
import pickle
import pandas as pd
import requests

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

# Title
st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)

# Instruction
st.markdown("<p style='text-align: center; font-size:18px;'>Please select from the existing library</p>", unsafe_allow_html=True)

# Movie select
selected_movie = st.selectbox("Type in the movie to get recommendations:", movies['title'].values)

# Button
if st.button('Recommend'):
    recommendations = recommend(selected_movie)

    for name, poster_url in recommendations:
        st.markdown(f"### {name}")
        if poster_url:
            st.image(poster_url)
