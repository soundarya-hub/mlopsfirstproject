import os
from pathlib import Path


list_of_files = [
        ".github/MLOPSFIRSTPROJECT/.gitkeep",
        "src/__init__.py",
        "src/components/__ini__.py",
        "src/components/data_ingestoin.py",
        "src/components/data_transformation.py",
        "src/components/model_trainer.py",
        "src/components/model_evaluation.py",
        "src/pipeline/__init__.py",
        "src/pipeline/training_pipeline.py",
        "src/pipeline/prediction_pipeline.py",
        "src/logger/logging.py",
        "src/exception/exception",
        "src/utils/utils.py",
        "src/utils/__init__.py",
        "tests/unit/__init__.py",
        "tests/intigration/__init__.py",
        "init_setup.sh",
        "requirements.txt",
        "requirements_dev.txt",
        "setup.py",
        "setup.cfg",
        "pyproject.toml",
        "tox.ini",
        "experiment/experiments.ipynb", 

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #split the filename and directory bcz i want directory

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file


print("DONE")