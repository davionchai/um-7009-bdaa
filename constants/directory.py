from pathlib import Path

PARENT_DIR: Path = Path(__file__).resolve().parent.parent
DATA_DIR: Path = Path(f"{PARENT_DIR}/data")
TRAINING_PATH: Path = Path(f"{PARENT_DIR}/trained_db")

DB_PATH: Path = Path(f"{TRAINING_PATH}/trained_data.json")
STYLE_DIR: Path = Path(f"{PARENT_DIR}/style")
