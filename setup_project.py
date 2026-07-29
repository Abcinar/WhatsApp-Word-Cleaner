"""
WhatsApp Word Cleaner
Project Setup Script

Creates the required project folders if they do not already exist.
"""

from pathlib import Path


PROJECT_FOLDERS = [
    "docs",
    "tests",
    "examples",
    "input",
    "output",
    "logs",
    ".github",
    ".github/workflows",
]


def create_folder(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

    gitkeep = path / ".gitkeep"

    if not gitkeep.exists():
        gitkeep.touch()

    print(f"✓ {path}")


def main() -> None:
    print("=" * 50)
    print(" WhatsApp Word Cleaner - Project Setup")
    print("=" * 50)
    print()

    for folder in PROJECT_FOLDERS:
        create_folder(Path(folder))

    print()
    print("=" * 50)
    print("Project structure is ready.")
    print("=" * 50)


if __name__ == "__main__":
    main()
