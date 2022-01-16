# Backend
from pathlib import Path
from models.svd.constants.data import MovieData
from models.svd.main import svd

# Frontend
import streamlit as st
from pages.home import page_home
from pages.svd import page_svd

# Local Constants
PARENT_DIR: Path = Path(__file__).resolve().parent
DATA_DIR: Path = Path(f"{PARENT_DIR}/data")
STYLE_DIR: Path = Path(f"{PARENT_DIR}/style")


def main():
    st.set_page_config(
        page_title="BDAA Movie Recommender", page_icon=":surfer:", layout="wide"
    )
    pages = {
        "Home": page_home,
        "Movie Recommender": page_svd,
    }
    # Sidebar setup
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Jump to", list(pages.keys()))
    pages[selection]()

    # ---- CSS ----
    with open(f"{STYLE_DIR}/style.css") as style_css:
        st.markdown(f"<style>{style_css.read()}</style>", unsafe_allow_html=True)
    animation_symbol: str = "❄️"
    animation_drops: str = ""
    for _ in range(0, 10):
        animation_drops += f'<div class="snowflake">{animation_symbol}</div>'
    st.markdown(animation_drops, unsafe_allow_html=True)


def calculate_similar_movies():
    # k-principal components to represent movies, movie_id to find recommendations, top_n retrieve top n results
    k: int = 50
    movie_id: float = 10  # (getting an id from movies.dat)
    top_n: int = 10

    # Ingest data
    data: MovieData = MovieData(data_dir=DATA_DIR)

    movie_name, similar_movies = svd(
        k=k, movie_id=movie_id, top_n=top_n, data=data.data, movie_data=data.movie_data
    )
    print(f"My search: {movie_name} with id {movie_id}")
    for movie in similar_movies:
        print(movie)


if __name__ == "__main__":
    main()
