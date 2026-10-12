# Synthetic Bias Injection Experiment

## 1. Objective

To evaluate whether the fairness auditing toolkit can flag a deliberately introduced difference in positive outcome rates between two groups.

## 2. Methodology

A synthetic dataset containing 200 records was created:

- Group A: 100 records
- Group B: 100 records
- Initial positive outcome rate: 50% for both groups

To introduce disparity, 40 positive labels in Group B were changed to negative labels.

## 3. Results

| Metric | Before Injection | After Injection |
|---|---:|---:|
| Group A positive rate | 50% | 50% |
| Group B positive rate | 50% | 10% |
| Demographic Parity Difference (DPD) | 0.00 | 0.40 |
| Disparate Impact Ratio (DIR) | 1.00 | 0.20 |
| Potential disparity flag | False | True |

## 4. Interpretation

Before injection, both groups had equal positive outcome rates. After injection, the toolkit flagged the difference using its configured DIR threshold of 0.80.

The experiment demonstrates that the current implementation can detect this deliberately introduced disparity in a controlled synthetic dataset.

## 5. Limitations

- This is a controlled experiment with only two groups.
- It does not establish detection reliability on real-world datasets.
- A disparity flag does not prove discrimination or identify its cause.
- The experiment evaluates dataset-level outcome differences, not the fairness of a trained model.

## 6. Conclusion

The initial synthetic bias detection test passed. Further experiments are needed to evaluate the toolkit across different types and levels of injected disparity and additional datasets.

## 7. Bias-Strength Experiment

### Objective

To evaluate how the toolkit responds to increasing levels of deliberately introduced group-level outcome disparity.

### Experimental Setup

The experiment used two groups with 100 records each. Both groups initially had 50 positive labels. We then changed 0, 10, 20, 30, or 40 positive labels in Group B to negative labels.

### Results

| Positive labels changed | Group A rate | Group B rate | DPD | DIR | Flagged |
|---:|---:|---:|---:|---:|---|
| 0 | 0.50 | 0.50 | 0.00 | 1.00 | No |
| 10 | 0.50 | 0.40 | 0.10 | 0.80 | No |
| 20 | 0.50 | 0.30 | 0.20 | 0.60 | Yes |
| 30 | 0.50 | 0.20 | 0.30 | 0.40 | Yes |
| 40 | 0.50 | 0.10 | 0.40 | 0.20 | Yes |

### Findings

The observed DPD increased as more positive labels were changed in Group B. The DIR decreased from 1.00 to 0.20.

With the configured rule `DIR < 0.80`, the toolkit did not flag the case where DIR was exactly 0.80, but it flagged all tested cases below that threshold.

### Limitations

This is a controlled synthetic experiment. It demonstrates the expected behavior of the implemented threshold rule, but it does not establish detection accuracy on real-world datasets or prove discrimination.

### Output

Results were saved to `reports/bias_strength_results.csv`.