# Mobile Security Report Review — Level 1

```text
Review this Android or iOS security assessment report for basic QA. Do not summarize or invent missing evidence.

For every finding check:
- Title identifies the weakness and affected mobile component, API, storage location or platform control.
- Platform, app version/build, package/bundle ID, OS/device and test environment are stated.
- Evidence shows the exact behaviour using screenshots, proxy traffic, logs, decompiled code or runtime output as appropriate.
- Reproduction includes prerequisites, authentication, device state, root/jailbreak status, tools and exact steps.
- Impact matches the demonstrated attacker model: local user, malicious app, rooted/jailbroken device, network attacker or remote user.
- Severity accounts for platform sandboxing, required physical access, user interaction and backend controls.
- Remediation is actionable and separates mobile-client fixes from backend/API fixes.
- Secrets, tokens, PII, device identifiers and customer data are redacted.
- MASVS/MSTG, CWE and OWASP Mobile mappings are relevant and not forced.

For each defect output: Priority, finding/section, problem, why it matters, correction and example wording.

Verdict: PASS TO SENIOR REVIEW or RETURN TO AUTHOR.
```
