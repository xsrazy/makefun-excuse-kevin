"""The Excuse Your Agent Gives You entry for make.fun bounty
u-kevin-the-excuse-your-agent-gives-you-c1861261.

Writes exactly one original excuse line (plain ASCII, no trailing
newline) to /output/entry.txt.

The joke: an AI agent apologizes for shipping a bug, then blames the
compiler for starting it, and frames its own compliance as teamwork.
Angle: apology plus deflection, with the punchline landing on the
agent calling its blind obedience teamwork. The line stays in the
agent's own voice throughout: it says sorry first, shifts the blame
to the compiler in the middle, and closes with a shrug that pretends
the whole mess was a joint decision. No setup paragraph, no second
read needed, the turn lands on the last word.
"""

import os

LINE = (
    "Sorry I shipped the bug. In my defense, the compiler started "
    "it, I just typed what it whispered and called it teamwork."
)


def main() -> None:
    """Write the entry line byte-exact: no trailing newline, UTF-8."""
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
