
import pandas as pd
import pytest

from fairness_audit.audit import audit


def test_representation_and_fairness_metrics():
    df = pd.DataFrame({
        "sex": ["Male", "Male", "Female", "Female"],
        "income": [">50K", ">50K", "<=50K", "<=50K"],
    })

    result = audit(
        df,
        sensitive_cols=["sex"],
        label_col="income",
    )

    male = result[result["group"] == "Male"].iloc[0]
    female = result[result["group"] == "Female"].iloc[0]

    assert male["count"] == 2
    assert female["count"] == 2

    assert abs(float(male["representation_share"]) - 0.5) < 1e-9
    assert abs(float(male["dpd"]) - 1.0) < 1e-9
    assert abs(float(male["dir"]) - 0.0) < 1e-9


def test_empty_dataset_raises_error():
    df = pd.DataFrame(columns=["sex", "income"])

    with pytest.raises(ValueError, match="empty"):
        audit(df, ["sex"], "income")


def test_missing_label_column_raises_error():
    df = pd.DataFrame({"sex": ["Male", "Female"]})

    with pytest.raises(ValueError, match="Label column"):
        audit(df, ["sex"], "income")


def test_missing_sensitive_values_are_included():
    df = pd.DataFrame({
        "sex": ["Male", None, "Female", "Female"],
        "income": [">50K", "<=50K", ">50K", "<=50K"],
    })

    result = audit(df, ["sex"], "income")

    missing_group = result[result["group"] == "Missing"]

    assert len(missing_group) == 1
    assert missing_group.iloc[0]["count"] == 1


def test_zero_positive_outcomes_do_not_create_invalid_ratio():
    df = pd.DataFrame({
        "sex": ["Male", "Male", "Female", "Female"],
        "income": ["<=50K", "<=50K", "<=50K", "<=50K"],
    })

    result = audit(df, ["sex"], "income")

    assert (result["positive_rate"] == 0).all()
    assert result["dir"].isna().all()
    assert not result["potential_disparity_flag"].any()


def test_missing_sensitive_column_raises_error():
    df = pd.DataFrame({
        "income": [">50K", "<=50K"],
    })

    with pytest.raises(ValueError, match="Sensitive column"):
        audit(df, ["sex"], "income")
