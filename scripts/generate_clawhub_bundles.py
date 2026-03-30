#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import pathlib
import re
import shutil
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PUBLISH_DIR = ROOT / "publish" / "clawhub"
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
DEFAULT_VERSION = "1.1.0"
PACKAGE_DATE = "2026-03-30"
SPEC_VERSION = "agentskills.io/1.0"
LICENSE_ID = "MIT"

FRONTMATTER_SPLIT = "\n---\n"
SHARED_REF_RE = re.compile(r"(?P<quote>`)(\.\./\.\./(?P<path>(?:shared|schemas)/[^`]+))`")
SKILL_REF_RE = re.compile(r"`(?P<skill>[a-z0-9]+(?:-[a-z0-9]+)*)`")


@dataclass
class SkillBundle:
    name: str
    description: str
    version: str
    source_path: pathlib.Path
    body: str
    raw_skill_text: str


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n") or FRONTMATTER_SPLIT not in text:
        raise ValueError("invalid frontmatter")
    frontmatter, body = text.split(FRONTMATTER_SPLIT, 1)
    meta: dict[str, str] = {}
    current_parent = None
    for line in frontmatter.removeprefix("---\n").splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current_parent == "metadata" and ":" in line:
            key, value = line.strip().split(":", 1)
            meta[f"metadata.{key.strip()}"] = value.strip().strip('"')
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_parent = key.strip()
        meta[current_parent] = value.strip().strip('"')
    return meta, body


def load_skill(skill_dir: pathlib.Path) -> SkillBundle:
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    meta, body = parse_frontmatter(skill_text)
    return SkillBundle(
        name=meta["name"],
        description=meta["description"],
        version=meta.get("metadata.version", DEFAULT_VERSION),
        source_path=skill_dir,
        body=body,
        raw_skill_text=skill_text,
    )


