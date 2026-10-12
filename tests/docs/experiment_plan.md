# Experiment Plan: Bias and Fairness Auditing Toolkit

## 1. Objective

Evaluate whether the proposed toolkit identifies potential fairness risks more comprehensively than simpler dataset inspection approaches.

## 2. Dataset

- Primary dataset: UCI Adult Census Income
- Sensitive attributes: `sex`, `race`
- Target: `income`
- Synthetic dataset: controlled group-level label disparity experiments

## 3. Baseline Approaches

### Baseline A: Profiling Only
Use the HTML profiling report to inspect distributions, missing values, and data-quality patterns.

### Baseline B: Manual Audit
Inspect group counts, representation percentages, and observed positive outcome rates using CSV summaries.

### Baseline C: Representation-Only Audit
Evaluate group representation and small-group warnings without outcome-rate disparity metrics.

### Proposed Toolkit
Combine representation analysis, positive outcome rates, DPD, DIR, small-group flags, severity labels, and group-wise missingness analysis.

## 4. Evaluation Method

Use synthetic datasets with known outcome-rate differences. Compare each approach's ability to surface the intentionally introduced signals.

Record:
- Which risk signals each approach identifies
- Whether the known synthetic disparity is flagged
- Whether small-group warnings are generated
- Whether findings can be reproduced from saved outputs

## 5. Evaluation Metrics

- Detection of deliberately introduced disparity
- False-positive behavior on equal-rate synthetic data
- Correctness of DPD and DIR calculations
- Correctness of small-group warnings
- Reproducibility of generated reports

## 6. Limitations

The current experiments evaluate controlled examples and configured rules. They do not establish real-world detection accuracy, causal discrimination, or model-level fairness.

## 7. Future Work

- Implement a representation-only baseline as a separate executable method.
- Evaluate additional synthetic scenarios.
- Validate findings on additional datasets.
- Explore model-level fairness metrics using Fairlearn.
