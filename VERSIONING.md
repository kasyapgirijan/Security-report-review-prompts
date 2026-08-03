# Versioning Policy

This repository uses Semantic Versioning for prompt behavior, output schemas and evaluation contracts.

During initial development, releases remain in the `0.x` series.

## Version changes

- **Major:** incompatible output schema or prompt behavior; removed fields; changed evidence/disposition meaning; approval criteria changed incompatibly.
- **Minor:** backward-compatible prompt capability, domain collection, schema field or evaluation fixture.
- **Patch:** wording or safety correction that preserves the documented output contract.

Every runnable prompt should declare:

- Prompt ID
- Prompt version
- Domain
- Review level
- Required shared modules
- Output schema version
- Standards lockfile version

A prompt change is not considered an improvement until it passes the applicable regression corpus. Model/provider changes must be recorded as evaluation metadata, not hidden inside a prompt version.
