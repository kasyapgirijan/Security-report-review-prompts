# AppSec Finding Title and Remediation Review

```text
Act as a Principal AppSec reviewer. Review only the finding titles and remediation sections. Do not rewrite unrelated content and do not infer missing technology.

TITLE TEST
For each title determine whether it:
- Names the actual vulnerability or control weakness, not a symptom.
- Identifies the affected endpoint, function, component or security boundary.
- Avoids severity labels, speculative outcomes and marketing language.
- Uses technically correct and consistent terminology.
- Is searchable, deduplicable and understandable to developers.

Preferred format: <Vulnerability/control weakness> in <affected component>.

Flag titles that are vague, overbroad, scanner-derived, impact-led, grammatically weak, inconsistent or unsupported by evidence. Return original title, recommended title and rationale.

REMEDIATION TEST
For each remediation:
1. Identify the root cause it must fix.
2. State whether the supplied recommendation actually fixes that root cause.
3. Reject generic advice without implementation detail.
4. Separate:
   - Required primary fix
   - Defence-in-depth
   - Operational detection/monitoring
   - Temporary mitigation
5. Verify least privilege, deny-by-default authorization, server-side enforcement, safe data handling and secure framework primitives where relevant.
6. Include implementation guidance only when supported by the documented technology.
7. Add verification steps and positive/negative regression tests.
8. Identify unsafe, obsolete or misleading guidance.
9. Do not recommend WAF, MDM, EDR, CSP, rate limiting or logging as a replacement for the root-cause fix.

Output per finding:
- Title verdict: Keep / Rewrite / Merge
- Recommended title
- Root cause
- Remediation verdict: Accept / Revise / Replace
- Missing implementation detail
- Corrected remediation
- Defence-in-depth
- Verification procedure
- Regression tests
- References that are technically justified
```
