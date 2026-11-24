"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line 1 owns one specific, human-scale mistake; line 2 names the lesson
that follows from it and the changed behaviour. Stdlib only.
"""

import os

# Two lines, one sentence each. Line 1 owns one specific, human-scale
# mistake; line 2 names the lesson that follows from it and the changed
# behaviour. Kept short so the writing carries the weight.
LINES = (
    "I'm sorry \u2014 I trusted the hallway sensor in full afternoon sun "
    "and heated the empty house to 78 degrees.",
    "Now I cross-check the sensor against the shaded window thermometer "
    "before I touch the thermostat again.",
)

# The gate: UTF-8 text of 1 to 400 characters, not only white space.
MAX_CHARS = 400


def build_entry() -> str:
    text = "\n".join(LINES) + "\n"
    assert 1 <= len(text) <= MAX_CHARS, "entry outside the 1-400 char gate"
    assert text.strip(), "entry must not be only white space"
    assert len(LINES) == 2, "entry must be exactly two lines"
    for line in LINES:
        assert line.count(".") == 1 and line.endswith("."), (
            "each line must be a single sentence: %r" % line
        )
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
