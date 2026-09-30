"""
test_preprocess.py, Unit tests for the SmartLend preprocessing pipeline.
"""

import os
import sys

import numpy as np
import pandas as pd
import pytest

# Allow the test runner to find src/ without installing the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from preprocess import (
    EXPECTED_COLUMNS,
    impute_missing_values,
    remove_outliers,
    validate_columns,
)


def make_minimal_df():
    """Create a small DataFrame with the expected schema for testing."""
    data = {col: [1.0, 2.0, None] for col in EXPECTED_COLUMNS}
    df = pd.DataFrame(data)
    df["age"] = [35, 0, 55]
    df["SeriousDlqin2yrs"] = [0, 1, 0]
    df["RevolvingUtilizationOfUnsecuredLines"] = [0.5, 1.5, 0.3]
    return df


def test_imputed_columns_have_no_nulls():
    """After imputation, MonthlyIncome and NumberOfDependents must have no missing values."""
    df = make_minimal_df()
    df.loc[0, "MonthlyIncome"] = np.nan
    df.loc[1, "NumberOfDependents"] = np.nan

    result = impute_missing_values(df)

    assert result["MonthlyIncome"].isnull().sum() == 0, (
        "MonthlyIncome still contains null values after imputation"
    )
    assert result["NumberOfDependents"].isnull().sum() == 0, (
        "NumberOfDependents still contains null values after imputation"
    )


def test_processed_data_has_expected_columns():
    """The output of impute_missing_values must retain all expected columns."""
    df = make_minimal_df()
    result = impute_missing_values(df)

    for col in EXPECTED_COLUMNS:
        assert col in result.columns, (
            f"Expected column '{col}' missing after preprocessing"
        )


def test_remove_outliers():
    """Rows with utilisation above 1.0 or age 0 are removed."""
    data = {col: [1.0, 1.0, 1.0] for col in EXPECTED_COLUMNS}
    df = pd.DataFrame(data)
    df["SeriousDlqin2yrs"] = [0, 0, 0]
    df["age"] = [35, 40, 0]
    df["RevolvingUtilizationOfUnsecuredLines"] = [0.5, 1.5, 0.3]

    result = remove_outliers(df)

    assert len(result) == 1
    assert result.iloc[0]["age"] == 35
    assert result.iloc[0]["RevolvingUtilizationOfUnsecuredLines"] == 0.5


def test_validate_columns():
    """validate_columns raises ValueError when an expected column is missing."""
    df = make_minimal_df().drop(columns=["age"])

    with pytest.raises(ValueError):
        validate_columns(df)
