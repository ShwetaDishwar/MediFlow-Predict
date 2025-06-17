import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "tele_no_show_predictor"

list_of_files = [
    f"{project_name}/data/raw/.gitkeep",
    f"{project_name}/data/processed/.gitkeep",
    f"{project_name}/notebooks/01_data_preparation.ipynb",
    f"{project_name}/notebooks/02_eda.ipynb",
    f"{project_name}/notebooks/03_modeling.ipynb",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/preprocessing.py",
    f"{project_name}/src/modeling.py",
    f"{project_name}/src/utils.py",
    f"{project_name}/reports/visuals/.gitkeep",
    f"{project_name}/reports/summary.pdf",
    f"{project_name}/outputs/model.joblib",
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/.gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
