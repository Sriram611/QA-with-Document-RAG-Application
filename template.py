import os
from pathlib import Path

list_of_files = [
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py",
    "requirements.txt",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    # create directory if it doesn't exist
    if filepath.parent != Path("."):
        filepath.parent.mkdir(parents=True, exist_ok=True)

    # create file if it doesn't exist
    if not filepath.exists():
        filepath.touch()
        print(f"Created: {filepath}")