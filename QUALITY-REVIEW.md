# Adversarial Self-Review

This document records a critical review of the repository’s first release and the hardening applied afterward.

## Initial verdict

**Useful foundation, not principal-grade.**

The original prompts covered important security-report sections, but they behaved primarily as broad checklists. They could produce confident-looking reviews without proving that the model had reviewed the complete report or tied each conclusion to exact evidence.

## Critical defects found

### 1. No prompt-injection boundary

The prompts did not explicitly treat report content, payloads, screenshots and embedded text as untrusted data. A malicious or accidental instruction inside a report could redirect the reviewer.

**Correction:** added explicit input-boundary rules to the Level 3 prompts and `shared/review-contract.md`.

### 2. No complete-coverage control

A model could review the visible portion of a long report and still issue an overall approval.

**Correction:** Level 3 prompts now require a coverage statement, finding inventory, reviewed/not-reviewed disclosure and an incomplete-coverage verdict.

### 3. Weak traceability

The original prompts asked whether evidence existed but did not force each review conclusion to cite a page, figure, request, response, command or code locator.

**Correction:** exact evidence locators are now mandatory, with “Traceability missing” used when the report lacks them.

### 4. False precision

Arbitrary 1–10 category scores and an overall `/100` score looked rigorous without a defined rubric, weights or thresholds.

**Correction:** removed numeric scoring from hardened prompts. Replaced it with dispositions, evidence states, confidence and explicit blocker criteria.

### 5. Unsafe CVSS instruction

“Recalculate every metric” could force guesses where attacker context or environmental facts were absent.

**Correction:** recalculation is now allowed only when evidence supports every changed metric. Unknown and environment-dependent metrics must remain unknown.

### 6. Rejection bias

“Attempt to reject the report” can make a reviewer performatively hostile and increase false-negative or pedantic output.

**Correction:** prompts now require skeptical but fair review: reject unsupported claims while also identifying understated impact or missing remediation when evidence supports it.

### 7. No calibrated evidence language

The original binary phrasing did not consistently distinguish direct proof, inference, speculation, contradiction and missing evidence.

**Correction:** introduced CONFIRMED, SUPPORTED INFERENCE, UNVERIFIED, CONTRADICTED and NOT REVIEWABLE states.

### 8. Insufficient finding disposition

The original outputs focused on defects but did not provide a consistent decision for the finding itself.

**Correction:** Level 3 prompts now support accept, edit, re-rate, merge, split, downgrade, withdraw and not-reviewable dispositions.

### 9. Weak remediation lifecycle

Root-cause remediation was required, but ownership, temporary-control expiry, rollout, migration, rollback and objective closure evidence were incomplete.

**Correction:** remediation review now separates primary fix, temporary mitigation, defence-in-depth and monitoring, with rollout and retest acceptance criteria.

### 10. Missing retest and management-review workflows

The repository lacked prompts for closure evidence and executive-summary reconciliation.

**Correction:** added shared retest/closure and executive-summary review prompts.

### 11. Mobile platform detail was too compressed

The mobile prompt mixed Android and iOS controls without enough platform-specific decision logic.

**Correction:** expanded the principal mobile prompt and added focused Android and iOS review prompts.

### 12. Network attack paths lacked an edge-by-edge output model

The NWPT prompt mentioned attack-path validation but did not force each transition to be represented and independently proven.

**Correction:** added a focused attack-path and evidence prompt with PROVEN, PARTIALLY PROVEN, ASSUMED, BROKEN and NOT REVIEWABLE edge states.

## Residual limitations

The repository is stronger, but important work remains:

- No anonymized sample reports with expected “golden” review output
- No automated prompt regression or model-comparison test suite
- No machine-readable JSON output schemas
- No dedicated cloud, container, Kubernetes, thick-client, desktop, IoT or source-code-review collections
- No dedicated API-only, SAST-only or DAST-only focused prompt
- No controlled benchmark for false-positive and false-negative reviewer behaviour
- Standards and mappings are not version-pinned; external references still require verification at use time
- Long outputs may still cause a model to skip checks unless reports are reviewed in batches
- Screenshot, diagram and table interpretation remains model-dependent
- A strong prompt cannot compensate for missing evidence, an unqualified reviewer or an unapproved data-handling workflow

## Current verdict

**Ready for expert-assisted use with human validation. Not suitable for autonomous approval of client reports.**

The next quality milestone should be a small anonymized evaluation set containing strong findings, weak findings, deliberate false positives, severity traps, copy-paste residue and incomplete evidence. Each prompt change should be tested against that set before release.
