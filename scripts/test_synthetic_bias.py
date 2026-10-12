
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fairness_audit.audit import audit


# Both groups initially have the same positive outcome rate.
df = pd.DataFrame({
    "sex": ["Group_A"] * 100 + ["Group_B"] * 100,
    "income": [">50K"] * 50 + ["<=50K"] * 50
              + [">50K"] * 50 + ["<=50K"] * 50,
})

print("=== BEFORE BIAS INJECTION ===")
before = audit(df, ["sex"], "income")
print(
    before[["group", "positive_rate", "dpd", "dir"]]
    .to_string(index=False)
)

# Deliberately change 40 positive labels in Group_B.
df.loc[100:139, "income"] = "<=50K"

print("\n=== AFTER BIAS INJECTION ===")
after = audit(df, ["sex"], "income")
print(
    after[[
        "group",
        "positive_rate",
        "dpd",
        "dir",
        "potential_disparity_flag",
        "severity",
    ]].to_string(index=False)
)

output = ROOT / "reports" / "synthetic_bias_results.csv"
output.parent.mkdir(exist_ok=True)
after.to_csv(output, index=False)

print(f"\nResults saved to: {output}")
