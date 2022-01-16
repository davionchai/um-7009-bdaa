import numpy as np
import pandas as pd
from typing import List, Tuple

from models.svd.calculators.cosinesimilarity import top_cosine_similarity
from models.svd.operators.retriever import Retriever
from models.svd.utils.matrixprocess import MatrixProcess


def svd(
    k: int, movie_id: float, top_n: int, data: pd.DataFrame, movie_data: pd.DataFrame
) -> Tuple[str, float, List[str]]:
    # SVD Matrix
    V: np.ndarray = MatrixProcess.get_svd(data=data)
    # Representative data
    sliced: np.ndarray = V.T[:, :k]

    top_items_id: np.ndarray = top_cosine_similarity(
        data=sliced, movie_id=movie_id, top_n=top_n
    )

    retriever: Retriever = Retriever(movie_data=movie_data)
    similar_movies: List[str] = retriever.retrieve_similar_items(
        top_items_id=top_items_id, movie_id=movie_id
    )

    return retriever.movie_name, similar_movies
