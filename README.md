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

Get the dataset (if it's not already there! It's big!): arXiv.org submitters. (2024). arXiv Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/7548853


Run `cd v3`, run the notebooks:

1. Cleanup the data
* 00_load_abstracts.ipynb
* 00_load_metadata.ipynb
* 01_clean_and_tokenize.ipynb

2. Fit some models (LDA and Ensemble LDA are independent models)
* 02_fit_LDA.ipynb
* 02_fit_ensemble_LDA.ipynb

3. Use LLM to name the topics (LLama and Mistral can be used, among others, with varying results)
* 03_llama.ipynb
* 03_mistral.ipynb

4. Todo: create a usable topic network graph
* Topic_graph_cscl.ipynb (not finished)


