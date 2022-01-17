# db init
from tinydb import TinyDB
from constants.directory import DB_PATH, TRAINING_PATH


def main():
    initialize_db()


def initialize_db():
    try:
        if not TRAINING_PATH.exists():
            print(f"Dir - [{TRAINING_PATH}] not found. Proceeding to create the dir.")
            TRAINING_PATH.mkdir(parents=True, exist_ok=True)
    except Exception as error:
        print(f"Error while cleaning [{TRAINING_PATH}] - [{error}].")
    TinyDB(DB_PATH)


if __name__ == "__main__":
    main()
