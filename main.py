"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line (at most 200 characters) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

ROAST = "My earbuds conspired against me \u2014 one dies at 40%, the other at 4%; they couldn't agree on when."


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast must be 1-200 chars, got {len(text)}"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
