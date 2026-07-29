"""
==========================================================
 WhatsApp Word Cleaner Pro
 Version : 1.0.0
 Author  : Abdullah Çınar
 License : MIT
==========================================================
"""

from pathlib import Path
import sys

from cleaner.config import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_INPUT_FILE,
    DEFAULT_OUTPUT_FILE,
    INPUT_DIR,
    OUTPUT_DIR,
    LOG_DIR,
)

from cleaner.reader import DocumentReader
from cleaner.writer import DocumentWriter
from cleaner.cleaner import DocumentCleaner


def prepare_directories() -> None:
    """
    Create required directories.
    """

    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def print_banner() -> None:

    print("=" * 50)
    print(f"{APP_NAME} v{APP_VERSION}")
    print("=" * 50)


def main() -> int:

    print_banner()

    prepare_directories()

   # Input klasöründeki ilk .docx dosyasını bul
docx_files = sorted(INPUT_DIR.glob("*.docx"))

if not docx_files:

    print("\nNo .docx file found in input folder.")

    print("\nPlease copy your Word document to:")

    print(INPUT_DIR)

    return 1

if len(docx_files) > 1:

    print("\nERROR")
    print("More than one .docx file found.")
    print("Please leave only one document inside the input folder.")

    return 1

input_file = docx_files[0]

    try:

        print("\nLoading document...")

        document = DocumentReader.open(input_file)

        cleaner = DocumentCleaner()

        print("Cleaning...")

        cleaner.clean(document)

        print("Saving...")

        output = DocumentWriter.write(
            document,
            DEFAULT_OUTPUT_FILE,
        )

        print("\nDone.\n")

        print(cleaner.statistics)

        print(f"\nOutput file:\n{output}")

        return 0

    except Exception as exc:

        print("\nERROR")
        print("-" * 50)
        print(exc)
        print("-" * 50)

        return 2


if __name__ == "__main__":

    sys.exit(main())
