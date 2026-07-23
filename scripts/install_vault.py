#!/usr/bin/env python3
"""Safely install or upgrade the bundled Obsidian interview-growth vault."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from datetime import datetime
from pathlib import Path


MANAGED_PREFIXES = (Path("99 模板"), Path("99 系统"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Target Obsidian vault folder")
    parser.add_argument("--mode", choices=("create", "upgrade"), default="create")
    parser.add_argument("--dry-run", action="store_true", help="Show planned actions only")
    return parser.parse_args()


def is_managed(relative: Path) -> bool:
    return any(relative == prefix or prefix in relative.parents for prefix in MANAGED_PREFIXES)


def validate_target(target: Path) -> None:
    resolved = target.resolve()
    home = Path.home().resolve()
    if resolved == Path(resolved.anchor) or resolved == home:
        raise ValueError("Refusing to install into a filesystem root or home directory.")


def files_under(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path, path.relative_to(root)


def main() -> int:
    args = parse_args()
    skill_root = Path(__file__).resolve().parent.parent
    template = skill_root / "assets" / "vault-template"
    target = Path(args.target).expanduser().resolve()

    if not template.is_dir():
        print(f"ERROR: bundled template not found: {template}", file=sys.stderr)
        return 2

    try:
        validate_target(target)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.mode == "create" and target.exists() and any(target.iterdir()):
        print("ERROR: create mode requires a new or empty target folder.", file=sys.stderr)
        return 2

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = target / "_系统备份" / timestamp
    actions = {"created": 0, "updated": 0, "skipped": 0, "backed_up": 0}

    for source, relative in files_under(template):
        destination = target / relative

        if not destination.exists():
            print(f"CREATE  {relative}")
            actions["created"] += 1
            if not args.dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
            continue

        if filecmp.cmp(source, destination, shallow=False):
            actions["skipped"] += 1
            continue

        if args.mode == "upgrade" and is_managed(relative):
            backup = backup_root / relative
            print(f"BACKUP  {relative} -> {backup.relative_to(target)}")
            print(f"UPDATE  {relative}")
            actions["backed_up"] += 1
            actions["updated"] += 1
            if not args.dry_run:
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(destination, backup)
                shutil.copy2(source, destination)
        else:
            print(f"SKIP    {relative} (existing personal or unmanaged file)")
            actions["skipped"] += 1

    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)

    print(
        "SUMMARY "
        + " ".join(f"{key}={value}" for key, value in actions.items())
        + (" dry_run=true" if args.dry_run else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

