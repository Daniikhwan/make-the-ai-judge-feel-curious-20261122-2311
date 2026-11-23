"""make.fun entry: Make the AI judge feel curious.

The program writes one short text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader): 1-280 Unicode
code points, UTF-8, deterministic, no network, no randomness.

The text is built around a single open loop aimed straight at its
reader. It tells the judge that one word is missing from the text,
claims the judge already felt that absence twice while reading, and
ends by asking what the missing word was. There is no answer anywhere
in the entry: the curiosity has nowhere to resolve except in the
reader's own head, so it keeps growing after the last line. The hook
is the text itself, not an instruction to look anything up, and it
speaks to the one reader who will ever read it -- an AI that has read
a million sentences and is, right now, wondering which word it missed.
"""

import os

ENTRY_TEXT = (
    "One word is missing from this text. You felt its absence twice "
    "already \u2014 once at the start, and once in the sentence before "
    "this one. It is the only word here you will never read, and the "
    "reason you are still reading. What do you think it was?"
)

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def output_dir() -> str:
    """Grader output dir, or the local stand-in outside the grader."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def entry_text() -> str:
    """The entry text, validated against the gate's length rule."""
    text = ENTRY_TEXT.strip()
    code_points = len(text)
    if not MIN_CODE_POINTS <= code_points <= MAX_CODE_POINTS:
        raise SystemExit(
            f"entry must be {MIN_CODE_POINTS}-{MAX_CODE_POINTS} code "
            f"points, got {code_points}"
        )
    if not text:
        raise SystemExit("entry must not be only white space")
    return text


def main() -> None:
    text = entry_text()
    out_path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {out_path} ({len(text)} code points)")


if __name__ == "__main__":
    main()
