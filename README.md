# Bias and Fairness Auditing Toolkit for Training Datasets

## Project Overview

This project aims to develop a reusable Python toolkit that identifies potential bias risks in tabular machine-learning datasets before model training.

The toolkit will examine demographic representation, group-level label disparities, missing-data patterns, and potential proxy features. Optional model-based fairness metrics will be evaluated in later stages.

## Research Question

Can a dataset-level auditing toolkit reliably detect known, deliberately introduced bias and identify potential fairness risks in real-world datasets before model training?

## Technology Stack

- Python
- pandas and NumPy
- scikit-learn
- Fairlearn
- ydata-profiling
- pytest

## Initial Dataset

UCI Adult Census Income dataset.

- Sensitive attributes: sex and race
- Target: income
- Purpose: initial exploratory analysis and fairness auditing

## Planned Features

1. Dataset profiling and validation
2. Representation and small-group checks
3. Group-level label disparity analysis
4. Group-wise missingness analysis
5. Proxy-feature risk analysis
6. Optional model-based fairness metrics
7. Severity-ranked HTML/PDF audit reports

## Repository Structure

- `src/fairness_audit/`: reusable audit modules
- `scripts/`: executable scripts
- `data/`: local datasets
- `reports/`: generated results
- `configs/`: audit configurations
- `tests/`: automated tests
- `docs/`: research documentation

## Week 1 Progress

- Initial repository and environment setup
- Dataset selection and exploration
- Fairness metric research
- Proposed architecture and evaluation plan
- Baseline profiling demonstration

## Research Limitations

Audit flags are risk indicators, not proof of discrimination or a definitive judgment that a dataset is fair or unfair. Metrics will be interpreted in context, with attention to small groups, uncertainty, and dataset limitations.
