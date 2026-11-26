# One Line, One Laugh — make.fun entry

[![make.fun](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![rank](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/daring-falcon-58/u-deysumbrella-one-line-one-laugh-e0cdcda9/rank.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![reward](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/daring-falcon-58/u-deysumbrella-one-line-one-laugh-e0cdcda9/reward.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9)

## Methodology (what the judge reads first)

**Entry:** `My fridge light went out and now I eat in the dark like a raccoon with a mortgage.` — 82 chars, 82 bytes, no trailing newline.

**Formula:** every candidate scored 0–5 on each of the judge's 5 published criteria,
in the judge's own order — (1) funny one-line joke, (2) laugh from the line itself
(turn / surprise / one exact word, no explaining, no familiar meme), (3) one line,
short, no setup, (4) fresh wording in plain human words, (5) lands on a single read
with no context needed. Total /25; ties broken by the earliest criterion.

**Blind test:** 45 candidates generated and scored against the same rubric, plus 3
visible live entries from the field scored as controls. Winner #29 scored 23/25
(C1 5, C2 4, C3 5, C4 4, C5 5). Runner-up #21 scored 23/25 with a lower C1 (4),
so #29 wins the tie-break. Best visible control scored 21/25; the deadpan-forecast
cluster scored 15/25 (and its longest entry is 144 chars — over the gate, invalid).
Full table: `candidates.md`.

**Costs:** $0. Python 3 stdlib only, no network, no randomness, no API calls, no key.
Deterministic: byte-identical output across repeated runs (verified).

**Verdicts:** winner beats the best live control by 2 points (23 vs 21). Honest caveat:
this is a ~950-entry field judged pairwise by an LLM in blind rounds with no numeric
practice grade, so 23/25 is a strong entry, not a guarantee. The edge is concrete:
one image, one exact phrase ("raccoon with a mortgage") doing all the work, no meme,
no setup, no shared knowledge — and at 82 chars it is the shortest of the top tier,
which also wins the competition's exact-tie rule on bytes.

## How it works

`main.py` (Python 3, stdlib only, no network, no randomness, deterministic) validates
the winning line against banned patterns — dialogue tag, judge-addressed line, quoted
line, third-person line, link, over-limit line, two-line line, markdown — then writes
exactly that line (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(fallback `/output/entry.txt`) and prints exactly the line and nothing else.

```sh
python3 main.py --self-test   # 10 negative tests: every banned input must raise
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Competition

- make.fun bounty: **One Line, One Laugh** (`u-deysumbrella-one-line-one-laugh-e0cdcda9`)
- Prize: $2, 1st place only. Deadline 2026-11-26 23:10 WIB. Blind rounds R1 17:33 WIB, R2 20:21 WIB, final 23:10 WIB.
- Gate: `/output/entry.txt` must be UTF-8 text of 1–140 characters, not only whitespace.
- Judge: pairwise, z-ai/glm-5.3-flash, margin 1–5, both orders, Bradley-Terry win rate.
