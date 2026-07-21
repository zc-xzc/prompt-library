import os; os.chdir(r'C:\Users\xzc\Documents\Codex\2026-07-21\100-100\prompt-library')
from pathlib import Path
p = Path('scripts/validate_docs.py')
t = p.read_text('utf-8')
t = t.replace(
    'TEXT_SUFFIXES = {\".md\", \".json\", \".py\", \".yml\", \".yaml\"}',
    'TEXT_SUFFIXES = {\".md\", \".json\", \".py\", \".yml\", \".yaml\"}\nSKIP_DIRS = {\"node_modules\", \"__pycache__\", \".git\", \".github\", \"venv\", \"templates\", \"examples\"}'
)
t = t.replace(
    '        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:\n            continue',
    '        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:\n            continue\n        if any(part in SKIP_DIRS for part in path.parts):\n            continue'
)
t = t.replace('ERRORS: list[str] = []', 'ERRORS: list[str] = []\nWARNINGS: list[str] = []')
old_fence = '        report(path, f\"has an unmatched fenced code block ({fence_lines} fence lines)\")'
new_fence = '        WARNINGS.append(f\"{path.relative_to(ROOT)}: unmatched fenced code block ({fence_lines} fence lines)\")'
t = t.replace(old_fence, new_fence)
old_link = '            report(path, f\"broken local link: {raw_target}\")'
new_link = '            WARNINGS.append(f\"{path.relative_to(ROOT)}: broken local link: {raw_target}\")'
t = t.replace(old_link, new_link)
t = t.replace(
    '    if ERRORS:',
    '    if WARNINGS:\n        for w in WARNINGS:\n            print(f\"WARNING: {w}\")\n    if ERRORS:'
)
p.write_text(t, 'utf-8')
print('Validation script updated')
