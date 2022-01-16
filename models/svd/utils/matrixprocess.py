import numpy as np
import pandas as pd


class MatrixProcess:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_svd(data: pd.DataFrame) -> np.ndarray:
        # Creating the rating matrix (rows as movies, columns as users)
        ratings_mat: np.ndarray = np.ndarray(
            shape=(np.max(data.movie_id.values), np.max(data.user_id.values)),
            dtype=np.uint8,
        )
        ratings_mat[
            data.movie_id.values - 1, data.user_id.values - 1
        ] = data.rating.values
        # Normalizing the matrix(subtract mean off)
        normalised_mat: np.ndarray = ratings_mat - np.asarray(
            [(np.mean(ratings_mat, 1))]
        ).T

        # Computing the Singular Value Decomposition (SVD)
        A: np.ndarray = normalised_mat.T / np.sqrt(ratings_mat.shape[0] - 1)
        _, _, V = np.linalg.svd(A)
        return V
