import os
from pathlib import Path

project_name = "crewAI_template"

list_of_files = [
    "src/__init__.py",
    "src/main.py",
    "src/crew.py",
    "src/config/__init__.py",
    "src/models/__init__.py",
    "src/tools/__init__.py",
    "src/utils/__init__.py",
    ".env",
    ".env.example",
    ".gitignore",
    "Dockerfile",
    "README.md",
    ".dockerignore",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass