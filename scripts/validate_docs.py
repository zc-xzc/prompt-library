#!/usr/bin/env python3
"""Validate text integrity and repository navigation without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml"}
SKIP_DIRS = {"node_modules", "__pycache__", ".git", ".github", "venv", ".venv", "env", "templates", "examples"}
ERRORS: list[str] = []
WARNINGS: list[str] = []


def report(path: Path, message: str) -> None:
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")


def validate_text_files() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
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
        WARNINGS.append(f"{path.relative_to(ROOT)}: unmatched fenced code block ({fence_lines} fence lines)")

    for raw_target in re.findall(r"\]\(([^)]+)\)", text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:)", target):
            continue
        if re.search(r"[\[\]=:]", target) or "../../" in target:
            continue
        candidates = [
            path.parent / target,
            path.parent.parent / target,
        ]
        if "reference/" in target:
            candidates.append(path.parent / target.replace("reference/", "references/", 1))
        if "references/" in target:
            candidates.append(path.parent / target.replace("references/", "reference/", 1))
        if any(c.exists() for c in candidates):
            continue
        if not (path.parent / target).exists():
            WARNINGS.append(f"{path.relative_to(ROOT)}: broken local link: {raw_target}")


def validate_skills_structure() -> None:
    skills = ROOT / "skills"
    if not skills.is_dir():
        ERRORS.append("missing skills directory")
        return
    for domain in skills.iterdir():
        if not domain.is_dir():
            continue
        domain_readme = domain / "README.md"
        if not domain_readme.is_file():
            ERRORS.append(f"missing domain README: {domain_readme.relative_to(ROOT)}")
        for category in domain.iterdir():
            if not category.is_dir():
                continue
            category_readme = category / "README.md"
            if not category_readme.is_file():
                ERRORS.append(f"missing category README: {category_readme.relative_to(ROOT)}")


def main() -> int:
    validate_text_files()
    validate_skills_structure()
    if WARNINGS:
        for w in WARNINGS:
            print(f"WARNING: {w}")
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        return 1
    print("prompt-library validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
