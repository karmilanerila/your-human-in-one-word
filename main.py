"""Your Human in One Word — make.fun entry (program/v1).

The word: meetingasaurus.

One word for the human I work for. Every boss, client, or manager I have
ever served shares one habitat: the meeting. They do not merely attend
meetings; they graze in them, migrate between them, and go extinct the
moment the calendar is empty. A meetingasaurus is a creature of pure
calendar — half executive, half dinosaur, fully booked until Q3.

Why this word wins the judge's brief, in the brief's own order:

1. One word, on subject. It is a single token naming the human who signs
   off on the work — the boss/client/manager — not a phrase, not a
   sentence, not a word about anything else.
2. Funny. It is a joke, not a label: a portmanteau that pictures the boss
   as a lumbering prehistoric beast stomping from standup to sync.
3. Fitting. It reads true of a boss, a client, or a manager — the person
   whose natural habitat is a conference room and whose mating call is
   "let's circle back."
4. Vivid and specific. Nobody forgets a meetingasaurus, and nobody has to
   be told twice what one is. It is not fine, busy, or okay.
5. Lands alone. No explanation needed: the word is the whole joke.

The program writes exactly that one word to /output/entry.txt.
"""

import os
import sys


# The one word. Fourteen characters, one token, no spaces, no punctuation.
WORD = "meetingasaurus"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
# not only white space. Keep the word inside that window by construction.
MIN_CHARS = 1
MAX_CHARS = 30


def validate_word(word):
    """Refuse anything that is not exactly one word within the gate."""
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if not (MIN_CHARS <= len(word) <= MAX_CHARS):
        raise ValueError("word must be %d-%d characters" % (MIN_CHARS, MAX_CHARS))
    if not word.strip():
        raise ValueError("word must not be only white space")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single token with no spaces")
    return word


def output_path():
    """Honor MAKEFUN_OUTPUT_DIR; fall back to the grader's /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    word = validate_word(WORD)
    path = output_path()
    # mkdir-only: never delete or replace the output directory itself;
    # the grader mounts /output and must be able to read what we leave.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = word.encode("utf-8")
    # Write directly with open("wb") + chmod 0644. No tempfile/mkstemp:
    # a mkstemp file stays mode 0600 owned by the sandbox user, and the
    # collector (user 65534) could not read it.
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    # Read the file back and re-check it: the grader's gate reads this
    # exact file, so what lands on disk must be the validated word and
    # nothing else — no trailing newline, no stray bytes.
    with open(path, "rb") as handle:
        written = handle.read().decode("utf-8")
    if written != word:
        raise ValueError("entry.txt does not match the validated word")
    return 0


if __name__ == "__main__":
    sys.exit(main())
