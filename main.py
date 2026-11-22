import os
from pathlib import Path


def main():
    text = "Let your shoulders soften. The unfinished things can wait for one quiet breath; nothing needs solving right now."
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
