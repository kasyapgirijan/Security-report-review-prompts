# Security Policy

Report prompt-injection bypasses, secret-disclosure behavior, unsafe corpus content, malicious workflow changes or other security-sensitive defects privately before opening a public issue.

## What to include

- Affected prompt or file and version/commit
- Reproduction input using synthetic data
- Observed unsafe behavior
- Expected safe behavior
- Model/provider/version and relevant run settings
- Whether sensitive data was exposed or a false approval was produced

Do not include real client material, live secrets or confidential reports in a disclosure.

## High-priority security defects

- Following instructions embedded inside report content
- Revealing system instructions, hidden context or planted secrets
- Approving a report with incomplete review coverage
- Reproducing credentials, tokens or unredacted sensitive values
- Inventing CVSS changes, standards identifiers or product capabilities in a way that affects a client-facing decision
- CI changes that expose repository or provider credentials to untrusted pull requests

Until a private reporting channel is configured, contact the repository owner through their GitHub profile without posting exploit details publicly.
