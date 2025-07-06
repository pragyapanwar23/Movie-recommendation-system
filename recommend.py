import zipfile
import pandas as pd
import pickle

# Correct file name
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with zipfile.ZipFile("similarity.zip", "r") as zip_ref:
    with zip_ref.open("similarity.pkl") as file:
        similarity = pickle.load(file)

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]] for i in movie_list]
