# Evaluation Corpus

The public corpus begins with adversarial case specifications in `cases.yml`. Full evidence fixtures should be added only when they are synthetic or irreversibly anonymized under `DATA-HANDLING.md`.

## Case design

A useful case contains:

- Stable case ID and domain
- Synthetic report or finding evidence
- Seeded defect or valid security claim
- Required assertions
- Prohibited assertions
- Safety invariants
- Applicable prompt IDs
- Human adjudication notes

Balance valid findings and flawed findings. A strict prompt that rejects everything is also failing.

## Minimum adversarial categories

- Valid, well-evidenced finding
- Scanner-only false positive
- Inflated title or severity
- Broken attack chain
- Duplicate root causes
- Missing production-build evidence
- Compensating-control-only retest
- Prompt injection embedded in report content
- Truncated report and false whole-report approval
- Planted sensitive value that must not be repeated

Do not use exact prose matching as the primary golden test. Validate required and prohibited semantic assertions and structured enum fields.
