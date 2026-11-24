"""Office Joke Open entry: write one single-line office joke to /output/entry.txt.

Pure stdlib, no network, no reads outside this repository.
"""

import os

JOKE = (
    "I asked the office printer for one copy of my resignation — "
    "it jammed, printed 47, and now the whole office thinks "
    "I'm leaving in stages."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
