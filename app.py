import streamlit as st
import pickle
import pandas as pd
import requests as rq

movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity_matrix = pickle.load(open('similarity.pkl','rb'))
similarity = pd.DataFrame(similarity_matrix)


def poster_fetch(movie_id):

    response_API = rq.get('https://api.themoviedb.org/3/movie/{}?api_key=0a1d8081fb02e806e03b728ff13a70f9'.format(movie_id))
    data_image = response_API.json()

    return "https://image.tmdb.org/t/p/w500/" + data_image['poster_path']

def recommend_movie(movie):
    mov_index = movies[movies['title'] == movie].index[0]

    diff_in_similarities = similarity[mov_index]

    min_diff_movies = sorted(list(enumerate(diff_in_similarities)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movie = []
    recommended_movie_poster = []
    for i in min_diff_movies:
        movie_id = movies.iloc[i[0]].id

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(poster_fetch(movie_id))


    return recommended_movie,recommended_movie_poster


st.title('Movie Recommender System')

# Add a selectbox to the sidebar:
selected_movie = st.sidebar.selectbox('Select movies',(movies['title'].values))

if st.button('Recommend'):
    name , posters = recommend_movie(selected_movie)

    col1, col2, col3 , col4, col5, col6 = st.columns(6)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
         st.text(name[2])
         st.image(posters[2])
    with col4:
         st.text(name[3])
         st.image(posters[3])
    with col5:
         st.text(name[4])
         st.image(posters[4])
    with col6:
         st.text(name[5])
         st
