import pandas as pd
from pathlib import Path
from typing import List


class MovieData:
    def __init__(self, data_dir: Path) -> None:
        self.data_dir: Path = data_dir
        self.data: pd.DataFrame = self._import_data(
            data_file="ratings.dat", names=["user_id", "movie_id", "rating", "time"]
        )
        self.movie_data: pd.DataFrame = self._import_data(
            data_file="movies.dat", names=["movie_id", "title", "genre"]
        )

    def _import_data(self, data_file: str, names: List[str]):
        return pd.read_csv(
            f"{self.data_dir}/{data_file}",
            names=names,
            engine="python",
            delimiter="::",
            encoding="latin-1",
        )
