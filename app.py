import streamlit as st
import pickle
import pandas as pd
import requests

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix from pickle or zip
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB poster fetch
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY_HERE&language=en-US"
    response = requests.get(url)
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data.get("poster_path") else ""

# Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        title = movies.iloc[i[0]]['title']
        poster = fetch_poster(movie_id)
        recommended.append((title, poster))
    return recommended

# Set page config
st.set_page_config(layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .stApp {
            margin-top: -3rem;
        }
        h1 {
            text-align: center;
        }
        .movie-title {
            text-align: center;
            font-size: 22px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Centered image icon
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <img src='https://raw.githubusercontent.com/pragyapanwar23/Movie-recommendation-system/main/movie-icon.png' width='150'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Title and instructions
st.markdown("<h1>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Please select from the existing library</p>", unsafe_allow_html=True)

# Movie input
movie_name = st.selectbox("Type in the movie to get recommendations:", movies['title'].values)

# Recommend button
if st.button("Recommend"):
    recommendations = recommend(movie_name)

    if recommendations:
        for title, poster in recommendations:
            st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
            if poster:
                st.image(poster)
            st.markdown("---")
    else:
        st.warning("No recommendations found. Try another movie.")
