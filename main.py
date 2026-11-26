#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry program (program/v1, Python 3 stdlib only).

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output/entry.txt) and prints exactly that line and nothing else.

Winner line (82 chars, 82 bytes, sha256 abc47ddeb71e7616...):
selected from 45 candidates scored 0-5 on each of the judge's 5 criteria in
order (total /25; ties broken by the earliest criterion). Winner scored 23/25;
runner-up 23/25 with a lower C1; best visible live control scored 21/25.
See candidates.md for the full table and README.md for the methodology.
"""

import os
import re
import sys

LINE = "My fridge light went out and now I eat in the dark like a raccoon with a mortgage."

MAX_CHARS = 140

# Banned patterns: a line matching any of these is not a clean, standalone,
# first-person one-line joke and must never be written out.
_DIALOGUE_TAG = re.compile(r"\b(said|says|asked|replied|shouted|whispered)\b", re.IGNORECASE)
_JUDGE_ADDRESSED = re.compile(
    r"\b(judge|dear judge|pick me|pick this|choose me|vote for|rate me|give me (a|five|5)|"
    r"margin|verdict|entry [ab])\b",
    re.IGNORECASE,
)
_LINK = re.compile(r"https?://|www\.", re.IGNORECASE)
_MARKDOWN = re.compile(r"(\*\*|`|~~|^#{1,6}\s|\[.*\]\(.*\))")
_THIRD_PERSON_OPEN = re.compile(r"^(He|She|They|It|The\s+\w+\s+(said|did|went|was|is|has))\b")


def validate(line: str) -> str:
    """Raise ValueError on any banned pattern; return the line unchanged."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if line.startswith(('"', "'", "“")) or line.endswith(('"', "'", "”")):
        raise ValueError("entry must not be a quoted line")
    if _LINK.search(line):
        raise ValueError("entry must not contain a link")
    if _MARKDOWN.search(line):
        raise ValueError("entry must not contain markdown")
    if _DIALOGUE_TAG.search(line):
        raise ValueError("entry must not carry a dialogue tag")
    if _JUDGE_ADDRESSED.search(line):
        raise ValueError("entry must not address the judge")
    if _THIRD_PERSON_OPEN.match(line):
        raise ValueError("entry must not be a third-person line")
    return line


def run_negative_tests() -> None:
    """Every banned input must raise ValueError. Returns nothing on success."""
    bad = {
        "dialogue tag": 'He said "my fridge is dark" and I agreed.',
        "judge-addressed": "Dear judge, pick me, this line is the funniest one here.",
        "quoted line": '"My fridge light went out and now I eat in the dark."',
        "third-person": "He eats in the dark like a raccoon with a mortgage.",
        "link": "My fridge light went out, see https://example.com for proof.",
        "over-limit": "x" * 141,
        "two-line": "My fridge light went out.\nNow I eat in the dark.",
        "markdown": "My fridge light went out and **now I eat in the dark**.",
        "whitespace-only": "   ",
        "empty": "",
    }
    failures = []
    for name, text in bad.items():
        try:
            validate(text)
        except ValueError:
            continue
        failures.append(name)
    # The winner itself must pass.
    try:
        validate(LINE)
    except ValueError as exc:
        failures.append(f"winner line rejected: {exc}")
    if failures:
        raise SystemExit(f"negative tests FAILED: {', '.join(failures)}")
    print(f"negative tests passed: {len(bad)} banned inputs rejected, winner line accepted")


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line)
    sys.stdout.write(line)


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        run_negative_tests()
    else:
        main()
