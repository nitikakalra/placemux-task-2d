# Phase 2 Task 4 – Match Explainability

## Overview

This project implements an explainable AI pipeline for candidate-job matching. Instead of only predicting a match score, the system explains why a candidate was matched by identifying matched skills, missing skills, score breakdown, and a hiring recommendation.

The project also evaluates the matching system using standard evaluation metrics and logs experiment results for reproducibility.

---

## Features

- Resume and Job dataset loading
- Skill extraction from resumes and job descriptions
- Skill matching
- Baseline skill overlap calculation
- Explainable candidate recommendations
- Matched skills identification
- Missing skills identification
- Score breakdown
- Hiring recommendation
- Candidate shortlisting
- Top-5 candidate ranking
- Edge case handling
- Evaluation metrics
- Experiment logging
- JSON result export

---

## Project Structure

```
.
│── data/
│   ├── jobs.csv
│   └── resumes.csv
│
│── experiments/
│   └── experiment_log.json
│
│── outputs/
│   ├── explanation_result.json
│   ├── shortlist.json
│   └── metrics.json
│
│── src/
│   ├── baseline.py
│   ├── data_summary.py
│   ├── decision.py
│   ├── evaluation.py
│   ├── explainability.py
│   ├── logger.py
│   ├── matcher.py
│   ├── metrics.py
│   ├── preprocessing.py
│   ├── save_results.py
│   ├── shortlisting.py
│   └── skills.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Workflow

1. Load datasets
2. Extract candidate skills
3. Extract job skills
4. Compare skills
5. Calculate baseline score
6. Generate explainable recommendation
7. Rank candidates
8. Evaluate performance
9. Save outputs
10. Log experiment

---

## Evaluation Metrics

The system reports:

- Precision
- Recall
- False Positive Rate
- Validation Samples

---

## Explainability Output

For every recommendation the system provides:

- Match Score
- Matched Skills
- Missing Skills
- Score Breakdown
- Recommendation
- Shortlisting Decision

---

## Output Files

outputs/

- explanation_result.json
- shortlist.json
- metrics.json

experiments/

- experiment_log.json

---

## Run

```bash
pip install -r requirements.txt

python main.py
```

---

## Future Improvements

- Semantic skill matching using embeddings
- Experience and education extraction from resumes
- Explainability dashboard
- SHAP/LIME based explanations
- Machine learning ranking models