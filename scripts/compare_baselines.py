
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"

baseline = pd.read_csv(REPORTS / "representation_baseline.csv")
full = pd.read_csv(REPORTS / "fairness_audit.csv")

comparison = baseline.merge(
    full[
        [
            "attribute",
            "group",
            "positive_rate",
            "dpd",
            "dir",
            "potential_disparity_flag",
            "severity",
        ]
    ],
    on=["attribute", "group"],
    how="left",
    validate="one_to_one",
)

comparison["extra_signals_from_full_toolkit"] = (
    "Positive outcome rate, DPD, DIR, disparity flag, severity"
)

output_csv = REPORTS / "baseline_vs_full_toolkit.csv"
comparison.to_csv(output_csv, index=False)

# Create a readable Markdown comparison report.
lines = [
    "# Baseline vs Full Toolkit Comparison",
    "",
    "## Methods",
    "",
    "- **Representation-only baseline:** group counts, representation "
    "shares, and small-group flags.",
    "- **Full toolkit:** representation signals plus positive outcome "
    "rates, DPD, DIR, disparity flags, severity labels, and "
    "group-wise missingness analysis.",
    "",
    "## Group-level Results",
    "",
    comparison[
        [
            "attribute",
            "group",
            "representation_share",
            "positive_rate",
            "dpd",
            "dir",
            "small_group_flag",
            "potential_disparity_flag",
            "severity",
        ]
    ].to_markdown(index=False),
    "",
    "## Interpretation",
    "",
    "The representation-only baseline identifies group sizes and "
    "small-group risks. The full toolkit additionally reports "
    "observed outcome-rate disparities and configured investigation "
    "flags.",
    "",
    "This comparison describes differences in available signals. "
    "It does not establish that the full toolkit is more accurate "
    "without further evaluation against known test cases.",
    "",
    "## Output",
    "",
    "- `baseline_vs_full_toolkit.csv`",
    "- `baseline_vs_full_toolkit.md`",
    "",
]

output_md = REPORTS / "baseline_vs_full_toolkit.md"
output_md.write_text("\n".join(lines), encoding="utf-8")

print("Comparison generated successfully.")
print(f"CSV: {output_csv}")
print(f"Markdown: {output_md}")
print("\nPreview:")
print(
    comparison[
        ["attribute", "group", "positive_rate", "dpd", "dir", "severity"]
    ].to_string(index=False)
)
