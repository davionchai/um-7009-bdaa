import pandas as pd
import time
import streamlit as st
from typing import List
from tinydb import TinyDB, Query
from tinydb.operations import add

from constants.directory import DB_PATH
from models.svd.constants.data import MovieData
from models.svd.main import svd


def page_svd(**kwargs):
    with st.container():
        data: MovieData = kwargs.get("data", None)
        sorted_movie_data: pd.DataFrame = data.movie_data["title"]
        st.title(":tv: Movie Recommender :tv:")
        st.subheader("Movies that might be intesting :smiling_imp:")
        st.write("----")
        empty_option: str = "< Search Here >"
        movie_selected: str = st.selectbox(
            "Pick a movie >", options=[empty_option, *sorted_movie_data]
        )
        if not movie_selected == empty_option:
            with st.spinner("Beep Boop Beep..."):
                similar_movies: List[str] = calculate_similar_movies(
                    data=data, movie_selected=movie_selected
                )
                st.write("Our robot thinks that you might like the following movies:")
                for movie in similar_movies:
                    st.write("- ", movie)


def calculate_similar_movies(data: MovieData, movie_selected: str) -> List[str]:
    trained_db: TinyDB = TinyDB(DB_PATH)
    query: Query = Query()
    similar_movies: List[str] = []
    # Find the id from movie title (getting an id from movies.dat)
    # Movie_id to find recommendations
    movie_id: float = data.movie_data.loc[
        data.movie_data["title"] == movie_selected, "movie_id"
    ].values[0]
    if not trained_db.search(query.movie_id == f"{movie_id}"):
        print(f"Training for movie: [{movie_id}] - [{movie_selected}]")
        # k-principal components to represent movies, top_n retrieve top n results
        k: int = 50
        top_n: int = 10
        _, similar_movies = svd(
            k=k,
            movie_id=movie_id,
            top_n=top_n,
            data=data.data,
            movie_data=data.movie_data,
        )
        trained_db.insert(
            {"movie_id": f"{movie_id}", "title": movie_selected, "similar_movies": [],}
        )
        for similar_movie in similar_movies:
            # trained_db.update(add("similar_movies", [{"title": similar_movie}]))
            trained_db.update(
                add("similar_movies", [{"title": similar_movie}]),
                query.movie_id == f"{movie_id}",
            )
    else:
        searched_movies: List[dict] = trained_db.search(
            query.movie_id == f"{movie_id}"
        )[0].get("similar_movies", None)
        for similar_movie in searched_movies:
            similar_movies.append(similar_movie.get("title", None))
    return similar_movies
