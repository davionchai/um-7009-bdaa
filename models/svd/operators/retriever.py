import numpy as np
import pandas as pd
from typing import List


class Retriever:
    def __init__(self, movie_data: pd.DataFrame) -> None:
        self.movie_data: pd.DataFrame = movie_data

    def retrieve_similar_items(
        self, movie_id: float, top_items_id: np.ndarray
    ) -> List[str]:
        """Function to print top N similar movies"""
        self.movie_name: str = self.movie_data[
            self.movie_data.movie_id == movie_id
        ].title.values[0]
        return [
            self.movie_data[self.movie_data.movie_id == id].title.values[0]
            for id in (top_items_id + 1)[1:]
        ]
