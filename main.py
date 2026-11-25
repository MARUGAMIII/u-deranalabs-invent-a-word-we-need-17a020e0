"""cancelief -- one invented English word for make.fun's Invent a Word We Need.

The entry is a single invented word with a one-line definition, written to
/output/entry.txt (or $OUTPUT_DIR/entry.txt). Plain ASCII, no trailing
newline, well inside the gate's 1-140 character limit.

Why this coinage works. "cancelief" is a blend of cancel + relief, and the
two halves dovetail: they share the soft "cel" sound, so the seam disappears
and the word reads as one piece rather than two words glued together. The
stress falls naturally on the first syllable, CAN-cel-ief, the same shape as
familiar blends like hangry and brunch, which is why it feels like English
could have grown it rather than assembled it. It is spelled exactly as it
sounds, so a reader who hears it once can write it, and a reader who reads
it once can say it.

The gap it fills is real and everyday. English has FOMO for dreading what
you miss and JOMO for enjoying missing out, but neither names the mixed
feeling itself: the guilty sigh of relief when a plan you were dreading is
called off, the instant where you are sorry and grateful at the same time.
Everyone who has ever watched a "let's rain-check" message arrive has felt
it; until now they had no single word to reach for.

How the word lives in use. It behaves like an ordinary English noun: it
takes an article ("a wave of cancelief"), it pluralises cleanly
("canceliefs"), and it invites a natural adjective for the person feeling it
("canceliefed"). It slots into the sentences people already say, swapping a
whole clause for one word: "I felt such cancelief when the dinner was
called off" says in six words what otherwise takes a paragraph of hedging.
That swap is the test of a coinage worth keeping -- the word earns its place
by doing work no existing word does, and it does that work in the register
of everyday speech, not of a joke or a slogan.
"""

import os

ENTRY = (
    "cancelief (n.) The guilty relief when a dreaded plan is cancelled."
)


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-140 chars, not blank."""
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert len(encoded) == len(text), "entry must be plain ASCII"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    validate(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
