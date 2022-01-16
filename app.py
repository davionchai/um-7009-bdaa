import numpy as np
import pandas as pd
from pathlib import Path


if __name__ == "__main__":
    # Directory
    PARENT_DIR: Path = Path(__file__).resolve().parent
    DATA_DIR: Path = Path(f"{PARENT_DIR}/data")
    data = pd.read_csv(
        f"{DATA_DIR}/ratings.dat",
        names=["user_id", "movie_id", "rating", "time"],
        engine="python",
        delimiter="::",
    )
    movie_data = pd.read_csv(
        f"{DATA_DIR}/movies.dat",
        names=["movie_id", "title", "genre"],
        engine="python",
        delimiter="::",
    )
