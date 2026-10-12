
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def audit(
    df,
    sensitive_cols,
    label_col,
    favorable_label=">50K",
    min_group_share=0.05,
    dir_threshold=0.80,
):
    """
    Audit group representation and positive outcome rates.

    Returns a dictionary containing group metrics and risk flags.
    These flags indicate potential risks, not proof of unfairness.
    """
    results = []

    if df.empty:
        raise ValueError("Dataset cannot be empty.")

    if label_col not in df.columns:
        raise ValueError(f"Label column '{label_col}' not found.")

    for col in sensitive_cols:
        if col not in df.columns:
            raise ValueError(f"Sensitive column '{col}' not found.")

        # Include missing sensitive values as a separate group.
        groups = df[col].astype("string").fillna("Missing")
        labels = df[label_col].astype("string").str.strip().str.rstrip(".")
        favorable = favorable_label.strip().rstrip(".")

        for group in groups.unique():
            mask = groups == group
            group_labels = labels[mask].dropna()

            count = int(mask.sum())
            share = count / len(df)

            positive_rate = (
                float(group_labels.eq(favorable).mean())
                if len(group_labels) > 0
                else None
            )

            results.append({
                "attribute": col,
                "group": str(group),
                "count": count,
                "representation_share": share,
                "positive_rate": positive_rate,
                "small_group_flag": share < min_group_share,
            })

    metrics = pd.DataFrame(results)
    metrics["dpd"] = None
    metrics["dir"] = None

    for col in sensitive_cols:
        indexes = metrics.index[metrics["attribute"] == col]
        rates = metrics.loc[indexes, "positive_rate"].dropna()

        if len(rates) >= 2:
            dpd = float(rates.max() - rates.min())

            if rates.max() > 0:
                dir_value = float(rates.min() / rates.max())
            else:
                dir_value = None

            metrics.loc[indexes, "dpd"] = dpd
            metrics.loc[indexes, "dir"] = dir_value

    metrics["potential_disparity_flag"] = (
        metrics["dir"].apply(
            lambda value: value is not None
            and pd.notna(value)
            and value < dir_threshold
        )
    )


    def severity(row):
        if row["small_group_flag"]:
            return "Review - Small Group"

        ratio = row["dir"]

        if pd.isna(ratio):
            return "Insufficient Data"
        if ratio < 0.50:
            return "High Priority"
        if ratio < dir_threshold:
            return "Needs Review"
        return "No DIR Threshold Flag"

    metrics["severity"] = metrics.apply(severity, axis=1)


    # Group-wise missing-value analysis
    missingness_results = []

    for col in sensitive_cols:
        groups = df[col].astype("string").fillna("Missing")

        for group in groups.unique():
            mask = groups == group
            subset = df.loc[mask]

            for feature in df.columns:
                missing_count = int(subset[feature].isna().sum())
                total_count = len(subset)

                missingness_results.append({
                    "attribute": col,
                    "group": str(group),
                    "feature": feature,
                    "missing_count": missing_count,
                    "missing_percent": (
                        missing_count / total_count * 100
                        if total_count else 0
                    ),
                })

    missingness = pd.DataFrame(missingness_results)
    missingness.to_csv(
        ROOT / "reports" / "group_missingness.csv",
        index=False
    )

    return metrics
