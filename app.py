import pickle
import streamlit as st
import numpy as np
import pandas as pd

def recommend(book_name):
    pos=np.where(pt.index==book_name)[0][0]
    similar_books_in=pd.DataFrame(list(enumerate(similarity_scores[pos])),columns=['book-index','similarity']).sort_values('similarity',ascending=False)['book-index'][1:11]
    l1=list([])
    l2=list([])
    for i in similar_books_in:
        l1.append(pt.index[i])
        l2.append(list(filtered_rating[filtered_rating['Book-Title']==pt.index[i]]['Image-URL-M'].head(1))[0])
    return l1,l2

filtered_rating = pickle.load(open('filtered_rating.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))


st.header('Book Recommender System')
data1 = pd.read_csv("Books.csv")
data2 = pd.read_csv("Users.csv")
data3 = pd.read_csv("Ratings.csv")
if st.checkbox('Show Training Dataframe'):
    if st.checkbox('Show Books Dataset'):
        data1
    if st.checkbox('Show Users Dataset'):
        data2
    if st.checkbox('Show Ratings Dataset'):
        data3


st.subheader("Please type your Book's name!")
books_list = pt.index
selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    books_list
)

if st.button('Find Similar/Recommended Books'):
    recommended_book_names,recommended_book_posters = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_book_names[0])
        st.image(recommended_book_posters[0])
    with col2:
        st.text(recommended_book_names[1])
        st.image(recommended_book_posters[1])

    with col3:
        st.text(recommended_book_names[2])
        st.image(recommended_book_posters[2])
    with col4:
        st.text(recommended_book_names[3])
        st.image(recommended_book_posters[3])
    with col5:
        st.text(recommended_book_names[4])
        st.image(recommended_book_posters[4])
    #if st.button('Find more Similar/Recommended Books'):
    #    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_book_names[5])
        st.image(recommended_book_posters[5])
    with col2:
        st.text(recommended_book_names[6])
        st.image(recommended_book_posters[6])

    with col3:
        st.text(recommended_book_names[7])
        st.image(recommended_book_posters[7])
    with col4:
        st.text(recommended_book_names[8])
        st.image(recommended_book_posters[8])
    with col5:
        st.text(recommended_book_names[9])
        st.image(recommended_book_posters[9])
    