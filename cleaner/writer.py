"""
==========================================================
 WhatsApp Word Cleaner Pro
 Version : 1.0.0
 Author  : Abdullah Çınar
 License : MIT
==========================================================
"""

from __future__ import annotations

from pathlib import Path

from docx.document import Document


class DocumentWriter:
    """
    Responsible for saving Word documents.
    """

    def __init__(self, output_path: str | Path):

        self.output_path = Path(output_path)

    def ensure_directory(self) -> None:
        """
        Create output directory if it does not exist.
        """

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(self, document: Document) -> Path:
        """
        Save document to disk.
        """

        self.ensure_directory()

        document.save(self.output_path)

        return self.output_path

    @staticmethod
    def write(
        document: Document,
        output_path: str | Path,
    ) -> Path:
        """
        Shortcut save method.
        """

        writer = DocumentWriter(output_path)

        return writer.save(document)
