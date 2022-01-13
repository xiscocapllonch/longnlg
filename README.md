# Analysis of long generations with NLG

This repository contains the code necessary to carry out a research for the final project of the master's degree in data science at the Universitat Oberta de Catalunya.

### Clone repository

```bash
git clone https://github.com/xiscocapllonch/longnlg.git
cd longnlg
```

### Install environment

```bash
pip install pipenv
pipenv install --dev
(echo "import nltk" ; echo "nltk.download('punkt')") | pipenv run python
```

### Run test

```bash
pipenv run pytest
```

## Contents

#### Generator [[generator.py](generator.py)]

Implementation of a text generator using the GPT-2 model

#### Perplexity model [[perplexity_model.py](perplexity_model.py)]
Example of the method with which the perplexity model has been trained.
