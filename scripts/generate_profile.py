
from pathlib import Path
import pandas as pd
from ucimlrepo import fetch_ucirepo
from ydata_profiling import ProfileReport

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

print("Loading Adult dataset...")

adult = fetch_ucirepo(id=2)
df = pd.concat(
    [adult.data.features, adult.data.targets],
    axis=1
)

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().replace("?", pd.NA)

print("Generating HTML profiling report...")

profile = ProfileReport(
    df,
    title="UCI Adult Dataset - Data Profiling Report",
    explorative=True
)

output = REPORTS / "adult_profile.html"
profile.to_file(str(output))

print(f"Report saved successfully: {output}")
