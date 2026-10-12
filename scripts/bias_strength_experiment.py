
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fairness_audit.audit import audit

# Equal starting rates: 100 records per group, 50 positives each.
rows = []

for group in ["Group_A", "Group_B"]:
    for i in range(100):
        rows.append({
            "group": group,
            "label": ">50K" if i < 50 else "<=50K",
        })

results = []

# Change 0, 10, 20, 30, or 40 positive labels in Group B.
for changed in [0, 10, 20, 30, 40]:
    df = pd.DataFrame(rows).copy()

    if changed:
        group_b_positive = df.index[
            (df["group"] == "Group_B")
            & (df["label"] == ">50K")
        ][:changed]

        df.loc[group_b_positive, "label"] = "<=50K"

    report = audit(
        df,
        sensitive_cols=["group"],
        label_col="label",
    )

    results.append({
        "positive_labels_changed": changed,
        "group_a_rate": 0.50,
        "group_b_rate": (50 - changed) / 100,
        "dpd": float(report["dpd"].iloc[0]),
        "dir": float(report["dir"].iloc[0]),
        "flagged": bool(
            report["potential_disparity_flag"].iloc[0]
        ),
    })

output = ROOT / "reports" / "bias_strength_results.csv"
output.parent.mkdir(exist_ok=True)
pd.DataFrame(results).to_csv(output, index=False)

print(pd.DataFrame(results).to_string(index=False))
print(f"\nSaved results: {output}")
