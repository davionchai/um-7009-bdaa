import numpy as np
import pandas as pd

np.seterr(divide="ignore", invalid="ignore")


def top_cosine_similarity(
    data: pd.DataFrame, movie_id: float, top_n: int = 10
) -> np.ndarray:
    """Function to calculate the cosine similarity (sorting by most similar and returning the top N)"""
    index: float = movie_id - 1  # Movie id starts from 1 in the dataset
    movie_row: np.ndarray = data[index, :]
    magnitude: np.ndarray = np.sqrt(np.einsum("ij, ij -> i", data, data))
    similarity: np.ndarray = np.dot(movie_row, data.T) / (magnitude[index] * magnitude)
    sort_indexes: np.ndarray = np.argsort(-similarity)
    return sort_indexes[: top_n + 1]
