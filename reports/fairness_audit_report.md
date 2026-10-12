# Fairness Auditing Toolkit - Audit Report

## 1. Dataset Overview

- Dataset: UCI Adult Income
- Records: 48,842
- Columns: 15
- Sensitive attributes: sex, race
- Target: income

## 2. Representation and Outcome Analysis

| attribute   | group              |   count |   representation_percent |   income_over_50k_percent |
|:------------|:-------------------|--------:|-------------------------:|--------------------------:|
| sex         | Female             |   16192 |                    33.15 |                     10.93 |
| sex         | Male               |   32650 |                    66.85 |                     30.38 |
| race        | Amer-Indian-Eskimo |     470 |                     0.96 |                     11.7  |
| race        | Asian-Pac-Islander |    1519 |                     3.11 |                     26.93 |
| race        | Black              |    4685 |                     9.59 |                     12.08 |
| race        | Other              |     406 |                     0.83 |                     12.32 |
| race        | White              |   41762 |                    85.5  |                     25.4  |

## 3. Fairness Metrics and Risk Flags

| attribute   | group              |   count |   representation_share |   positive_rate | small_group_flag   |      dpd |      dir | potential_disparity_flag   | severity             |
|:------------|:-------------------|--------:|-----------------------:|----------------:|:-------------------|---------:|---------:|:---------------------------|:---------------------|
| sex         | Male               |   32650 |             0.668482   |        0.303767 | False              | 0.194516 | 0.359655 | True                       | High Priority        |
| sex         | Female             |   16192 |             0.331518   |        0.109251 | False              | 0.194516 | 0.359655 | True                       | High Priority        |
| race        | White              |   41762 |             0.855043   |        0.253987 | False              | 0.152235 | 0.43461  | True                       | High Priority        |
| race        | Black              |    4685 |             0.0959215  |        0.120811 | False              | 0.152235 | 0.43461  | True                       | High Priority        |
| race        | Asian-Pac-Islander |    1519 |             0.0311003  |        0.269256 | True               | 0.152235 | 0.43461  | True                       | Review - Small Group |
| race        | Amer-Indian-Eskimo |     470 |             0.00962287 |        0.117021 | True               | 0.152235 | 0.43461  | True                       | Review - Small Group |
| race        | Other              |     406 |             0.00831252 |        0.123153 | True               | 0.152235 | 0.43461  | True                       | Review - Small Group |

## 4. Group-wise Missingness

| attribute   | group              | feature        |   missing_count |   missing_percent |
|:------------|:-------------------|:---------------|----------------:|------------------:|
| race        | Asian-Pac-Islander | native-country |             128 |           8.4266  |
| sex         | Female             | occupation     |            1273 |           7.86191 |
| sex         | Female             | workclass      |            1270 |           7.84338 |
| race        | Other              | workclass      |              31 |           7.63547 |
| race        | Other              | occupation     |              31 |           7.63547 |
| race        | Amer-Indian-Eskimo | workclass      |              35 |           7.44681 |
| race        | Amer-Indian-Eskimo | occupation     |              35 |           7.44681 |
| race        | Black              | occupation     |             329 |           7.02241 |
| race        | Black              | workclass      |             326 |           6.95838 |
| race        | Asian-Pac-Islander | workclass      |              96 |           6.31995 |
| race        | Asian-Pac-Islander | occupation     |              96 |           6.31995 |
| race        | Other              | native-country |              24 |           5.91133 |
| race        | White              | occupation     |            2318 |           5.5505  |
| race        | White              | workclass      |            2311 |           5.53374 |
| sex         | Male               | occupation     |            1536 |           4.70444 |

## 5. Interpretation and Limitations

- DPD measures the difference between the highest and lowest group positive-outcome rates.
- DIR is the lowest positive-outcome rate divided by the highest positive-outcome rate.
- Severity labels are toolkit-defined investigation priorities, not proof of discrimination.
- Small groups may have less reliable estimates.
- This audit examines dataset-level signals; it does not establish causal discrimination or model fairness.

## 6. Generated Artifacts

- `dataset_summary.csv`
- `fairness_audit.csv`
- `group_missingness.csv`
- `adult_profile.html`
