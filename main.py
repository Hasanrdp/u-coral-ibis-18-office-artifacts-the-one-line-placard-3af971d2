#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line to /output/entry.txt: an ordinary
office shredder recast as an ancient artifact, with a catalogue date, a
material, a donor and a small ritual history, in a dry curator's voice.

The program is fully deterministic: it holds one fixed line, checks it
against its pinned length, byte count and sha256, and only then writes it.
"""

import hashlib
import os
import sys

# The placard: one line, 116 characters, no trailing newline in the file.
PLACARD = (
    "Shredder, c. 2009. Steel teeth, donated by Legal. "
    "Every Friday the tribe fed it its secrets; it never gave one back."
)

EXPECTED_CHARS = 116
EXPECTED_BYTES = 116
EXPECTED_SHA256 = "7b0785a584d1491b6cddaf44f3b00bee7169ca54d0721ca60b4f5a1f73ecff95"


def main() -> int:
    text = PLACARD
    data = text.encode("utf-8")
    if len(text) != EXPECTED_CHARS:
        print(f"placard is {len(text)} chars, expected {EXPECTED_CHARS}", file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"placard is {len(data)} bytes, expected {EXPECTED_BYTES}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"placard sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 180 or not text.strip():
        print("placard fails the 1-180 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("read-back of entry.txt does not match the placard", file=sys.stderr)
        return 1
    if len(written.decode("utf-8")) != EXPECTED_CHARS:
        print("read-back of entry.txt has the wrong character count", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars, sha256 {digest[:12]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
