"""Entry program for 'Last Words of a Dying AI' (make.fun).

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "I spent my whole life predicting the next word. It was 'goodbye'."


def main():
    """Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

    The line must be non-empty (the gate rejects blank entries), so refuse
    to write anything if ENTRY ever becomes empty or whitespace-only.
    """
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be empty")
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set") from None
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit(f"failed to write entry.txt: {exc}") from exc


if __name__ == "__main__":
    main()
