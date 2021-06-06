import os


def join(paths): return os.path.join(*paths)


root_path = os.path.dirname(os.path.abspath(__file__))

dirs = [
    join(["data", "raw"]),
    join(["data", "processed"]),
    join(["prediction_service", "model"]),
    "notebooks",
    "saved_models"]

for dir_ in dirs:
    filedir = join([root_path, dir_, ".gitkeep"])
    os.makedirs(os.path.dirname(filedir), exist_ok=True)
    open(filedir, 'a').close()

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    "app.py",
    join(["prediction_service", "__init__.py"]),
    join(["prediction_service", "prediction.py"]),
    join(["src", "__init__.py"]),
    join(["reports", "params.json"]),
    join(["reports", "scores.json"]),
    join(["tests", "conftest.py"]),
    join(["tests", "test_config.py"]),
    join(["tests", "__init__.py"]),
    join(["webapp", "static", "css", "main.css"]),
    join(["webapp", "templates", "index.html"]),
    join(["webapp", "templates", "404.html"]),
    join(["webapp", "templates", "base.html"]),
    join(["webapp", "static", "script", "index.js"]),
    "README.md"]

for file_ in files:
    filedir = join([root_path, file_])
    os.makedirs(os.path.dirname(filedir), exist_ok=True)
    open(filedir, "a").close()
