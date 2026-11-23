"""Offline tests for the generated apps mega-directory. No network access."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

APPS = Path(__file__).resolve().parents[1]
CATALOG = APPS / "data" / "catalog.json"
MASTER = APPS / "README.md"


class AppsCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not CATALOG.exists():
            raise unittest.SkipTest("apps catalog has not been generated yet")
        cls.data = json.loads(CATALOG.read_text(encoding="utf-8"))
        cls.entries = cls.data.get("entries") or []

    def test_catalog_reaches_target(self) -> None:
        self.assertGreaterEqual(
            len(self.entries),
            int(self.data.get("min_entries") or 5000),
            "apps directory is below the requested 5,000+ entry target",
        )
        self.assertEqual(self.data.get("entry_count"), len(self.entries))

    def test_entries_have_required_fields(self) -> None:
        required = {"id", "key", "name", "url", "description", "category", "type", "status", "sources", "indexed"}
        for entry in self.entries:
            with self.subTest(entry=entry.get("id")):
                self.assertFalse(required - set(entry), required - set(entry))
                self.assertTrue(entry["url"].startswith(("http://", "https://")), entry["url"])
                self.assertTrue(entry["sources"], entry["id"])

    def test_entries_are_unique(self) -> None:
        keys = [entry["key"] for entry in self.entries]
        ids = [entry["id"] for entry in self.entries]
        self.assertEqual(len(keys), len(set(keys)), "duplicate normalized identity found")
        self.assertEqual(len(ids), len(set(ids)), "duplicate directory id found")

    def test_count_maps_match_entries(self) -> None:
        categories: dict[str, int] = {}
        types: dict[str, int] = {}
        for entry in self.entries:
            categories[entry["category"]] = categories.get(entry["category"], 0) + 1
            types[entry["type"]] = types.get(entry["type"], 0) + 1
        self.assertEqual(self.data.get("categories"), categories)
        self.assertEqual(self.data.get("types"), types)

    def test_every_entry_has_a_directory(self) -> None:
        for entry in self.entries:
            readme = APPS / "tools" / self.slug(entry["category"]) / entry["id"] / "README.md"
            with self.subTest(entry=entry["id"]):
                self.assertTrue(readme.exists(), f"missing {readme}")
                content = readme.read_text(encoding="utf-8")
                self.assertIn(entry["url"], content)
                self.assertIn(entry["category"], content)
                self.assertIn(entry["type"], content)

    def test_master_readme_contains_every_url(self) -> None:
        content = MASTER.read_text(encoding="utf-8")
        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                self.assertIn(entry["url"], content)

    @staticmethod
    def slug(value: str) -> str:
        import re
        import unicodedata

        text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
        return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "entry"


if __name__ == "__main__":
    unittest.main()
