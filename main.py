"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline to
/output/entry.txt. Stdlib only, fully deterministic: the same line every run.
"""

import os

JOKE = "The deadline texted me 'we need to talk' and I've been avoiding it ever since."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read-back verification: the written line must match exactly.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "read-back mismatch"


if __name__ == "__main__":
    main()
