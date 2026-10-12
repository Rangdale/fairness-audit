
from pathlib import Path
import sys

import pandas as pd
from ucimlrepo import fetch_ucirepo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fairness_audit.audit import audit

print("Loading UCI Adult dataset...")

adult = fetch_ucirepo(id=2)
df = pd.concat(
    [adult.data.features, adult.data.targets],
    axis=1
)

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().replace("?", pd.NA)

# Representation-only baseline:
# Group counts and representation percentages only.
results = []

for col in ["sex", "race"]:
    groups = df[col].astype("string").fillna("Missing")
    counts = groups.value_counts(dropna=False)

    for group, count in counts.items():
        share = count / len(df)

        results.append({
            "attribute": col,
            "group": str(group),
            "count": int(count),
            "representation_share": float(share),
            "small_group_flag": share < 0.05,
        })

baseline = pd.DataFrame(results)

output = ROOT / "reports" / "representation_baseline.csv"
output.parent.mkdir(exist_ok=True)
baseline.to_csv(output, index=False)

print("\n=== Representation-only baseline ===")
print(baseline.to_string(index=False))
print(f"\nSaved: {output}")
