# Security Report Review Prompts

Evidence-driven prompts for reviewing security assessment reports before internal approval or client delivery.

These prompts are intentionally strict. They are designed to expose weak evidence, unsupported impact, inflated severity, unsafe remediation, copy-paste residue and findings that cannot survive a technical client challenge.

They do **not** prove or disprove a vulnerability by themselves and do not replace expert validation, retesting or professional accountability.

## Collections

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

- `review-contract.md` — prompt-injection boundary, traceability, coverage and evidence rules
- `executive-summary-review.md` — reconciles management claims with findings
- `retest-and-closure-review.md` — determines whether remediation evidence actually closes findings
- `meta-review-security-review-prompt.md` — audits and rewrites another report-review prompt

## Review levels

- **Level 1 — Analyst:** checks completeness, basic credibility, evidence, clarity and actionability before senior QA.
- **Level 2 — Senior:** challenges technical validity, exploitability, risk consistency and root-cause remediation.
- **Level 3 — Principal / Brutal:** performs a final adversarial quality gate with explicit evidence labels, report coverage tracking, finding disposition and client-defensibility tests.

“Brutal” means evidence-bound and difficult to fool—not hostile, theatrical or biased toward rejection.

## Recommended workflow

1. **Sanitize the material.** Remove or mask secrets, tokens, cookies, personal data, customer data and unnecessary internal identifiers.
2. **Confirm approved AI handling.** Do not paste an unredacted confidential report into an AI service that is not approved for that data.
3. **Choose the domain and review level.** Use Level 1 during author QA, Level 2 for technical peer review and Level 3 before delivery.
4. **Add the shared contract when needed.** Prepend `shared/review-contract.md` to shorter prompts or custom prompts.
5. **Supply context.** Include scope, assessment type, environment, tester position, build/version, roles, risk model and relevant limitations.
6. **Demand coverage disclosure.** For long reports, require a reviewed/not-reviewed ledger and batch the report without issuing premature approval.
7. **Review the reviewer.** Use `shared/meta-review-security-review-prompt.md` before adopting a modified prompt.
8. **Human-validate the output.** AI review comments remain hypotheses until a qualified reviewer confirms them against the report and evidence.

## Evidence language

The hardened prompts use calibrated evidence states:

- **CONFIRMED** — directly demonstrated by supplied evidence
- **SUPPORTED INFERENCE** — strongly implied but not directly demonstrated
- **UNVERIFIED** — plausible but insufficiently evidenced
- **CONTRADICTED** — conflicts with supplied evidence
- **NOT REVIEWABLE** — required material is missing or unreadable

This is more defensible than arbitrary numeric confidence or an unexplained `/100` quality score.

## Finding dispositions

Principal prompts can recommend:

- Accept
- Accept with edits
- Re-rate
- Merge
- Split
- Downgrade to hardening/informational
- Withdraw as unsupported or false positive
- Not reviewable

## Suggested finding-title formats

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
- No invented mappings, references, vectors, product behaviour or implementation details
- WAF, EDR, MDM, CSP, pinning, RASP and monitoring are defence-in-depth unless they directly correct the documented root cause
- No numeric quality score without a defined rubric

## Important limitations

A language model may still:

- Miss visual or technical evidence
- Misinterpret framework or platform behaviour
- Produce plausible but incorrect remediation
- Lose context in large reports
- Apply outdated security knowledge
- Be manipulated by untrusted report content when guardrails are omitted

The final reviewer remains responsible for every accepted change and client-facing statement.

## Contributing

Contributions should include:

- Intended assessment type and review level
- Threat model and evidence requirements
- Anti-hallucination and coverage controls
- Clear output schema
- Residual limitations
- No real client data, credentials or proprietary report text

## License

MIT
