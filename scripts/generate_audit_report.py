
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"

summary = pd.read_csv(REPORTS / "dataset_summary.csv")
fairness = pd.read_csv(REPORTS / "fairness_audit.csv")
missingness = pd.read_csv(REPORTS / "group_missingness.csv")

lines = [
    "# Fairness Auditing Toolkit - Audit Report",
    "",
    "## 1. Dataset Overview",
    "",
    "- Dataset: UCI Adult Income",
    "- Records: 48,842",
    "- Columns: 15",
    "- Sensitive attributes: sex, race",
    "- Target: income",
    "",
    "## 2. Representation and Outcome Analysis",
    "",
    summary.to_markdown(index=False),
    "",
    "## 3. Fairness Metrics and Risk Flags",
    "",
    fairness.to_markdown(index=False),
    "",
    "## 4. Group-wise Missingness",
    "",
]

nonzero = missingness[
    missingness["missing_percent"] > 0
].sort_values("missing_percent", ascending=False)

lines.append(
    nonzero.head(15).to_markdown(index=False)
)

lines.extend([
    "",
    "## 5. Interpretation and Limitations",
    "",
    "- DPD measures the difference between the highest "
    "and lowest group positive-outcome rates.",
    "- DIR is the lowest positive-outcome rate divided "
    "by the highest positive-outcome rate.",
    "- Severity labels are toolkit-defined investigation "
    "priorities, not proof of discrimination.",
    "- Small groups may have less reliable estimates.",
    "- This audit examines dataset-level signals; it does "
    "not establish causal discrimination or model fairness.",
    "",
    "## 6. Generated Artifacts",
    "",
    "- `dataset_summary.csv`",
    "- `fairness_audit.csv`",
    "- `group_missingness.csv`",
    "- `adult_profile.html`",
    "",
])

output = REPORTS / "fairness_audit_report.md"
output.write_text("\n".join(lines), encoding="utf-8")

print(f"Consolidated report saved: {output}")
