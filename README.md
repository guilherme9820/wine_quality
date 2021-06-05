**Step 1: Create a virtual environment using virtualenvwrapper**

Install it first if you don't have it installed already

```bash
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
```

Create a requirements.txt file to install some pip packages
```
dvc
dvc[gdrive]
scikit-learn
```

Create a virtual environment using python3 interpreter, and give it a name.
For this example we'll name it as 'wine_quality'

```bash
mkvirtualenv --python=/usr/bin/python3 -r requirements.txt wine_quality  
```

**Step 2: Create a structure like the following**

------------
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── data_given               <- Data acquired from a external source
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── reports
    │   ├── params         <- Parameters used 
    │   └── scores         <- Metrics of the model
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── saved_models             <- Trained and serialized models, model predictions, or model summaries
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
------------

**Step 3: Download the wine quality dataset from https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009 and put it into the 'data_given' folder**

**Step 4: Initialize git and dvc. Then track the dataset using dvc.**

```bash
git init
dvc init

dvc add data_given/winequality.csv
```

A folder called .dvc will be created when started. It'll let you track the changes with git when the dataset is added it by just typing:

```bash
git add data_given/.gitignore data_given/winequality.csv.dvc
```

However, we didn't track anything with git so far, thus we can add all files at once and commit the changes

```bash
git add . && git commit -m "First commit"
```

**Step 5: Link the local repository to a remote one, and upload your files**

```bash
git branch -M main
git remote add origin https://github.com/{your_username}/wine_quality.git
git push -u origin main
```
