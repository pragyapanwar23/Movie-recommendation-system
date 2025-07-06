import streamlit as st
import pandas as pd
from PIL import Image
from recommend import recommend  

import pickle
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp {
    margin-top: -4rem;
}
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ✅ Centered image using HTML
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://is5-ssl.mzstatic.com/image/thumb/Purple112/v4/fc/fe/36/fcfe363e-fd08-cc5f-c85c-f3d16367bb79/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg' width='150'/>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.subheader("Select from the existing library")
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
