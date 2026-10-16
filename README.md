# Bias and Fairness Auditing Toolkit for Training Datasets

## Project Overview

This project develops a reusable Python toolkit to identify potential bias and fairness risks in tabular machine-learning datasets before model training.

The toolkit currently analyzes demographic representation, group-level positive outcome rates, demographic disparity metrics, small-group risks, and group-wise missing-data patterns. It also generates dataset profiling and audit reports.

Audit results are intended to support further investigation. They do not independently prove discrimination or establish that a dataset is fair.

## Research Question

Can a dataset-level auditing toolkit reliably detect known, deliberately introduced bias and identify potential fairness risks in real-world datasets before model training?

## Technology Stack

- Python 3.12
- pandas
- NumPy
- scikit-learn
- Fairlearn
- ydata-profiling
- pytest

## Initial Dataset

**UCI Adult Census Income Dataset**

- Sensitive attributes: `sex`, `race`
- Target column: `income`
- Dataset size: 48,842 records and 15 columns
- Purpose: exploratory analysis and initial fairness auditing

## Implemented Features

1. Dataset loading and exploratory analysis
2. Group representation percentages
3. Group-level positive outcome rates
4. Demographic Parity Difference (DPD)
5. Disparate Impact Ratio (DIR)
6. Small-group warnings
7. Configurable DIR threshold and investigation-priority labels
8. Group-wise missing-value analysis
9. HTML dataset profiling report
10. CSV audit outputs and consolidated Markdown report
11. Automated tests for fairness metrics and input validation

## Planned Features

1. Proxy-feature risk analysis
2. Confidence intervals and uncertainty analysis
3. Additional datasets, including COMPAS and German Credit
4. Synthetic bias injection and detection experiments
5. Baseline comparisons against profiling-only and manual audits
6. Optional model-based fairness metrics using Fairlearn
7. Severity-ranked HTML/PDF audit reports
8. Expanded test coverage and reusable configuration options

## Repository Structure

```text
fairness-audit/
├── src/fairness_audit/    # Reusable audit modules
├── scripts/               # Dataset and report scripts
├── tests/                 # Automated tests
├── reports/               # Generated reports and CSV files
├── data/                  # Local datasets, if used
├── configs/               # Audit configurations, if used
├── docs/                  # Research documentation
├── README.md
└── requirements.txt
```

Some directories may be added as the project develops.

## Week 1 Progress

- Initial repository and Python environment setup
- UCI Adult dataset selection and exploration
- Group-level representation and outcome analysis
- Initial DPD and DIR calculations
- Small-group investigation flags
- Group-wise missingness analysis
- HTML dataset profiling demonstration
- Consolidated Markdown report generation
- Initial automated tests: 3 tests passing

- Implemented a representation-only baseline.
- Generated a baseline-versus-full-toolkit comparison report.
- Completed synthetic bias injection and bias-strength experiments.
- Added automated tests covering core metrics, input validation, and synthetic disparity detection.
- Expanded automated test coverage for core metrics, input validation, missing sensitive values, zero positive outcomes, and synthetic disparity detection.
- Current automated test suite: **7 tests passing**.

## Research Limitations

- Audit flags are risk indicators, not proof of discrimination.
- DPD and DIR summarize observed outcome-rate differences and do not explain their causes.
- Small groups may produce less stable estimates.
- Missingness differences require further investigation.
- Dataset-level metrics do not establish the fairness of a trained model.
- Proxy detection, uncertainty estimation, synthetic-bias experiments, and model-level fairness evaluation remain planned work.
- Fairness metrics should be interpreted in the context of dataset characteristics and domain-specific requirements.

## Running the Project

Activate the project's virtual environment, then run these commands from the repository root in PowerShell:

```powershell
$env:PYTHONPATH = "src"

python .\scripts\explore_adult.py
python .\scripts\generate_profile.py
python .\scripts\run_fairness_audit.py
python .\scripts\generate_audit_report.py
python -m pytest -v
```

The dataset scripts may require internet access to retrieve the UCI Adult dataset.

## Current Test Status

The initial test suite contains three tests covering representation and fairness metrics, empty-dataset validation, and missing-label validation.

Latest observed result: **3 tests passed**.
