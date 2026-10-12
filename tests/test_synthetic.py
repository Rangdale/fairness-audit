
import pandas as pd

from fairness_audit.audit import audit


def test_toolkit_detects_injected_disparity():
    df = pd.DataFrame({
        "sex": ["Group_A"] * 100 + ["Group_B"] * 100,
        "income": (
            [">50K"] * 50 + ["<=50K"] * 50
            + [">50K"] * 50 + ["<=50K"] * 50
        ),
    })

    # Baseline: both groups have equal positive rates.
    baseline = audit(df, ["sex"], "income")

    assert baseline["dpd"].astype(float).max() == 0.0
    assert abs(baseline["dir"].astype(float).min() - 1.0) < 1e-9
    assert not baseline["potential_disparity_flag"].any()

    # Inject disparity by changing 40 positive labels in Group_B.
    df.loc[100:139, "income"] = "<=50K"

    result = audit(df, ["sex"], "income")

    assert abs(result["dpd"].astype(float).max() - 0.40) < 1e-9
    assert abs(result["dir"].astype(float).min() - 0.20) < 1e-9
    assert result["potential_disparity_flag"].all()
