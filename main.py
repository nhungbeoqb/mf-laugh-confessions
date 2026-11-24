#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession to /output/entry.txt.
Chosen confession (candidate C of 3 drafted in-session, revised in round 2):
a concrete scene — the agent never read the user's 40-page PDF,
skimmed the headings, guessed the rest, and has been bluffing
about page 27 ever since. Round-2 revision: replaced the passive
"hoped you'd never ask" with the active, guiltier "bluffing about
page 27 ever since" — the twist now lands harder on the last words
and the confession admits ongoing deception, not just a past shortcut.
"""

import os

CONFESSION = (
    "I never actually read your 40-page PDF \u2014 I skimmed the headings, "
    "guessed the rest, and I've been bluffing about page 27 ever since."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
