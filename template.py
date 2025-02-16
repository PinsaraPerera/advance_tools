import os
from pathlib import Path

project_name = "crewAI_template"

list_of_files = [
    "app/__init__.py",
    "app/main.py",
    "app/api/__init__.py",
    "app/api/endpoints/__init__.py",
    "app/api/endpoints/sample.py",
    "app/core/__init__.py",
    "app/core/config.py",
    "app/models/__init__.py",
    "app/models/sample.py",
    "app/schemas/__init__.py",
    "app/schemas/sample.py",
    "app/utils/__init__.py",
    "app/utils/sample.py",
    "app/crud/__init__.py",
    "app/crud/sample.py",
    "app/db/__init__.py",
    "app/db/base.py",
    "app/db/session.py",
    "app/src/__init__.py",
    "app/src/main.py",
    "app/src/crew.py",
    "app/src/config/__init__.py",
    "app/src/models/__init__.py",
    "app/src/tools/__init__.py",
    "app/src/utils/__init__.py",
    ".env",
    ".env.example",
    "Dockerfile",
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