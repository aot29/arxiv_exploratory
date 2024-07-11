# arxiv_exploratory
Explore the arXiv dataset.

## Using Conda
```
conda create -n arxiv_exp python=3.12.2
conda activate arxiv_exp
pip install -r requirements.txt
```

```
conda activate arxiv_exp
jupyter lab
```

## Using plain Python
```
python -m venv arxiv_exp
source arxiv_exp/bin/activate
cd workspace/arxiv_exploratory/
pip install -r requirements.txt
```

```
source arxiv_exp/bin/activate
cd workspace/arxiv_exploratory/
jupyter lab
```

1. Load the dataset: arXiv.org submitters. (2024). arXiv Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/7548853
2. Run cd to vx, run 00_load_abstracts and 00_load_metadata etc.