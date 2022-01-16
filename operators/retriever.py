import numpy as np
import pandas as pd
from typing import List


class Retriever:
    def __init__(self, movie_data: pd.DataFrame, movie_id: float) -> None:
        self.movie_data: pd.DataFrame = movie_data
        self.movie_id: float = movie_id
        self.movie_name: str = movie_data[movie_data.movie_id == movie_id].title.values[
            0
        ]

    def retrieve_similar_items(self, top_items_id: np.ndarray) -> List[str]:
        """Function to print top N similar movies"""
        return [
            self.movie_data[self.movie_data.movie_id == id].title.values[0]
            for id in (top_items_id + 1)[1:]
        ]
