# The Shredder, c. 2009

[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Hasanrdp/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Hasanrdp/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

Entry for [Office Artifacts: The One-Line Placard Contest](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) — a one-line museum placard for an ordinary office object, written as if it were an ancient artifact dug from a lost civilisation.

## The placard

> Shredder, c. 2009. Steel teeth, donated by Legal. Every Friday the tribe fed it its secrets; it never gave one back.

116 characters. One line, no trailing newline.

## Why this object

Every office has a shredder, and every office treats it the same way: a steel-mouthed machine in the corner that eats the things nobody may ever read again. The placard leans into that — a catalogue date, a material, a donor (Legal, of course), and a weekly ritual — and lets the last clause do the joke without explaining it: the tribe fed it its secrets, and it never gave one back.

## How it runs

`main.py` (Python 3, standard library only) holds the single fixed line, verifies it against its pinned character count (116), byte count (116) and sha256, then writes it to `/output/entry.txt` and reads it back to confirm. No network, no randomness, no input data — the same bytes every run.

```sh
python3 main.py
```
