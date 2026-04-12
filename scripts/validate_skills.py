#!/usr/bin/env python3
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
MIRRORS = {
    '.agents/skills': ROOT / '.agents' / 'skills',
    '.claude/skills': ROOT / '.claude' / 'skills',
    'publish/clawhub': ROOT / 'publish' / 'clawhub',
}
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def split_frontmatter(text: str):
    if not text.startswith('---\n'):
        raise ValueError('missing YAML frontmatter start')
    parts = text.split('\n---\n', 1)
    if len(parts) != 2:
        raise ValueError('missing YAML frontmatter end')
    front, body = parts
    return front.removeprefix('---\n'), body

def parse_yaml_frontmatter(frontmatter: str):
    ruby = shutil.which('ruby')
    if not ruby:
        raise ValueError('ruby not found; strict YAML validation unavailable')
    script = """
require 'yaml'
require 'json'
begin
  data = YAML.safe_load(STDIN.read, permitted_classes: [], aliases: false) || {}
  puts JSON.generate(data)
rescue Psych::SyntaxError => e
  warn e.message
  exit 1
end
"""
    proc = subprocess.run(
        [ruby, '-e', script],
        input=frontmatter,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise ValueError(f'invalid YAML: {proc.stderr.strip()}')
    data = json.loads(proc.stdout)
    if not isinstance(data, dict):
        raise ValueError('frontmatter must parse to a mapping')
    return data

def extract_meta(data: dict):
    meta = {
        'name': data.get('name'),
        'description': data.get('description'),
    }
    metadata = data.get('metadata')
    if isinstance(metadata, dict):
        meta['metadata.version'] = metadata.get('version')
    return meta

errors = []
count = 0
skill_names = set()
for d in sorted(SKILLS.iterdir()):
    if not d.is_dir():
        continue
    count += 1
    skill_names.add(d.name)
    p = d / 'SKILL.md'
    if not p.exists():
        errors.append(f'{d.name}: missing SKILL.md')
        continue
    try:
        frontmatter, body = split_frontmatter(p.read_text(encoding='utf-8'))
        meta = extract_meta(parse_yaml_frontmatter(frontmatter))
    except ValueError as e:
        errors.append(f'{d.name}: {e}')
        continue
    if meta.get('name') != d.name:
        errors.append(f"{d.name}: frontmatter name mismatch ({meta.get('name')})")
    if not NAME_RE.match(meta.get('name', '')):
        errors.append(f'{d.name}: invalid name')
    if not meta.get('description'):
        errors.append(f'{d.name}: missing description')
    if not body.strip():
        errors.append(f'{d.name}: empty body')

for label, root in MIRRORS.items():
    if not root.exists():
        continue
    mirrored = {path.name for path in root.iterdir()}
    missing = sorted(skill_names - mirrored)
    extra = sorted(mirrored - skill_names)
    for name in missing:
        errors.append(f'{label}: missing {name}')
    for name in extra:
        errors.append(f'{label}: unexpected {name}')
if errors:
    for e in errors:
        print('ERROR:', e)
    sys.exit(1)
print(f'Validated {count} skills successfully.')
