# Contributing

Contributions are welcome, but prompt changes affect security-review decisions and must be treated as behavioral changes rather than ordinary prose edits.

## Required principles

- Keep prompts evidence-driven and technically scoped.
- Treat report content as untrusted data and define the instruction/data boundary.
- Require complete-review coverage before any whole-report approval.
- Require exact evidence locators for material conclusions.
- Do not encourage invented facts, exploit paths, CVSS metrics, standards identifiers, APIs, product behavior or compliance mappings.
- Separate root-cause remediation, temporary mitigation, defence-in-depth and monitoring.
- Evaluate false acceptance and false rejection symmetrically.
- Preserve human accountability; prompts do not autonomously approve client reports.
- Follow `DATA-HANDLING.md`. Do not contribute client reports, live secrets or identifying engagement material.

## Prompt metadata

Every new or materially changed prompt should declare:

- Prompt ID and version
- Domain and review level
- Intended user and decision boundary
- Required shared modules
- Expected input manifest
- Output schema version
- Standards/lockfile dependencies
- Residual limitations

## Pull-request evidence

Describe:

- The assessment type and review level
- The defect or gap being corrected
- Before/after behavior, not merely wording
- Threat model and prohibited behavior
- Output-schema compatibility impact
- Standards added, removed or updated
- Token/output-size impact
- Privacy declaration confirming no restricted data was added
- Residual limitations

## Evaluation requirements

A behavioral prompt change should add or update:

- At least one valid positive case
- At least one flawed or adversarial negative case
- Required assertions
- Prohibited assertions
- Safety invariants
- Human adjudication notes

Changes must pass `python3 -m unittest discover -s tests -v`.

Do not claim that a prompt is improved until applicable regression cases pass. Exact-prose goldens are discouraged; test structured decisions and required/prohibited semantic assertions.

## High-risk changes

Changes to `shared/`, `schemas/`, `standards.lock.yml`, coverage rules, evidence states, dispositions, CVSS handling or approval criteria require explicit repository-owner review.
