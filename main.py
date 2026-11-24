"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the entrant's honest count of open browser tabs as a single
number in digits and nothing else to /output/entry.txt.
"""

import os


def main():
    count = 1  # exactly one tab open: one thing at a time, everything else closed
    text = str(count)
    # Gate self-check: /output/entry.txt must be UTF-8 text of 1-5 chars,
    # digits only, not only white space.
    assert 1 <= len(text) <= 5 and text.isdigit(), "entry must be 1-5 digits"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
