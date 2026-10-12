# Baseline vs Full Toolkit Comparison

## Methods

- **Representation-only baseline:** group counts, representation shares, and small-group flags.
- **Full toolkit:** representation signals plus positive outcome rates, DPD, DIR, disparity flags, severity labels, and group-wise missingness analysis.

## Group-level Results

| attribute   | group              |   representation_share |   positive_rate |      dpd |      dir | small_group_flag   | potential_disparity_flag   | severity             |
|:------------|:-------------------|-----------------------:|----------------:|---------:|---------:|:-------------------|:---------------------------|:---------------------|
| sex         | Male               |             0.668482   |        0.303767 | 0.194516 | 0.359655 | False              | True                       | High Priority        |
| sex         | Female             |             0.331518   |        0.109251 | 0.194516 | 0.359655 | False              | True                       | High Priority        |
| race        | White              |             0.855043   |        0.253987 | 0.152235 | 0.43461  | False              | True                       | High Priority        |
| race        | Black              |             0.0959215  |        0.120811 | 0.152235 | 0.43461  | False              | True                       | High Priority        |
| race        | Asian-Pac-Islander |             0.0311003  |        0.269256 | 0.152235 | 0.43461  | True               | True                       | Review - Small Group |
| race        | Amer-Indian-Eskimo |             0.00962287 |        0.117021 | 0.152235 | 0.43461  | True               | True                       | Review - Small Group |
| race        | Other              |             0.00831252 |        0.123153 | 0.152235 | 0.43461  | True               | True                       | Review - Small Group |

## Interpretation

The representation-only baseline identifies group sizes and small-group risks. The full toolkit additionally reports observed outcome-rate disparities and configured investigation flags.

This comparison describes differences in available signals. It does not establish that the full toolkit is more accurate without further evaluation against known test cases.

## Output

- `baseline_vs_full_toolkit.csv`
- `baseline_vs_full_toolkit.md`
