# Experimental Plan — Bias and Fairness Auditing Toolkit

## 1. Objective

The objective of this experiment is to evaluate whether the Bias and Fairness Auditing Toolkit can detect known, deliberately introduced differences in positive outcome rates and how its performance compares with simpler auditing approaches.

The experiments will measure detection performance, false-positive rates, fairness metrics, and execution time.

## 2. Research Question

Can a dataset-level auditing toolkit reliably detect deliberately introduced bias and identify potential fairness risks in datasets before model training?

## 3. Dataset and Experimental Scope

### Primary dataset

UCI Adult Census Income Dataset.

- Sensitive attributes: `sex`, `race`
- Target column: `income`
- Favorable outcome: `>50K`
- Data processing: Python and pandas
- Audit implementation: Existing fairness-audit toolkit

The existing audit implementation normalizes trailing periods in income labels. Therefore, `>50K` and `>50K.` should be treated consistently.

### Experimental scope

The primary experiments will focus on group representation, positive outcome rates, Demographic Parity Difference (DPD), Disparate Impact Ratio (DIR), and the ability to detect controlled differences between groups.

Model-based fairness metrics such as equalized odds are outside the core scope unless model predictions are added separately.

COMPAS and German Credit are candidates for future validation, not prerequisites for the initial experiments.

## 4. Experimental Hypotheses

**H1 — Detection sensitivity:** Stronger injected outcome disparities will generally be easier to detect than weaker disparities.

**H2 — Baseline comparison:** The full toolkit will provide more dedicated fairness-analysis outputs than profiling-only and representation-only approaches.

**H3 — Representation limitation:** Representation-only analysis may fail to identify an outcome disparity when the group composition remains unchanged.

**H4 — Threshold sensitivity:** Changing the DIR threshold will change the frequency of fairness-risk flags.

**H5 — Efficiency:** Automated auditing may reduce the time required to produce a repeatable audit compared with a manual audit. This will be evaluated using recorded execution time and analyst time.

These hypotheses must be evaluated using experimental results rather than assumed to be true.

## 5. Controlled Dataset Construction

### 5.1 Preserve the original dataset

Keep an untouched copy of the original Adult dataset for exploratory analysis and a natural-data case study.

Do not treat the original dataset as ground-truth unbiased data. Its real-world group differences are not, by themselves, proof of bias or proof of fairness.

### 5.2 Create a controlled negative control

Create a separate experimental copy and randomly permute its income labels across records using a fixed random seed.

This preserves the overall distribution of income labels while breaking their original association with individual records, including sensitive attributes.

Use multiple seeds to assess variability. Small random differences in group outcome rates may remain, so the control should be checked before use.

The resulting dataset is a synthetic experimental control, not a representation of a genuinely unbiased real-world population.

### 5.3 Inject known outcome disparities

Starting from each controlled copy, deliberately reduce the favorable outcome rate of one selected group.

Initial test groups:

- `sex = Female`
- `race = Black`

Run the experiments separately for each sensitive attribute.

Proposed injection strengths are reductions of 0, 5, 10, 15, and 20 percentage points in the selected group's positive outcome rate relative to its control rate.

Implement these changes by flipping a controlled number of favorable labels to unfavorable labels within the selected group. Record the exact number of changed labels and the achieved outcome-rate difference.

If a requested injection strength cannot be achieved, record the actual result rather than silently substituting another strength.

Only experimental copies may be modified. Record the random seed, selected group, requested injection strength, actual change, and output file for each run.

## 6. Four Baseline Approaches

### Baseline 1 — Profiling-only

Generate the general-purpose HTML dataset profiling report without running the dedicated fairness audit.

Record what relevant information is visible in the report and whether an outcome disparity can be identified through a predefined review procedure.

This baseline does not automatically provide the same fairness-specific metrics as the full toolkit.

### Baseline 2 — Manual audit

Calculate group counts, representation percentages, positive outcome rates, DPD, and DIR using a spreadsheet or a separately documented manual procedure.

Apply the same predeclared DIR threshold used for the full-toolkit comparison.

Record analyst time and any calculation or interpretation errors.

### Baseline 3 — Representation-only

Compare group counts and representation percentages and identify small-group risks.

Do not use target-label disparities, DPD, or DIR in this baseline. This preserves the distinction between representation auditing and outcome auditing.

### Baseline 4 — Full fairness toolkit

Use the complete available audit implementation to calculate group representation, positive outcome rates, DPD, DIR, small-group flags, and group-wise missingness.

Use the current default DIR threshold of 0.80 for the primary comparison, unless the experiment explicitly tests another threshold.

The current implementation and its output should be inspected before the experiment is finalized.

## 7. Experiment Matrix

