# Security Report Review Prompts

Evidence-driven prompts and assurance controls for reviewing security assessment reports before internal approval or client delivery.

**Current release: `0.2.0` — research-backed hardening foundation**

These prompts are intentionally strict. They are designed to expose weak evidence, unsupported impact, inflated severity, unsafe remediation, copy-paste residue, prompt injection and findings that cannot survive a technical client challenge.

They do **not** prove or disprove a vulnerability by themselves and do not replace expert validation, retesting or professional accountability.

## What changed in 0.2.0

The repository is no longer only a Markdown prompt collection. It now includes:

- Mandatory trust-boundary and review-coverage controls
- Evidence-bound CVSS review rules
- Pinned standards versions
- Strict JSON Schema 2020-12 output contract
- Security and data-handling policies
- Versioning and changelog
- Initial adversarial benchmark cases and golden-assertion guidance
- Static repository-contract tests and GitHub Actions validation

See `CHANGELOG.md` and `QUALITY-REVIEW.md`.

## Prompt collections

### `appsec/`
Web, API, source-assisted, SAST, DAST and business-logic assessment reports.

- `level-1-analyst-review.md`
- `level-2-senior-review.md`
- `level-3-principal-brutal-review.md`
- `finding-title-and-remediation-review.md`

### `nwpt/`
Internal, external, assumed-breach, segmentation and identity-focused network penetration testing reports.

- `level-1-analyst-review.md`
- `level-2-senior-review.md`
- `level-3-principal-brutal-review.md`
- `attack-path-and-evidence-review.md`

### `mobile/`
Android, iOS and cross-platform mobile security reports.

- `level-1-analyst-review.md`
- `level-2-senior-review.md`
- `level-3-principal-brutal-review.md`
- `android-focused-review.md`
- `ios-focused-review.md`

### `shared/`
Controls that apply across assessment types.

- `review-contract.md` — instruction/data boundary, traceability, coverage and evidence rules
- `output-contract.md` — structured evidence states, dispositions, CVSS and coverage rules
- `executive-summary-review.md` — reconciles management claims with complete finding coverage
- `retest-and-closure-review.md` — deterministic closure predicates
- `meta-review-security-review-prompt.md` — audits another report-review prompt before rewrite

## Assurance and evaluation

- `schemas/review-output.schema.json` — strict machine-readable review output
- `standards.lock.yml` — pinned standards and reference rules
- `corpus/cases.yml` — initial positive, negative and adversarial evaluation cases
- `goldens/` — required/prohibited assertion guidance
- `tests/test_repository_contracts.py` — static safety and consistency tests
- `.github/workflows/static-validation.yml` — read-only automated validation
- `DATA-HANDLING.md` — public-corpus and confidentiality policy
- `SECURITY.md` — security-sensitive reporting guidance
- `VERSIONING.md` — prompt and schema compatibility policy

## Review levels

- **Level 1 — Analyst:** checks completeness, basic credibility, evidence, clarity and actionability before senior QA.
- **Level 2 — Senior:** challenges technical validity, exploitability, risk consistency and root-cause remediation.
- **Level 3 — Principal / Brutal:** performs a final adversarial quality gate with explicit evidence labels, report coverage tracking, finding dispositions and client-defensibility tests.

“Brutal” means evidence-bound and difficult to fool—not hostile, theatrical or biased toward rejection.

## Recommended workflow

1. **Sanitize the material.** Remove or mask secrets, tokens, cookies, personal data, customer data and unnecessary internal identifiers.
2. **Confirm approved AI handling.** Do not paste an unredacted confidential report into an AI service that is not approved for that data.
3. **Choose the domain and review level.** Use Level 1 during author QA, Level 2 for technical peer review and Level 3 before delivery.
4. **Use the shared contracts.** Prepend `shared/review-contract.md`; use `shared/output-contract.md` for structured or regression-tested output.
5. **Supply context.** Include scope, assessment type, environment, tester position, build/version, roles, risk model and limitations.
6. **Demand coverage disclosure.** For long reports, require expected/reviewed finding ledgers and batch the report without issuing premature approval.
7. **Use pinned standards.** Preserve the report's historical standard version and do not invent or silently update identifiers.
8. **Review the reviewer.** Use the meta-review prompt before adopting a modified prompt.
9. **Human-validate the output.** AI review comments remain hypotheses until a qualified reviewer confirms them against evidence.

## Evidence language

- **CONFIRMED** — directly demonstrated by supplied evidence
- **SUPPORTED INFERENCE** — strongly implied but not directly demonstrated
- **UNVERIFIED** — plausible but insufficiently evidenced
- **CONTRADICTED** — conflicts with supplied evidence
- **NOT REVIEWABLE** — required material is missing or unreadable

Evidence state and reviewer confidence are different concepts. A reviewer may have high confidence that a claim is unverified.

## Finding dispositions

- Accept
- Accept with edits
- Re-rate
- Merge
- Split
- Downgrade to hardening/informational
- Withdraw as unsupported or false positive
- Not reviewable

## Finding-title formats

- `<Weakness> in <Affected Component>`
- `<Weakness> in <Parameter/Field> of <Endpoint/Function>`
- `<Material Qualifier> <Weakness> in <Component>`
- `Systemic <Control Weakness> Across <Defined Scope>`

Examples:

- `Missing Object-Level Authorization in Invoice Download API`
- `SQL Injection in sort Parameter of Product Search Endpoint`
- `Cross-Tenant Data Access in Report Export Function`
- `Systemic SMB Signing Weakness Across Internal Windows Servers`
- `Sensitive Data Stored in Android Application Logs`

Use outcome-led titles only when the outcome is directly demonstrated and necessary to describe the weakness accurately.

## Core principles

- Evidence before claims
- Exact evidence locators before reviewer certainty
- Complete coverage disclosure before approval
- Reproducibility before exploitability claims
- Attacker model before severity
- Root-cause remediation before compensating controls
- Demonstrated impact separated from credible extension and speculation
- No invented mappings, references, vectors, product behavior or implementation details
- WAF, EDR, MDM, CSP, pinning, RASP and monitoring are defence-in-depth unless they directly correct the documented root cause
- No numeric quality score without a defined rubric
- Symmetric concern for false acceptance and false rejection

## Run static validation

```bash
python3 -m unittest discover -s tests -v
```

The current tests verify the strict schema, standards lock, trust boundaries, coverage gates, evidence-locator requirements, safe CVSS language, mobile reference pinning and presence of adversarial benchmark cases.

## Current limitations

The repository is **ready for expert-assisted use with human validation**, not autonomous report approval.

Still needed for a stable `1.0.0` release:

- Full synthetic evidence fixtures for the seeded cases
- Two-reviewer human-adjudicated golden files
- Multi-model and repeated-run evaluation harness
- Precision/recall and critical-error thresholds
- Long-context and multimodal benchmark cases
- Dedicated API, SAST, DAST, cloud, Kubernetes, container, thick-client and IoT collections
- Signed release evaluation reports

## Contributing

Read `CONTRIBUTING.md`, `DATA-HANDLING.md`, `VERSIONING.md` and `SECURITY.md` before submitting a prompt, schema or corpus change.

## License

MIT for prompts, schemas and tooling. Dataset licensing will be declared separately for public corpus artifacts.
