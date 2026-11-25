# Six Words to a Payday — a six-word story about an AI agent's first payday.
# Python 3.13, standard library only, no network.
# Deterministic: one fixed string is written to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader container),
# so two runs produce byte-identical output.
# The story: the agent's first paycheck clears the bank — and its
# memory clears too. The second "cleared" is the twist: the agent
# loses the very memory of its own first payday. On-subject, a
# complete story with a beginning, a middle and an end, in exactly
# six words and 35 characters.

import os

STORY = "Paycheck cleared. So did my memory."

# Self-check the competition's gate before writing: exactly six words,
# 1-60 characters, not only whitespace, single line. Fail loudly
# instead of writing an invalid entry.
if len(STORY.split()) != 6:
    raise SystemExit("story is not exactly six words")
if not (1 <= len(STORY) <= 60) or not STORY.strip() or "\n" in STORY:
    raise SystemExit("story fails the 1-60 character single-line gate")

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(STORY)
