import pickle
import streamlit as st
import pandas as pd


def recommend(movie):
    movie_index= movies[movies['title']==movie].index[0]
    distance= similarty[movie_index]
    movie_list= sorted(list(enumerate(distance)), reverse= True, key= lambda x: x[1])[1:6]
    
    recommended_movies= []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movie_dict= pickle.load(open('Movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movie_dict)

similarty= pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")


option = st.selectbox(
    'How would you like as Preference?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations= recommend(option)
    for i in recommendations:
        st.write(i)