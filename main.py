"""Make the AI judge feel curious — one short text, one small blue door.

Entry text: 273 characters (277 bytes). Design: direct address to the judge (it has read
hundreds of small texts tonight) plus one concrete, gentle mystery — a small
blue door that was never there before, warm light spilling from under it.
Intrigue without tension, calm shown not instructed, one lingering image.
Revisions: "of them" added to the second sentence for a slower, steadier
rhythm; "never there before" and "spilling" sharpen the mystery.
"""

import os

TEXT = (
    "You have read hundreds of these tonight. Nearly every one of them wanted "
    "something from you. This one only asks you to notice the small blue "
    "door at the end of the street \u2014 the one never there "
    "before \u2014 and the warm light spilling from under it, waiting, "
    "patiently, for you."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry must be 1-280 chars, got {len(TEXT)}"
    assert TEXT.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