def compute_hash(path: pathlib.Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


def extract_skill_dependencies(text: str, self_name: str) -> list[str]:
    candidates = {
        match.group("skill")
        for match in SKILL_REF_RE.finditer(text)
        if match.group("skill").startswith("game-") or match.group("skill") == "using-game-superpowers"
    }
    return sorted(skill for skill in candidates if skill != self_name and (SKILLS_DIR / skill).is_dir())


def copy_referenced_assets(skill: SkillBundle, package_dir: pathlib.Path) -> list[pathlib.Path]:
    copied: list[pathlib.Path] = []
    rewritten = skill.raw_skill_text

    for match in SHARED_REF_RE.finditer(skill.raw_skill_text):
        rel_path = pathlib.Path(match.group("path"))
        src = ROOT / rel_path
        dest = package_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied.append(dest)
        rewritten = rewritten.replace(match.group(2), f"./{rel_path.as_posix()}")

    (package_dir / "SKILL.md").write_text(rewritten, encoding="utf-8")
    return copied


def build_examples(skill: SkillBundle) -> list[str]:
    title = skill.name.replace("-", " ")
    return [
        f'Use `{skill.name}` for this game project and keep the output evidence-based.',
        f'Apply `{skill.name}` to improve or assess an existing browser game in a focused way.',
        f'Use `{skill.name}` as part of a larger Game Superpowers workflow when the request clearly matches {title}.',
    ]


def build_readme(skill: SkillBundle, dependencies: list[str]) -> str:
    examples = build_examples(skill)
    dependency_block = (
        "\n".join(f"- `{dependency}`" for dependency in dependencies)
        if dependencies
        else "- None"
    )
    return f"""# {skill.name}

Part of the **Game Superpowers** skill system.

## Summary

{skill.description}

## Recommended usage

- {examples[0]}
- {examples[1]}
- {examples[2]}

## Companion skills

{dependency_block}

## Source of truth

This publish bundle is derived from the Game Superpowers source repository.
Canonical authoring lives in:

```text
skills/{skill.name}/SKILL.md
```

## Notes

- This bundle is published for OpenClaw / ClawHub distribution.
- The Game Superpowers repository also supports Claude Code and Codex distributions.
- If a workflow references companion skills, install those companion skills as separate bundles.
"""


def build_examples_doc(skill: SkillBundle) -> str:
    prompts = build_examples(skill)
    return f"""# Usage Examples

## Example prompts

- {prompts[0]}
- {prompts[1]}
- {prompts[2]}

## Expected behavior

- Load the skill instructions from `SKILL.md`.
- Use any packaged `shared/` references when the skill body points to them.
- If the workflow calls for companion skills, tell the user which companion skills should be installed or invoked next.
"""


def build_smoke_test(skill: SkillBundle, dependencies: list[str]) -> str:
    dependency_line = ", ".join(dependencies[:8]) if dependencies else "none"
    return f"""# Smoke Test

Bundle: `{skill.name}`
Version: `{skill.version}`

## Prompt

Use `{skill.name}` on a fitting game-development task.

## Expected checks

- The agent recognizes the skill's stated purpose.
- The agent uses packaged references when `SKILL.md` points to `./shared/...`.
- The agent does not claim companion skills are bundled implicitly when they are separate installs.
- Companion skills referenced in this bundle: {dependency_line}
"""


def build_changelog(skill: SkillBundle) -> str:
    return f"""# Changelog

## {skill.version} — {PACKAGE_DATE}

- Initial ClawHub publish bundle generated from `skills/{skill.name}/SKILL.md`.
- Added bundle metadata, README, and MANIFEST for OpenClaw / ClawHub distribution.
"""


def build_manifest(
    skill: SkillBundle,
    package_dir: pathlib.Path,
    dependencies: list[str],
    files: list[pathlib.Path],
) -> str:
    file_entries = []
    for path in sorted(files):
        rel = path.relative_to(package_dir).as_posix()
        role = "reference"
        if rel == "SKILL.md":
            role = "skill"
        elif rel == "README.md":
            role = "reference"
        elif rel == "CHANGELOG.md":
            role = "reference"
        file_entries.append(
            "  - path: {path}\n"
            "    role: {role}\n"
            "    version: {version}\n"
            "    hash: {hash}\n"
            "    note: {note}".format(
                path=rel,
                role=role,
                version=1 if role != "skill" else 1,
                hash=compute_hash(path),
                note=manifest_note(rel, role),
            )
        )

    dependency_lines = "\n".join(f"  - {dependency}" for dependency in dependencies) or "  []"
    return f"""bundle: {skill.name}
bundle_version: {skill.version}
bundle_date: {PACKAGE_DATE}
license: {LICENSE_ID}
description: >
  {skill.description}
compatibility:
  designed_for:
    surfaces:
      - chat
      - cli
      - ide
    capabilities:
      - local filesystem access
      - markdown skill bundles
      - reusable game-development workflows
  tested_on:
    - platform: OpenClaw
      surface: ClawHub
      status: pending
      date: {PACKAGE_DATE}
    - platform: Claude Code
      surface: CLI
      status: pass
      date: {PACKAGE_DATE}
    - platform: Codex
      surface: CLI
      status: pass
      date: {PACKAGE_DATE}
  spec_version: {SPEC_VERSION}
  frontmatter_mode: metadata
dependencies:
{dependency_lines}
files:
{chr(10).join(file_entries)}
"""


def manifest_note(rel_path: str, role: str) -> str:
    if role == "skill":
        return "Canonical skill definition for this publish bundle"
    if rel_path == "README.md":
        return "ClawHub-facing usage and context"
    if rel_path == "CHANGELOG.md":
        return "Bundle release notes"
    return f"Referenced support file: {rel_path}"


def generate_bundle(skill: SkillBundle) -> None:
    package_dir = PUBLISH_DIR / skill.name
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)

    dependencies = extract_skill_dependencies(skill.raw_skill_text, skill.name)
    referenced_files = copy_referenced_assets(skill, package_dir)

    readme_path = package_dir / "README.md"
    readme_path.write_text(build_readme(skill, dependencies), encoding="utf-8")

    examples_dir = package_dir / "examples"
    examples_dir.mkdir(parents=True, exist_ok=True)
    examples_path = examples_dir / "usage.md"
    examples_path.write_text(build_examples_doc(skill), encoding="utf-8")

    tests_dir = package_dir / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)
    smoke_test_path = tests_dir / "smoke.md"
    smoke_test_path.write_text(build_smoke_test(skill, dependencies), encoding="utf-8")

    changelog_path = package_dir / "CHANGELOG.md"
    changelog_path.write_text(build_changelog(skill), encoding="utf-8")

    manifest_path = package_dir / "MANIFEST.yaml"
    files = [
        package_dir / "SKILL.md",
        readme_path,
        changelog_path,
        examples_path,
        smoke_test_path,
        *referenced_files,
    ]
    manifest_path.write_text(build_manifest(skill, package_dir, dependencies, files), encoding="utf-8")


def main() -> None:
    if PUBLISH_DIR.exists():
        shutil.rmtree(PUBLISH_DIR)
    PUBLISH_DIR.mkdir(parents=True, exist_ok=True)

    skills = [load_skill(path) for path in sorted(SKILLS_DIR.iterdir()) if path.is_dir()]
    for skill in skills:
        generate_bundle(skill)

    print(f"Generated {len(skills)} ClawHub bundles in {PUBLISH_DIR}")


if __name__ == "__main__":
    main()
