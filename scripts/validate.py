#!/usr/bin/env python3
"""Static validation for this repository.

Runs four checks over the repository tree and exits non-zero if any fail:
  1. YAML files parse (PyYAML safe_load_all).
  2. JSON files parse.
  3. Relative Markdown links resolve to an existing path.
  4. No secret or employer-private patterns are present.

Usage:
  python scripts/validate.py
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git"}
SELF = "scripts/validate.py"


def iter_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            yield os.path.join(dirpath, name)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def main():
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
        return 2

    failures = []
    yaml_count = json_count = md_count = 0

    link_re = re.compile(r"\]\(([^)]+)\)")
    secret_patterns = {
        "aws access key id": re.compile(r"AKIA[0-9A-Z]{16}"),
        "aws secret assignment": re.compile(
            r"aws_secret_access_key\s*[:=]\s*['\"]?[A-Za-z0-9/+]{20,}"
        ),
        "private key block": re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
        "kubeconfig credential": re.compile(r"client-(?:certificate|key)-data\s*:"),
        "aws account id": re.compile(r"(?<!\d)\d{12}(?!\d)"),
        "private ipv4": re.compile(
            r"(?<!\d)(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            r"|192\.168\.\d{1,3}\.\d{1,3}"
            r"|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})(?!\d)"
        ),
        "employer reference": re.compile(
            r"\b(?:zinus|keetsa|mellow|zrpa|zinny|cargill)\b", re.IGNORECASE
        ),
    }
    text_ext = (".md", ".yaml", ".yml", ".json", ".tf", ".txt", ".sh", ".py")

    for path in iter_files():
        relpath = rel(path)

        if path.endswith((".yaml", ".yml")):
            yaml_count += 1
            try:
                with open(path, encoding="utf-8") as fh:
                    list(yaml.safe_load_all(fh))
            except Exception as exc:  # noqa: BLE001 - report any parse error
                failures.append(f"YAML parse: {relpath}: {exc}")

        if path.endswith(".json"):
            json_count += 1
            try:
                with open(path, encoding="utf-8") as fh:
                    json.load(fh)
            except Exception as exc:  # noqa: BLE001
                failures.append(f"JSON parse: {relpath}: {exc}")

        if path.endswith(".md"):
            md_count += 1
            base = os.path.dirname(path)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            for target in link_re.findall(text):
                token = target.strip().split()[0]
                if (
                    token.startswith("#")
                    or token.startswith("mailto:")
                    or re.match(r"^[a-z][a-z0-9+.-]*://", token)
                ):
                    continue
                token = token.split("#")[0]
                if not token:
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(base, token))):
                    failures.append(f"Markdown link: {relpath} -> {target}")

        if path.endswith(text_ext) and relpath not in (SELF, "LICENSE"):
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    text = fh.read()
            except OSError:
                continue
            for name, pattern in secret_patterns.items():
                match = pattern.search(text)
                if match:
                    line = text[: match.start()].count("\n") + 1
                    failures.append(
                        f"Secret scan [{name}]: {relpath}:{line}: {match.group(0)[:32]}"
                    )

    print(f"Checked {yaml_count} YAML, {json_count} JSON, {md_count} Markdown files.")
    if failures:
        print(f"\nFAILED ({len(failures)} issue(s)):")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
