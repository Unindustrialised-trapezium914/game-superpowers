#!/usr/bin/env python3
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        raise ValueError('missing YAML frontmatter start')
    parts = text.split('\n---\n', 1)
    if len(parts) != 2:
        raise ValueError('missing YAML frontmatter end')
    front, body = parts
    meta = {}
    for line in front.removeprefix('---\n').splitlines():
        if not line.strip() or line.startswith('  ') or ':' not in line:
            continue
        k, v = line.split(':', 1)
        meta[k.strip()] = v.strip().strip('"')
    return meta, body

errors = []
count = 0
for d in sorted(SKILLS.iterdir()):
    if not d.is_dir():
        continue
    count += 1
    p = d / 'SKILL.md'
    if not p.exists():
        errors.append(f'{d.name}: missing SKILL.md')
        continue
    meta, body = parse_frontmatter(p.read_text(encoding='utf-8'))
    if meta.get('name') != d.name:
        errors.append(f"{d.name}: frontmatter name mismatch ({meta.get('name')})")
    if not NAME_RE.match(meta.get('name', '')):
        errors.append(f'{d.name}: invalid name')
    if not meta.get('description'):
        errors.append(f'{d.name}: missing description')
    if not body.strip():
        errors.append(f'{d.name}: empty body')
if errors:
    for e in errors:
        print('ERROR:', e)
    sys.exit(1)
print(f'Validated {count} skills successfully.')
