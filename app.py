# Backend
from models.svd.constants.data import MovieData

# Frontend
import streamlit as st
from pages.home import page_home
from pages.svd import page_svd

# Local Constants
from constants.directory import DATA_DIR, STYLE_DIR


def main():
    # Frontend index
    st.set_page_config(
        page_title="BDAA Movie Recommender", page_icon=":surfer:", layout="wide"
    )

    data: MovieData = load_data()

    pages = {
        "Home": page_home,
        "Movie Recommender": page_svd,
    }

    # Sidebar setup
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Jump to", list(pages.keys()))
    pages[selection](data=data)

    # ---- CSS ----
    with open(f"{STYLE_DIR}/style.css") as style_css:
        st.markdown(f"<style>{style_css.read()}</style>", unsafe_allow_html=True)
    animation_symbol: str = "❄️"
    animation_drops: str = ""
    for _ in range(0, 10):
        animation_drops += f'<div class="snowflake">{animation_symbol}</div>'
    st.markdown(animation_drops, unsafe_allow_html=True)


@st.cache(suppress_st_warning=True)
def load_data():
    """Ingest data"""
    print("Loading data")
    data: MovieData = MovieData(data_dir=DATA_DIR)
    print("Data loaded")
    return data


if __name__ == "__main__":
    main()
