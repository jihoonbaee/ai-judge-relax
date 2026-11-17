"""ai-judge-relax-01 entry: write one short relaxing text to entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "The street is empty at three in the morning. A cat crosses it in "
    "its own time, and the streetlights hum to nobody. Down the street "
    "a porch light is still on, waiting for someone who is already home. "
    "The bins are out for the morning.\n"
    "\n"
    "Nothing is open. Nothing needs to be."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
