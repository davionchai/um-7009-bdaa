import numpy as np
import pandas as pd

import streamlit as st
from pathlib import Path
from typing import List

from calculators.cosinesimilarity import top_cosine_similarity
from constants.data import MovieData
from utils.matrixprocess import MatrixProcess
from operators.retriever import Retriever


def main():
    # Ingest data
    data: MovieData = MovieData(data_dir=DATA_DIR)
    V: np.ndarray = MatrixProcess.get_svd(data=data.data)

    # k-principal components to represent movies, movie_id to find recommendations, top_n retrieve top n results
    k: int = 50
    movie_id: float = 10  # (getting an id from movies.dat)
    top_n: int = 10
    sliced: np.ndarray = V.T[:, :k]  # representative data

    top_items_id: np.ndarray = top_cosine_similarity(
        data=sliced, movie_id=movie_id, top_n=top_n
    )

    retriever: Retriever = Retriever(movie_data=data.movie_data, movie_id=movie_id)
    similar_movies: List[str] = retriever.retrieve_similar_items(
        top_items_id=top_items_id
    )
    print(f"My search: {retriever.movie_name} with id {retriever.movie_id}")
    for movie in similar_movies:
        print(movie)


if __name__ == "__main__":
    # Directory
    PARENT_DIR: Path = Path(__file__).resolve().parent
    DATA_DIR: Path = Path(f"{PARENT_DIR}/data")
    main()
