import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter
import pickle
import pandas as pd
import requests
from PIL import Image
import PIL.Image
from bs4 import BeautifulSoup
from urllib.request import urlopen
import io
from streamlit_lottie import st_lottie

# Load data and movies list from corresponding JSON files
with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)

st.set_page_config(layout="wide")





st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem; 
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# st.markdown("<h1 style='text-align: center; color: red;'>Binge Watch</h1>", unsafe_allow_html=True)
st.markdown("##")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    color: #F10B0B;
     border-radius: 5%;   


     position:relative;left:40%;
     background-color: #00ff00);
     height: 1em;
     width: 6em;
     font-size:43px
}
</style>""", unsafe_allow_html=True)
b = st.button("Binge Watch")




# To set background gif

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_coding2 = load_lottiefile("bg_lotti_gif.json")
st_lottie(
    lottie_coding2,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
)


st.markdown("##")








# To display movies  based on genre
# Adventure,Action,Animation,Romance,Comedy,Sci-fi







def main_page_content():
    st.markdown('##')

    point1 = [0] * 26
    point2 = [0] * 26
    point3 = [0] * 26
    point4 = [0] * 26
    point5 = [0] * 26
    point6 = [0] * 26

    st.markdown("<h1 style='text-align: center; color: red;'>Action</h1>", unsafe_allow_html=True)
    st.markdown('##')
    point1[0] = 1
    point1.append(8)
    table = knn(point1, 5)
    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie, link in table:
        c += 1

        if (c % 5 == 1):
            with col1:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 2):
            with col2:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 3):
            with col3:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 4):
            with col4:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 0):
            with col5:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

    st.markdown("<h1 style='text-align: center; color: red;'>Adventure</h1>", unsafe_allow_html=True)
    st.markdown('##')
    point2[1] = 1
    point2.append(8)
    table = knn(point2, 5)
    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie, link in table:
        c += 1

        if (c % 5 == 1):
            with col1:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 2):
            with col2:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 3):
            with col3:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 4):
            with col4:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 0):
            with col5:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

    st.markdown("<h1 style='text-align: center; color: red;'>Animation</h1>", unsafe_allow_html=True)
    st.markdown('##')
    point3[2] = 1
    point3.append(8)
    table = knn(point3, 5)
    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie, link in table:
        c += 1

        if (c % 5 == 1):
            with col1:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 2):
            with col2:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 3):
            with col3:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 4):
            with col4:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 0):
            with col5:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

    st.markdown("<h1 style='text-align: center; color: red;'>Romance</h1>", unsafe_allow_html=True)
    st.markdown('##')
    point4[19] = 1;
    point4.append(8)
    table = knn(point4, 5)
    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie, link in table:
        c += 1

        if (c % 5 == 1):
            with col1:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 2):
            with col2:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 3):
            with col3:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 4):
            with col4:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 0):
            with col5:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

    st.markdown("<h1 style='text-align: center; color: red;'>Comedy</h1>", unsafe_allow_html=True)
    st.markdown('##')
    point5[4] = 1
    point5.append(8)
    table = knn(point5, 5)
    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie, link in table:
        c += 1

        if (c % 5 == 1):
            with col1:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 2):
            with col2:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 3):
            with col3:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 4):
            with col4:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 0):
            with col5:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

    st.markdown("<h1 style='text-align: center; color: red;'>Sci-Fi</h1>", unsafe_allow_html=True)
    st.markdown('##')

    point6[20] = 1;
    point6.append(8)
    table = knn(point6, 5)
    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie, link in table:
        c += 1

        if (c % 5 == 1):
            with col1:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 2):
            with col2:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")
        elif (c % 5 == 3):
            with col3:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 4):
            with col4:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")

        elif (c % 5 == 0):
            with col5:
                movie_poster_fetcher(link)
                st.markdown(f"[{movie}]({link})")









#To fetch movie poster on movie basis



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path





#To recommend movies and movie poster on movie basis recommendation


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters







#To fetch movie poster for genre based recommendation



def movie_poster_fetcher(imdb_link):
    ## Display Movie Poster
    url_data = requests.get(imdb_link).text
    s_data = BeautifulSoup(url_data, 'html.parser')
    imdb_dp = s_data.find("meta", property="og:image")
    movie_poster_link = imdb_dp.attrs['content']
    u = urlopen(movie_poster_link)
    raw_data = u.read()
    image = PIL.Image.open(io.BytesIO(raw_data))
    image = image.resize((260, 390), )
    st.image(image, use_column_width=False)







#K-Nearest Neighbor(KNN) Algorithm is used to recommend movies on item based collaborative recommendation



def knn(test_point, k):
    # Create dummy target variable for the KNN Classifier
    target = [0 for item in movie_titles]
    # Instantiate object for the Classifier
    model = KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Distances to most distant movie
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    # Print list of 10 recommendations < Change value of k for a different number >
    table = list()
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table





# If button named Binge Watch is clicked
#Go to home page again




if (b):


    tmp = 0
    genres = ['Action', 'Adventure', 'Animation', 'Romance', 'Comedy', 'Biography', 'Crime', 'Documentary', 'Drama',
              'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        movies = [title[0] for title in movie_titles]
        apps = ['--Select--', 'Movie based', 'Genres based']
        app_options = st.selectbox('Select application:', apps,key=1)
        app_options=apps[0]
       # app_options=st.selectbox('Select application:', apps, key=2)
        if (app_options == 'Movie based'):
            tmp = 1
        elif app_options == apps[2]:
            tmp = 2

    with col3:
        if (tmp == 1):
            movie_select = st.selectbox('Select movie:', ['--Select--'] + movies)
            if (movie_select != '--Select--'):
                tmp = 3;
        if (tmp == 2):
            options = st.multiselect('Select genres:', genres)
            if(options):
                tmp = 4;

    with col5:
        if (tmp == 4):
            st.markdown("Do you want movies on the basis of IMDb score")
            y=st.button('YES')
            if(y):
                imdb_score = st.slider('IMDb score:', 1, 10, 8)
            else:
                imdb_score=8
            tmp = 5



    st.markdown('##')
    st.markdown('##')

    if (tmp == 3):

        genres = data[movies.index(movie_select)]
        test_point = genres
        table = knn(test_point, 11)
        table.pop(0)

        movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        selected_movie = movie_select
        names, posters = recommend(selected_movie)

        c1, c2, c3, c4, c5 = st.columns(5)
        with c3:
            st.image(posters[0])
            st.text(names[0])

        st.write("---")

        st.markdown("<h3 style='text-align: center; color: red;'>Similar Movies</h3>", unsafe_allow_html=True)
        st.markdown('##')
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:

            st.image(posters[1])
            st.text(names[1])
        with col2:

            st.image(posters[2])
            st.text(names[2])

        with col3:

            st.image(posters[3])
            st.text(names[3])
        with col4:

            st.image(posters[4])
            st.text(names[4])
        with col5:

            st.image(posters[5])
            st.text(names[5])

        st.write("---")

        st.markdown("<h3 style='text-align: center; color: red;'>Recommended Movies</h3>", unsafe_allow_html=True)

        c = 0
        col1, col2, col3, col4, col5 = st.columns(5)

        for movie, link in table:

            if (c % 5 == 0):
                with col1:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 1):
                with col2:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 2):
                with col3:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 3):
                with col4:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 4):
                with col5:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            c += 1



    if (tmp == 5):
        test_point = [1 if genre in options else 0 for genre in genres]
        test_point.append(imdb_score)
        table = knn(test_point, 10)
        st.markdown("<h3 style='text-align: center; color: red;'>Recommended Movies</h3>", unsafe_allow_html=True)

        st.markdown('##')

        c = 0
        col1, col2, col3, col4, col5 = st.columns(5)

        for movie, link in table:

            if (c % 5 == 0):
                with col1:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 1):
                with col2:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 2):
                with col3:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 3):
                with col4:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 4):
                with col5:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            c += 1
    if (tmp == 0):
        main_page_content()








else:
    tmp = 0
    genres = ['Action', 'Adventure', 'Animation', 'Romance', 'Comedy', 'Biography', 'Crime', 'Documentary', 'Drama',
              'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        movies = [title[0] for title in movie_titles]
        apps = ['--Select--', 'Movie based', 'Genres based']
        app_options = st.selectbox('Select application:', apps)

        if (app_options == 'Movie based'):
            tmp = 1
        elif app_options == apps[2]:
            tmp = 2

    with col3:
        if (tmp == 1):
            movie_select = st.selectbox('Select movie:', ['--Select--'] + movies)
            if (movie_select != '--Select--'):
                tmp = 3;
        if (tmp == 2):
            options = st.multiselect('Select genres:', genres)
            if(options):
                tmp = 4;

    with col5:
        if (tmp == 4):

            st.markdown("Movies based on IMDb score")
            y = st.checkbox('YES')

            if (y):
                imdb_score = st.slider('IMDb score:', 1, 10, 8)
            else:
                imdb_score=8

            tmp = 5
        if(tmp==3):
            def load_lottieurl(url):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()


            lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_CTaizi.json")
            st_lottie(lottie_hello, height=200, key="hello")

    st.markdown('##')
    st.markdown('##')

    if (tmp == 3):

        genres = data[movies.index(movie_select)]
        test_point = genres
        table = knn(test_point, 11)
        table.pop(0)

        movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        selected_movie = movie_select
        names, posters = recommend(selected_movie)

        c1, c2, c3, c4, c5 = st.columns(5)
        with c3:
            st.image(posters[0])
            st.text(names[0])

        st.write("---")

        st.markdown("<h3 style='text-align: center; color: red;'>Similar Movies</h3>", unsafe_allow_html=True)
        st.markdown('##')


        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:

            st.image(posters[1])
            st.text(names[1])
        with col2:

            st.image(posters[2])
            st.text(names[2])

        with col3:

            st.image(posters[3])
            st.text(names[3])
        with col4:

            st.image(posters[4])
            st.text(names[4])
        with col5:

            st.image(posters[5])
            st.text(names[5])



        st.write("---")

        st.markdown("<h3 style='text-align: center; color: red;'>Recommended Movies</h3>", unsafe_allow_html=True)

        c = 0
        col1, col2, col3, col4, col5 = st.columns(5)

        for movie, link in table:

            if (c % 5 == 0):
                with col1:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 1):
                with col2:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 2):
                with col3:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 3):
                with col4:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 4):
                with col5:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            c += 1

    if (tmp == 5):
        test_point = [1 if genre in options else 0 for genre in genres]
        test_point.append(imdb_score)
        table = knn(test_point, 10)
        st.markdown("<h3 style='text-align: center; color: red;'>Recommended Movies</h3>", unsafe_allow_html=True)

        st.markdown('##')

        c = 0
        col1, col2, col3, col4, col5 = st.columns(5)

        for movie, link in table:

            if (c % 5 == 0):
                with col1:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 1):
                with col2:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")
            elif (c % 5 == 2):
                with col3:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 3):
                with col4:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            elif (c % 5 == 4):
                with col5:
                    movie_poster_fetcher(link)
                    st.markdown(f"[{movie}]({link})")

            c += 1
    if (tmp == 0):
        main_page_content()



