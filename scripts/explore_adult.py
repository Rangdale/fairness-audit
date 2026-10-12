
from pathlib import Path
import pandas as pd
from ucimlrepo import fetch_ucirepo

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

print("Loading UCI Adult dataset...")

adult = fetch_ucirepo(id=2)

df = pd.concat(
    [adult.data.features, adult.data.targets],
    axis=1
)

df.columns = df.columns.str.strip()

# Clean whitespace and mark '?' as missing
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().replace("?", pd.NA)

print("\nDataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isna().sum())

results = []

for col in ["sex", "race"]:
    for group, subset in df.groupby(col, dropna=False):
        income = subset["income"].astype("string").str.rstrip(".")
        valid = income.notna()

        rate = (
            income[valid].eq(">50K").mean() * 100
            if valid.any() else None
        )

        results.append({
            "attribute": col,
            "group": str(group),
            "count": len(subset),
            "representation_percent": round(
                len(subset) / len(df) * 100, 2
            ),
            "income_over_50k_percent": (
                round(rate, 2) if rate is not None else None
            ),
        })

summary = pd.DataFrame(results)
output = REPORTS / "dataset_summary.csv"
summary.to_csv(output, index=False)

print("\nGroup summary:")
print(summary.to_string(index=False))
print(f"\nSaved CSV: {output}")
