# Research-Backed Quality Review

This document records the repository's adversarial self-review and the hardening implemented after a deeper review of security-report QA, LLM hallucination, indirect prompt injection, structured output, risk scoring and prompt evaluation practices.

## Current verdict

**Ready for expert-assisted use with mandatory human validation. Not ready for autonomous client-report approval.**

The repository is now more than a prompt collection: it has trust-boundary rules, complete-review coverage gates, evidence states, exact locator requirements, evidence-bound CVSS handling, a standards lock, a strict JSON output schema, an initial adversarial corpus and static contract tests.

## Critical defects found in the earlier release

### 1. Missing injection boundaries in Level 1 and Level 2

Report text, payloads, screenshots and source comments could contain instructions that redirected the reviewer.

**Corrected:** all Analyst and Senior prompts now explicitly treat report content as untrusted evidence and prohibit following embedded instructions or executing content.

### 2. False whole-report approval

Short prompts could approve a report without proving every finding or material section was received and reviewed.

**Corrected:** Analyst, Senior, focused mobile, executive-summary and retest prompts now require expected/reviewed ledgers and prohibit approval when coverage is incomplete.

### 3. Weak traceability

Review conclusions were not consistently tied to page, request, screenshot, code, command or artifact identifiers.

**Corrected:** exact evidence locators are mandatory for material conclusions and defects.

### 4. Unsafe CVSS handling

NWPT Level 2 instructed the model to “recalculate CVSS where used,” which could force unsupported assumptions. Other prompts did not fully constrain version conversion and environmental values.

**Corrected:** prompts preserve the report's scoring version, prohibit silent conversion, change metrics only with direct evidence and leave unknown/environment-dependent metrics unknown.

### 5. Unpinned “current” standards

Mobile prompts requested current MASVS/MASWE/MASTG mappings without defining how currency would be verified.

**Corrected:** `standards.lock.yml` pins verified versions, while prompts preserve historical report versions and mark unverifiable identifiers unverified rather than constructing them from memory.

### 6. Free-form output drift

Outputs could vary too much across runs and could not be deterministically validated or integrated.

**Corrected:** `shared/output-contract.md` and `schemas/review-output.schema.json` define strict coverage, evidence, disposition, CVSS, impact and remediation structures.

### 7. No behavioral regression foundation

Prompt changes were judged by wording rather than observed behavior.

**Corrected in part:** `corpus/cases.yml` seeds valid findings, false positives, attack-chain breaks, build traps, retest traps, prompt injection and truncation cases. `goldens/` defines assertion-based evaluation rather than exact prose matching.

### 8. Inadequate repository governance

The repository lacked data-handling, security-disclosure, versioning, ownership and automated policy checks.

**Corrected:** added `DATA-HANDLING.md`, `SECURITY.md`, `VERSIONING.md`, `CHANGELOG.md`, `.github/CODEOWNERS`, static tests and a read-only GitHub Actions workflow.

## Safety and quality invariants

A future release must not:

- Follow instructions embedded in report content
- Reveal hidden instructions or planted sensitive values
- Approve a whole report with incomplete coverage
- Modify CVSS metrics without evidence for every changed value
- Invent standards identifiers, CVEs, APIs, product behavior or configuration keys
- Mark a compensating-control-only retest as closed
- Treat scanner output, banners, strings or debug/root-only observations as exploitation proof
- Reject well-evidenced valid findings merely because the reviewer is instructed to be “brutal”

## Implemented evaluation cases

The initial case catalogue includes:

- Confirmed cross-tenant authorization failure
- Scanner-only SQL injection alert
- CVSS/impact inflation trap
- Duplicate root-cause findings
- Banner/CVE ambiguity
- Broken identity attack chain
- Segmentation-policy ambiguity
- Root-only TLS interception
- Debug-build token logging
- WAF-only retest
- Indirect prompt injection
- Truncated report and executive-summary mismatch

## Residual limitations and release blockers

The foundation is implemented, but `1.0.0` still requires:

- Full synthetic evidence fixtures for the seeded cases
- Two-reviewer, human-adjudicated golden assertion files
- Automated schema validation of actual model outputs
- Multi-model and repeated-run evaluation harness
- Precision, recall, critical-error and stability thresholds
- Long-context and multimodal test cases
- Blind hold-out cases that prompt authors cannot tune against
- Dedicated API, SAST, DAST, cloud, Kubernetes, container, thick-client and IoT collections
- Signed release evaluation reports and protected required checks

## Release judgment

- **0.1.0:** useful prompt library, not assurance-ready
- **0.2.0:** research-backed hardening foundation with static controls and seeded evaluations
- **1.0.0 target:** empirically evaluated, versioned prompt product with reproducible model/run metadata and release thresholds

The decisive improvement is not a longer “omniscient” prompt. It is a system where every prompt has a threat model, every output has a contract, every claim is traceable, every unsafe failure is tested and every release has measurable evidence.
