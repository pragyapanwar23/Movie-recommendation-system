# Movie-recommendation-system
Design and implementation of ML powered movie recommendation system

Problem Statement:
The vast array of cinematic options presents a delightful yet daunting challenge for film enthusiasts. While the gigantic volume of available movies offers endless possibilities for exploration and identifying titles that align with personal preferences can be a time-consuming process. Build a recommendation system that helps suggest titles of the similar genres as a certain title according to the personal preferences.

Overview:
To overcome the struggles of browsing to find titles favoring personal preferences, a movie recommendation system that suggests similar genres titles has been built. This movie recommendation system leverages the power of genre similarity. This system aims to address the aforementioned challenge by suggesting films that share similar genre characteristics with a user-selected movie. The system uses ML techniques to turn the genres to vectors and analyze them for each title in the data-frame to find the similarity between them so that it can suggest the titles with the highest similarity to the user-selected title. This system provides an ease of finding their preferred titles to movie enthusiast overwhelmed by the large volume of options present.

Methodology used:
Data Acquisition Datasets sourced from Kaggle.
Data Preprocessing Data imported into Pandas DataFrames. Data cleaning and preparation using Pandas. Merged multiple CSV files into a single DataFrame. Feature selection to retain relevant columns. Textual data (genres, cast, crew) converted to lists using Ast library. Genre names extracted from genre list column. Cast and crew lists shortened. New column created combining genres, cast, and crew.

Data Modeling Feature engineering using CountVectorizer and cosine_similarity from sklearn. Genre data converted into numerical vectors. Similarity scores calculated between movies based on genre vectors.
Backend Development Data serialization using pickle for efficient storage and retrieval.
Frontend Development Streamlit framework used for building the user interface. Wide layout configured for the web page. Movie titles loaded into a dropdown for user selection. Recommendation button implemented to trigger the recommendation process.
Recommendation Logic User-selected movie is used to find similar movies based on pre-computed similarity scores. Recommended movies are displayed with their titles and overviews.
Additional Features Loading indicator displayed during recommendation process. Customizations for title size, logo placement, and color scheme implemented.

Conclusion:
The project developed a movie recommender using a dataset with 5000 movies to give recommendations based on genres. The user is recommended movies according to their preference and the most likely recommendations they will enjoy. The user types the name of the movie in the search box or can simply select one from the dropdown, press the “recommend” button and get the desired recommendations according to the selected movie. This is a simple yet functional system that will help movie enthusiasts to find a curated list of titles suiting their preferences.
