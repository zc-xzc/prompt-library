#!/usr/bin/env python3
"""Validate text integrity and repository navigation without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml"}
ERRORS: list[str] = []


def report(path: Path, message: str) -> None:
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")


def validate_text_files() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as error:
            report(path, f"invalid UTF-8: {error}")
            continue
        if "\ufffd" in text:
            report(path, "contains a Unicode replacement character")
        if re.search(r"\?{3,}", text):
            report(path, "contains a suspicious run of question marks")
        if path.suffix.lower() == ".md":
            validate_markdown(path, text)


def validate_markdown(path: Path, text: str) -> None:
    fence_lines = sum(1 for line in text.splitlines() if line.startswith("```"))
    if fence_lines % 2:
        report(path, f"has an unmatched fenced code block ({fence_lines} fence lines)")

    for raw_target in re.findall(r"\]\(([^)]+)\)", text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:)", target):
            continue
        if not (path.parent / target).exists():
            report(path, f"broken local link: {raw_target}")


def validate_prompt_layout() -> None:
    prompts = ROOT / "prompts"
    if not prompts.is_dir():
        ERRORS.append("missing prompts directory")
        return
    for directory in prompts.iterdir():
        if not directory.is_dir():
            continue
        prompt = directory / f"{directory.name}.md"
        readme = directory / "README.md"
        if not prompt.is_file():
            ERRORS.append(f"missing prompt file: {prompt.relative_to(ROOT)}")
        if not readme.is_file():
            ERRORS.append(f"missing prompt README: {readme.relative_to(ROOT)}")


def main() -> int:
    validate_text_files()
    validate_prompt_layout()
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        return 1
    print("prompt-library validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
