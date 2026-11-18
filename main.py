"""ai-judge-relax-01 entry: write one short relaxing text to entry.txt.

Entry v3: "A leaf on wool" (274 characters).
Standard library only. Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "Under the apple tree, a sheep lies with her legs folded beneath "
    "her. Her jaw moves from side to side. A few blades of grass lean "
    "against her wool. Above her, the leaves turn in a light wind, and "
    "patches of sun move over her back.\n"
    "\n"
    "A leaf settles on the wool and stays there."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
