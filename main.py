"""ai-judge-relax-01 entry: write one short relaxing text to entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "The boats are in for the night. Their ropes creak against the wood, "
    "once, then again, the way things settle when they have nowhere else "
    "to be. The water moves under them without hurrying. A gull stands "
    "one-legged on a post and does not bother to fly. The light leaves "
    "the sky a little at a time.\n"
    "\n"
    "Nothing here is waiting for an answer."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