| Experiment | Test conditions | Main objective |
|---|---|---|
| E1: Control validation | Controlled copies with no injected disparity | Measure false-positive behavior |
| E2: Bias-strength sweep | 5, 10, 15, and 20 percentage-point reductions | Measure detection as disparity increases |
| E3: Attribute comparison | Separate experiments for `sex` and `race` | Compare results across sensitive attributes |
| E4: Threshold sensitivity | DIR thresholds of 0.70, 0.80, and 0.90 | Measure changes in flags |
| E5: Baseline comparison | All four approaches on matched dataset variants | Compare detection capability and cost |
| E6: Natural-data audit | Original Adult dataset | Describe observed disparities without assuming ground-truth fairness |

Use at least five random seeds for each primary experimental condition where practical. Report the mean and standard deviation across repeated runs.

The threshold experiment is an evaluation setting; the default threshold remains 0.80 unless otherwise configured.

## 8. Evaluation Metrics

### 8.1 Detection rate

Measures the proportion of deliberately injected test cases that are correctly flagged.

Detection Rate = TP / (TP + FN)

Where:

- TP = injected test cases correctly flagged.
- FN = injected test cases not flagged.

### 8.2 False-positive rate

Measures the proportion of controlled negative-control cases incorrectly flagged.

False-Positive Rate = FP / (FP + TN)

Where:

- FP = negative-control cases incorrectly flagged.
- TN = negative-control cases correctly not flagged.

The binary flagging rules must be defined before the main experiment. Because profiling-only and manual methods may involve human review, record their review procedure and analyst time explicitly.

### 8.3 Demographic Parity Difference (DPD)

For the group positive outcome rates \(r_1, r_2, \ldots, r_n\):

DPD = maximum group rate − minimum group rate.

A larger value represents a larger observed difference in positive outcome rates. It does not explain the cause of that difference.

### 8.4 Disparate Impact Ratio (DIR)

DIR = minimum group positive outcome rate / maximum group positive outcome rate.

A value closer to 1 indicates more similar observed rates under this measure. A value below 0.80 will trigger a potential-disparity flag under the current default configuration.

If every group has a zero positive outcome rate, the ratio is undefined and must be handled explicitly.

The 0.80 threshold is a screening convention, not a universal legal or statistical conclusion.

### 8.5 Runtime

Measure elapsed time for each auditing approach on the same hardware and dataset variant.

Record automated execution time separately from human review time so that the comparison remains meaningful.

## 9. Experimental Procedure

1. Verify the dataset columns, target labels, sensitive groups, and current audit configuration.
2. Preserve the original dataset.
3. Generate controlled negative-control datasets using recorded random seeds.
4. Apply the predefined outcome-disparity injections to copies of the controls.
5. Save the injection metadata and verify the actual outcome-rate changes.
6. Run the four baselines on matched dataset variants.
7. Record output metrics, binary risk flags, execution time, and analyst time where applicable.
8. Repeat the experiment across the selected seeds.
9. Calculate detection rate and false-positive rate using the predeclared rules.
10. Compare baseline performance and document failure cases, limitations, and reproducibility details.

Reviewers evaluating profiling-only and manual-audit outputs should use a consistent rubric. If more than one reviewer is involved, record disagreements rather than silently combining different judgments.

## 10. Expected Outputs

The following are proposed deliverables. Generate them after confirming the actual implementation and output formats.

- `reports/experiment_results.csv` — per-run experiment results.
- `reports/experiment_summary.md` — summary of metrics, comparisons, and limitations.
- `reports/plots/` — plots of detection rate, false-positive rate, DPD, DIR, and runtime where appropriate.

Each experiment record should include the dataset variant, sensitive attribute, random seed, requested and achieved injection strength, baseline, configured threshold, observed metrics, risk flag, and runtime.

## 11. Reproducibility and Fair Comparison

- Use the same controlled dataset variants across the four baselines.
- Fix and record random seeds.
- Record Python and dependency versions.
- Keep the original dataset unchanged.
- Apply the same primary DIR threshold across comparable approaches.
- Define binary flagging criteria before examining the main results.
- Separate development experiments from final reported results.
- Report variation across repeated runs, not just one result.
- Do not describe synthetic experimental results as proof of real-world discrimination.

## 12. Limitations

- Synthetic label changes do not reproduce every mechanism that causes real-world bias.
- Randomized controls can retain small group-rate differences due to sampling variation.
- Profiling-only and manual methods may depend on reviewer judgment.
- DPD and DIR identify differences but do not establish their causes.
- Small groups can produce unstable estimates.
- Threshold choices can change the number of flagged cases.
- Dataset-level fairness results do not establish the fairness of a trained model.

## 13. Future Work

Potential extensions include:

- Intersectional analysis of `sex × race`, subject to adequate group sizes.
- Confidence intervals and uncertainty estimates.
- Proxy-feature risk analysis.
- Model-based evaluation with equalized odds.
- Validation on COMPAS and German Credit.
- Severity-ranked HTML/PDF reports.

The toolkit should be evaluated as a decision-support system that identifies potential fairness risks for further investigation.
