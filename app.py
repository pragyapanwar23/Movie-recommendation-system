import streamlit as st
import pickle
import pandas as pd
from PIL import Image



def recommend(movie):
    index = movies.loc[movies['title'] == movie].index[0]
    distance = similarity[index]
    distance = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in distance[1:6]:
        recommended_movies.append(movies.iloc[i[0]])
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp {
    margin-top: -4rem; 
        display: flex;
}
.stApp img {  
    width: 200px;  
    display: flex;
    margin-left:450px;
}</style>
""", unsafe_allow_html=True)

st.image("https://is5-ssl.mzstatic.com/image/thumb/Purple112/v4/fc/fe/36/fcfe363e-fd08-cc5f-c85c-f3d16367bb79/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg", width=150)  # Adjust width as needed

st.markdown("""
<h1 style="text-align: center;">Movie Recommendation System</h1>
""", unsafe_allow_html=True)

movie_name = st.selectbox("Type in the movie to get recommendations", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(movie_name)
    for movie in recommendations:
        st.write(movie['title'])
        st.write(movie['overview'])
