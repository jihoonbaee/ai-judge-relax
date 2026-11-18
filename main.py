"""ai-judge-relax-01 entry: write one short relaxing text to entry.txt.

Entry v4: "Warm hearthstone" (922 characters).
A split log cooling in a stone hearth after everyone has gone in:
one small flame returning lower each time, ash slowly covering
the red seam, until only warmth remains in the stone.
Standard library only. Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "Within the stone hearth, the last split log lay red along "
    "its underside. Everyone had gone into the cabin. A small "
    "flame rose from one end, folded close to the wood, and "
    "rose again a little lower.\n"
    "\n"
    "It returned twice more, each time confined to the same "
    "notch. After that, the notch kept a bead of orange light. "
    "The long red seam beneath the log remained bright enough "
    "to show the grain.\n"
    "\n"
    "Ash gathered over the seam from either end. The exposed "
    "part shortened to the length of a thumb, with a brighter "
    "place near its middle. Occasionally that place deepened "
    "in colour, without growing wider.\n"
    "\n"
    "By ten, the ash had covered all but a narrow opening. "
    "Red showed through when a loose flake settled inward. "
    "The flake stayed, and the opening was smaller.\n"
    "\n"
    "Later, the log was grey from end to end. Its lower edge "
    "still warmed the hearthstone. In the notch where the "
    "flame had been, a little shelf of ash kept the shape of "
    "the wood."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
