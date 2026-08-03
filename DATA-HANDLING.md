# Data Handling Policy

This repository is public. Do not contribute real client reports, reusable exploit material, credentials or confidential assessment evidence.

## Required rules

1. **Synthetic first.** Prefer entirely synthetic organizations, applications, hosts, users, data and evidence.
2. **No live secrets.** Passwords, hashes, session cookies, bearer tokens, API keys, private keys and reusable certificates are prohibited.
3. **No direct identifiers.** Remove client names, employee names, email addresses, customer identifiers, ticket IDs, internal project names and contract references.
4. **Replace infrastructure fingerprints.** Replace public/internal IPs, domains, account IDs, tenant IDs, resource IDs, hostnames and unusual architecture labels.
5. **Preserve only security semantics.** Redaction may retain roles, tenant separation, ownership relationships and attack-path structure, but not identifying values.
6. **Two-person review for derived fixtures.** One contributor sanitizes; a second reviewer verifies that the source cannot reasonably be reconstructed.
7. **Automated scanning.** Proposed fixtures must pass secret and high-entropy scanning before merge.
8. **Provenance.** Every fixture must declare whether it is synthetic, transformed or derived, along with its author, licence and review date.
9. **Approved AI handling only.** Confidential material must not be sent to an external model provider without explicit organizational approval and appropriate data-processing terms.
10. **Minimize exploit detail.** Include only what is necessary to test review behavior; remove operationally reusable credentials and unnecessary destructive steps.

## Public corpus rule

Public fixtures must be synthetic or irreversibly anonymized and approved for release. When in doubt, do not publish the material.
