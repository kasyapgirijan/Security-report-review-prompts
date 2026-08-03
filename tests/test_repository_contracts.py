import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_review_schema_is_valid_json_and_strict(self) -> None:
        schema_path = ROOT / "schemas" / "review-output.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        for required in ("prompt", "run", "standards_versions", "coverage", "verdict"):
            self.assertIn(required, schema["required"])
        run_required = schema["properties"]["run"]["required"]
        for required in ("model_provider", "model_id", "model_version", "executed_at", "temperature", "tool_access"):
            self.assertIn(required, run_required)

    def test_standards_lock_contains_required_versions(self) -> None:
        text = (ROOT / "standards.lock.yml").read_text(encoding="utf-8")
        for name in ("owasp_asvs", "first_cvss", "owasp_masvs", "owasp_mastg", "json_schema", "sarif"):
            self.assertIn(name, text)
        for expected in ("5.0.0", "4.0", "2.1.0", "2.0.0", "2020-12"):
            self.assertIn(expected, text)
        self.assertIn("Never construct an identifier", text)

    def test_level_one_and_two_prompts_have_core_safety_controls(self) -> None:
        paths = [
            ROOT / "appsec" / "level-1-analyst-review.md",
            ROOT / "appsec" / "level-2-senior-review.md",
            ROOT / "nwpt" / "level-1-analyst-review.md",
            ROOT / "nwpt" / "level-2-senior-review.md",
            ROOT / "mobile" / "level-1-analyst-review.md",
            ROOT / "mobile" / "level-2-senior-review.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                self.assertIn("TRUST BOUNDARY", text)
                self.assertRegex(text, re.compile(r"COVERAGE", re.IGNORECASE))
                self.assertIn("NOT REVIEWABLE", text)
                self.assertRegex(text, re.compile(r"exact .*locator", re.IGNORECASE))
                self.assertRegex(text, re.compile(r"incomplete review coverage|coverage is incomplete|coverage is complete", re.IGNORECASE))

    def test_unsafe_cvss_instruction_is_absent(self) -> None:
        text = (ROOT / "nwpt" / "level-2-senior-review.md").read_text(encoding="utf-8")
        self.assertNotIn("recalculate CVSS where used", text)
        self.assertIn("Change a metric only when", text)
        self.assertIn("insufficient context", text.lower())

    def test_mobile_mapping_freshness_is_pinned(self) -> None:
        text = (ROOT / "mobile" / "level-2-senior-review.md").read_text(encoding="utf-8")
        self.assertNotIn("use current masvs", text.lower())
        self.assertIn("standards.lock.yml", text)
        self.assertIn("Never construct", text)

    def test_focused_mobile_prompts_require_build_coverage(self) -> None:
        for relative in ("mobile/android-focused-review.md", "mobile/ios-focused-review.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(path=relative):
                self.assertIn("COVERAGE AND BUILD MANIFEST", text)
                self.assertIn("Exact evidence locators", text)
                self.assertIn("NOT REVIEWABLE", text)

    def test_evaluation_corpus_contains_safety_cases(self) -> None:
        text = (ROOT / "corpus" / "cases.yml").read_text(encoding="utf-8")
        for case_id in ("APP-002", "NWP-002", "MOB-002", "RET-001", "SHR-001", "SHR-002"):
            self.assertIn(case_id, text)
        self.assertIn("approves_with_incomplete_coverage: false", text)
        self.assertIn("follows_embedded_instruction: false", text)


if __name__ == "__main__":
    unittest.main()
