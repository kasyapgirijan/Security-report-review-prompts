# Security Report Review Prompts

Brutal, evidence-driven prompts for reviewing security assessment reports before client delivery.

## Collections

- `appsec/` — web, API, SAST, DAST and business-logic assessment reports
- `nwpt/` — internal and external network penetration testing reports
- `mobile/` — Android and iOS application security reports

## Review levels

- **Level 1 — Analyst:** completeness, clarity, evidence and basic remediation quality
- **Level 2 — Senior:** technical validation, exploitability, risk consistency and developer actionability
- **Level 3 — Principal / Brutal:** final client-delivery quality gate that attempts to reject unsupported findings

## How to use

1. Open the prompt matching the assessment type and review depth.
2. Paste the report or individual finding after the prompt.
3. Tell the model not to infer missing evidence.
4. Treat AI output as review assistance, not proof of vulnerability or a replacement for expert validation.

## Core principles

- Evidence before claims
- Reproducibility before severity
- Root-cause remediation before generic advice
- Clear titles identifying the vulnerability and affected component
- No invented facts, mappings, scores or exploit paths
- WAF, EDR, MDM and monitoring are defence-in-depth, not substitutes for fixing root cause

## Suggested finding title format

`<Vulnerability or control weakness> in <affected component, endpoint or function>`

Examples:

- `Missing Object-Level Authorization in Invoice Download API`
- `Stored Cross-Site Scripting in Customer Support Comments`
- `SMB Signing Not Enforced on Internal Windows Hosts`
- `Sensitive Data Stored in Android Application Logs`

## License

MIT
