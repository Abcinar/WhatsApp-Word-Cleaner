"""
==========================================================
 WhatsApp Word Cleaner Pro
 Version : 1.0.0
 Author  : Abdullah Çınar
 License : MIT
==========================================================
"""

from __future__ import annotations

from collections.abc import Iterator

from docx.document import Document
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

from cleaner.patterns import (
    DATE_PATTERN,
    LINE_NUMBER_PATTERN,
    MULTIPLE_SPACE_PATTERN,
    ZERO_WIDTH_PATTERN,
)

from cleaner.statistics import Statistics


class DocumentCleaner:
    """
    Main document cleaning engine.
    """

    def __init__(self):

        self.stats = Statistics()

    # ---------------------------------------------------------
    # PUBLIC
    # ---------------------------------------------------------

    def clean(self, document: Document) -> Document:
        """
        Clean complete document.
        """

        previous_blank = False

        for paragraph in self._iter_paragraphs(document):

            self.stats.paragraphs_processed += 1

            previous_blank = self._clean_paragraph(
                paragraph,
                previous_blank,
            )

        return document

    # ---------------------------------------------------------
    # ITERATORS
    # ---------------------------------------------------------

    def _iter_paragraphs(
        self,
        document: Document,
    ) -> Iterator[Paragraph]:

        # Normal paragraphs
        for paragraph in document.paragraphs:
            yield paragraph

        # Tables
        for table in document.tables:
            yield from self._iter_table(table)

        # Headers / Footers
        for section in document.sections:

            for paragraph in section.header.paragraphs:
                yield paragraph

            for paragraph in section.footer.paragraphs:
                yield paragraph

    def _iter_table(
        self,
        table: Table,
    ) -> Iterator[Paragraph]:

        for row in table.rows:

            for cell in row.cells:

                yield from self._iter_cell(cell)

    def _iter_cell(
        self,
        cell: _Cell,
    ) -> Iterator[Paragraph]:

        for paragraph in cell.paragraphs:
            yield paragraph

        for table in cell.tables:
            yield from self._iter_table(table)

    # ---------------------------------------------------------
    # PARAGRAPH CLEANER
    # ---------------------------------------------------------

    def _clean_paragraph(
        self,
        paragraph: Paragraph,
        previous_blank: bool,
    ) -> bool:

        self._remove_dates(paragraph)

        self._remove_zero_width(paragraph)

        self._normalize_spaces(paragraph)

        text = paragraph.text.strip()

        if LINE_NUMBER_PATTERN.fullmatch(text):

            self._clear_paragraph(paragraph)

            self.stats.numbers_removed += 1

            return True

        if paragraph.text.strip() == "":

            if previous_blank:

                self._clear_paragraph(paragraph)

                self.stats.blank_lines_removed += 1

            return True

        return False
