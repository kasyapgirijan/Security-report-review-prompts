# Shared Structured Output Contract

Prepend this contract when a review must be machine-readable or regression-tested.

```text
OUTPUT RULES

Return valid JSON only. Do not wrap JSON in Markdown. Do not add fields outside the supplied schema.

Use these evidence states:
- confirmed
- supported_inference
- unverified
- contradicted
- not_reviewable

Use these finding dispositions:
- accept
- accept_with_edits
- re_rate
- merge
- split
- downgrade
- withdraw
- not_reviewable

COVERAGE
- List every expected finding ID received.
- List every finding ID actually reviewed.
- List unreadable or truncated items.
- Set coverage.complete=true only when the expected and reviewed sets are equal and no material section is unreadable.
- Never issue APPROVE when coverage.complete=false.

TRACEABILITY
Every material conclusion and review defect must include an exact evidence locator such as page, section, finding ID, figure, screenshot, request, response, command, code location or artifact identifier.
Use an empty locator list only when evidence is absent, and explicitly mark the item unverified or not_reviewable.

CVSS
- Preserve the report's declared CVSS version.
- Do not silently convert versions.
- Change a metric only when a supplied evidence locator directly supports the new value.
- Unknown or environment-dependent values must remain unknown.
- Record the original vector, proposed vector and evidence for every changed metric.

CONFIDENCE
- high: direct, located evidence proves the material conclusion and no material contradiction exists.
- medium: most elements are direct, but one non-critical element is explicitly inferred.
- low: the conclusion depends on missing, indirect, ambiguous or potentially stale evidence.
- not_applicable: the item is outside scope or not reviewable.

Confidence is not a substitute for evidence status.
```

The canonical machine-readable structure is defined in `schemas/review-output.schema.json`.
