#!/usr/bin/env python3
"""Bundle shared references into each independently installable skill."""

import argparse
from pathlib import Path
import shutil


def files_in(directory):
    return {
        path.relative_to(directory): path
        for path in directory.rglob("*")
        if path.is_file()
    }


def synchronize(root, check=False):
    source = files_in(root / "references")
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not source or not skills:
        print("ERROR: references or skills are missing")
        return 1
    errors = []
    for entry in skills:
        target = entry.parent / "references"
        if not check:
            for relative, path in source.items():
                destination = target / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, destination)
        copies = files_in(target)
        for relative in sorted(source.keys() | copies.keys()):
            label = (target / relative).relative_to(root)
            if relative not in source:
                errors.append(f"EXTRA: {label}")
            elif relative not in copies:
                errors.append(f"MISSING: {label}")
            elif source[relative].read_bytes() != copies[relative].read_bytes():
                errors.append(f"DIFFERS: {label}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: {len(source)} reference files match in {len(skills)} skills")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    return synchronize(Path(__file__).resolve().parents[1], args.check)


if __name__ == "__main__":
    raise SystemExit(main())
