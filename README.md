# SmartLend - COMP10086 Artificial Intelligence Applications Project

SmartLend is a fictional UK fintech company building a loan default prediction service.

This repository is the running lab project for **COMP10086 Artificial Intelligence Applications**. You will use it to build a machine learning solution for predicting loan defaults, while also getting experience with the practical side of developing and organising an ML project.

## Project Structure

```text
smartlend/
│
├── .github/
│   └── workflows/
│       └── ci.yml
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── models/
├── notebooks/
├── src/
│   └── preprocess.py
├── tests/
│   └── test_preprocess.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Folders

### `config/`
Configuration files used by the project.

### `data/`
Project data. The original dataset goes in `data/raw/` and must be kept unchanged. Processed data is written to `data/processed/`.

### `docs/`
Documentation for the project, including reports, diagrams, and supporting material.

### `models/`
Saved machine learning models and related files.

### `notebooks/`
Jupyter notebooks for exploration, visualisation, and experimentation.

### `src/`
Reusable Python source code. The Lab 02 preprocessing pipeline is in `src/preprocess.py`.

### `tests/`
Automated tests for the project. The preprocessing tests are in `tests/test_preprocess.py`.

A simple way to think about the split is:

> **Use notebooks to explore. Use `src/` for code you want to keep and reuse.**

## Dataset

The project uses the **Give Me Some Credit** dataset.

Place the training file here:

```text
data/raw/cs-training.csv
```

Do not edit or commit the original CSV. The `.gitignore` file excludes raw and processed CSV files from Git.

## Python Environment

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Lab 02: Preprocessing Pipeline

The preprocessing pipeline:

1. Loads the raw CSV.
2. Removes an unnamed index column if present.
3. Validates the expected schema.
4. Median-imputes `MonthlyIncome` and `NumberOfDependents`.
5. Removes rows where `RevolvingUtilizationOfUnsecuredLines > 1.0`.
6. Removes rows where `age <= 0`.
7. Saves the processed dataset to `data/processed/cs-processed.csv`.

Run it with:

```bash
python src/preprocess.py
```

The output file should be created at:

```text
data/processed/cs-processed.csv
```

## Tests

Run the tests with:

```bash
pytest tests/ -v
```

The tests cover:

- median imputation for `MonthlyIncome` and `NumberOfDependents`
- retention of the expected columns
- removal of the specified outliers
- validation of required columns

## Continuous Integration

GitHub Actions is configured in:

```text
.github/workflows/ci.yml
```

The workflow installs the project dependencies and runs:

```bash
pytest tests/ -v
```

The workflow is currently configured for manual execution using **workflow_dispatch**, as specified for this lab.

To run it on GitHub:

1. Push the project to GitHub.
2. Open the repository's **Actions** tab.
3. Select **SmartLend CI**.
4. Select **Run workflow**.
5. Confirm that the workflow completes successfully.

## Git Hygiene

Do not commit:

```text
data/raw/*.csv
data/processed/*.csv
models/*.pkl
models/*.joblib
```

Before committing, check:

```bash
git status
```

Useful Lab 02 commit messages are:

```text
chore: establish standard project directory structure
feat: add preprocessing pipeline with imputation and outlier filtering
test: add unit tests for imputation and column schema
ci: add GitHub Actions workflow to run preprocessing tests
docs: update README with setup and run instructions
```

## Project Goal

The aim of the project is to build a **loan default prediction system for SmartLend**.

The project covers the machine learning workflow from understanding and preparing the data through to training and evaluating models. The code should be organised, testable, reproducible, and documented so that the decisions made during development can be explained.
