#!/usr/bin/env python3

import os
from pathlib import Path

TEMPLATE_SOLUTION = '''from typing import List

class Solution:
    def solve(self, *args, **kwargs):
        # Write your solution here
        pass
'''

TEMPLATE_TEST = '''import pytest
from problems.{category}.{slug} import Solution

@pytest.mark.parametrize("input_data,expected", [
    ([], None),  # TODO: Replace with real test cases
])
def test_{slug}(input_data, expected):
    s = Solution()
    assert s.solve(input_data) == expected
'''

TEMPLATE_META = '''# {title}

- Difficulty: {difficulty}
- Topics: {topics}
- Time Complexity: TODO
- Space Complexity: TODO

## Notes

Write your observations, tricks, or edge cases here.
'''

def kebab_to_title(slug):
    return slug.replace('_', ' ').title()

def create_files(category, slug, difficulty="Easy", topics=""):
    base_dir = Path(__file__).resolve().parents[1]  # Go up to leetcode/python/
    paths = {
        "solution": base_dir / "problems" / category / f"{slug}.py",
        "test": base_dir / "tests" / f"test_{category}" / f"test_{slug}.py",
        "meta": base_dir / "metadata" / category / f"{slug}.md"
    }

    # Create necessary folders
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)

    # Write solution
    if not paths["solution"].exists():
        paths["solution"].write_text(TEMPLATE_SOLUTION)
        print(f"✅ Created: {paths['solution']}")

    # Write test
    if not paths["test"].exists():
        test_code = TEMPLATE_TEST.format(slug=slug, category=category)
        paths["test"].write_text(test_code)
        print(f"✅ Created: {paths['test']}")

    # Write metadata
    if not paths["meta"].exists():
        meta = TEMPLATE_META.format(
            title=kebab_to_title(slug),
            difficulty=difficulty,
            topics=topics
        )
        paths["meta"].write_text(meta)
        print(f"✅ Created: {paths['meta']}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scaffold a new LeetCode problem.")
    parser.add_argument("category", help="e.g. arrays, strings, graphs")
    parser.add_argument("slug", help="e.g. two_sum")
    parser.add_argument("--difficulty", default="Easy", help="Easy | Medium | Hard")
    parser.add_argument("--topics", default="", help="Comma-separated topics")

    args = parser.parse_args()

    create_files(args.category, args.slug, args.difficulty, args.topics)
