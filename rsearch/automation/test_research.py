"""Offline unit tests for the rsearch automation. No network access is used."""
from __future__ import annotations

import unittest

import refresh_catalog as rc


class NormalizationTests(unittest.TestCase):
    def test_urls_and_repos_collapse_to_one_key(self) -> None:
        self.assertEqual(
            rc.norm_key("https://GitHub.com/Some.Repo/Tool.git/"),
            rc.norm_key("https://github.com/some-repo/tool"),
        )
        self.assertEqual(rc.norm_key("HTTP://WWW.Example.org/path/?a=1#b"), "example.org/path")

    def test_name_and_url_of_same_tool_share_key_set(self) -> None:
        tool = {
            "id": "x",
            "name": "Example Tool",
            "url": "https://example.org/tool",
            "aliases": ["exampletool"],
        }
        keys = rc.tool_keys(tool)
        self.assertIn("exampletool", keys)
        self.assertIn("example.org/tool", keys)


class RegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = rc.load_json(rc.REGISTRY)
        self.exclusions = rc.load_json(rc.EXCLUSIONS)

    def test_registry_is_valid_and_deduplicated(self) -> None:
        self.assertEqual(rc.validate(self.registry, self.exclusions), [])

    def test_no_new_tool_duplicates_a_legacy_tool(self) -> None:
        legacy = {rc.norm_key(item["name"]) for item in self.exclusions["tools"]}
        for tool in self.registry["tools"]:
            for key in rc.tool_keys(tool):
                self.assertNotIn(key, legacy, f"{tool['id']} duplicates legacy identity {key}")

    def test_every_tool_has_primary_evidence(self) -> None:
        for tool in self.registry["tools"]:
            self.assertTrue(tool["evidence"], tool["id"])
            self.assertTrue(all(str(u).startswith("https://") for u in tool["evidence"]), tool["id"])

    def test_catalog_contains_every_tool(self) -> None:
        rendered = rc.render_catalog(self.registry, "2026-01-01T00:00:00Z")
        for tool in self.registry["tools"]:
            self.assertIn(tool["name"], rendered)


if __name__ == "__main__":
    unittest.main()
