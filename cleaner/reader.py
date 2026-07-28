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

from docx import Document


class DocumentReader:
    """
    Responsible for loading Microsoft Word documents.
    """

    def __init__(self, file_path: str | Path):

        self.file_path = Path(file_path)

    @property
    def exists(self) -> bool:
        """
        Check whether the document exists.
        """

        return self.file_path.exists()

    def validate(self) -> None:
        """
        Validate the input document.
        """

        if not self.exists:
            raise FileNotFoundError(
                f"Input document not found:\n{self.file_path}"
            )

        if self.file_path.suffix.lower() != ".docx":
            raise ValueError(
                "Only .docx files are supported."
            )

    def load(self) -> Document:
        """
        Load the Word document.
        """

        self.validate()

        return Document(self.file_path)

    @staticmethod
    def open(file_path: str | Path) -> Document:
        """
        Shortcut method.
        """

        reader = DocumentReader(file_path)

        return reader.load()
