#!/usr/bin/env python3
"""Validate the public wrapper's reference to the released Core image."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


CONFIG_PATH = Path("ha-db-toolbox/config.yaml")
EXPECTED_IMAGE = "ghcr.io/montag-labs/ha-db-toolbox"
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:[.-][0-9A-Za-z.-]+)?$")


def read_scalar(config: str, name: str) -> str | None:
    """Read one quoted YAML top-level scalar without a general YAML parser."""
    match = re.search(rf'^{re.escape(name)}:\s*"([^"\n]+)"\s*$', config, re.MULTILINE)
    return match.group(1) if match else None


def validate_contract(root: Path) -> tuple[list[str], str | None]:
    """Return violations and the expected Core image version when valid."""
    errors: list[str] = []
    try:
        config = (root / CONFIG_PATH).read_text(encoding="utf-8")
    except OSError as error:
        return [f"Cannot read {CONFIG_PATH}: {error}"], None

    version = read_scalar(config, "version")
    image = read_scalar(config, "image")
    if version is None:
        errors.append("Add-on config requires a quoted top-level version")
    elif not VERSION_PATTERN.fullmatch(version):
        errors.append(f"Add-on version is invalid: {version}")
    if image != EXPECTED_IMAGE:
        errors.append(f"Add-on image must be {EXPECTED_IMAGE}")
    return errors, version


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--print-version", action="store_true")
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    errors, version = validate_contract(root)
    if errors:
        for error in errors:
            print(f"core-image-contract: {error}", file=sys.stderr)
        return 1
    if arguments.print_version:
        print(version)
    else:
        print("core-image-contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
