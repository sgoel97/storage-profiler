from pathlib import Path
import os
import pandas as pd


def get_current_path():
    path = Path("./")

    return f"Currently at {path.resolve()}"


def get_files(path):
    path = Path(path)

    print(f"Gathering data from {path.resolve()}")
    data = []

    for dirpath, dirnames, finenames in os.walk(path):
        size_gb = Path(dirpath).stat().st_size / 1000
        data.append([size_gb, dirpath, dirnames, finenames])

    df = pd.DataFrame(data, columns=["size_gb", "dirpath", "dirnames", "filenames"])

    return df
