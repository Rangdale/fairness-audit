
from pathlib import Path
import pandas as pd
from ucimlrepo import fetch_ucirepo
from fairness_audit.audit import audit

ROOT = Path(__file__).resolve().parents[1]

print("Loading UCI Adult dataset...")

adult = fetch_ucirepo(id=2)
df = pd.concat(
    [adult.data.features, adult.data.targets],
    axis=1
)

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().replace("?", pd.NA)

print("Running fairness audit...")

report = audit(
    df=df,
    sensitive_cols=["sex", "race"],
    label_col="income",
    favorable_label=">50K",
)

output = ROOT / "reports" / "fairness_audit.csv"
report.to_csv(output, index=False)

print("\nFairness audit results:")
print(report.to_string(index=False))
print(f"\nSaved report: {output}")
