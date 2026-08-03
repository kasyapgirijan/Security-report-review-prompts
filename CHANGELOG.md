# Changelog

All notable changes to this repository are documented here.

## [0.2.0] — 2026-08-03

### Added

- Pinned `standards.lock.yml`
- Strict JSON Schema 2020-12 review-output contract
- Shared structured-output contract
- Security and data-handling policies
- Prompt and schema versioning policy
- Initial adversarial benchmark corpus and golden-assertion guidance

### Changed

- Hardened Analyst and Senior prompts with prompt-injection boundaries, complete-review ledgers and mandatory evidence locators
- Replaced unsafe or underspecified CVSS recalculation instructions with evidence-bound metric review
- Replaced unpinned “current” mobile-standard mappings with supplied or locked standard versions
- Added build-specific evidence requirements to Android and iOS focused reviews
- Strengthened executive-summary, retest and meta-review workflows

### Security

- Whole-report approval is prohibited when review coverage is incomplete
- Report content, payloads, commands, screenshots and embedded text are explicitly treated as untrusted evidence
- Sensitive-value reproduction and invented standards/product behavior are prohibited

## [0.1.0] — 2026-08-03

- Initial AppSec, NWPT, mobile and shared report-review prompt collection
