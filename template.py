import os


def join(paths): return os.path.join(*paths)


root_path = os.path.dirname(os.path.abspath(__file__))

dirs = [
    join(["data", "raw"]),
    join(["data", "processed"]),
    "notebooks",
    "saved_models",
    "src"]

for dir_ in dirs:
    filedir = join([root_path, dir_, ".gitkeep"])
    os.makedirs(os.path.dirname(filedir), exist_ok=True)
    open(filedir, 'a').close()

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    join(["src", "__init__.py"]),
    join(["reports", "params.json"]),
    join(["reports", "scores.json"]),
    join(["tests", "conftest.py"]),
    join(["tests", "test_config.py"]),
    join(["tests", "__init__.py"]),
    "README.md"]

for file_ in files:
    filedir = join([root_path, file_])
    os.makedirs(os.path.dirname(filedir), exist_ok=True)
    open(filedir, "a").close()
