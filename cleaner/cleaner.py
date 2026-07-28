from __future__ import annotations

from typing import Iterator

from docx import Document
from docx.text.paragraph import Paragraph

from cleaner.patterns import (
    DATE_PATTERN,
    LINE_NUMBER_PATTERN,
    MULTIPLE_SPACE_PATTERN,
)
from cleaner.statistics import Statistics


class DocumentCleaner:

    def __init__(self):
        self.stats = Statistics()

    def clean(self, document: Document) -> Document:
        """
        Main cleaning pipeline.
        """

        previous_blank = False

        for paragraph in self._iter_all_paragraphs(document):

            self.stats.paragraphs_processed += 1

            result = self._clean_paragraph(
                paragraph,
                previous_blank,
            )

            previous_blank = result

        return document


    def _iter_all_paragraphs(
        self,
        document: Document,
    ) -> Iterator[Paragraph]:
        """
        Iterate through all paragraphs:
        - body
        - tables
        - headers
        - footers
        """

        for paragraph in document.paragraphs:
            yield paragraph


        for table in document.tables:

            for row in table.rows:

                for cell in row.cells:

                    for paragraph in cell.paragraphs:
                        yield paragraph


        for section in document.sections:

            for paragraph in section.header.paragraphs:
                yield paragraph

            for paragraph in section.footer.paragraphs:
                yield paragraph



    def _clean_paragraph(
        self,
        paragraph: Paragraph,
        previous_blank: bool,
    ) -> bool:
        """
        Cleans a single paragraph.
        Returns blank state.
        """

        self._clean_dates(paragraph)


        text = paragraph.text.strip()


        if LINE_NUMBER_PATTERN.fullmatch(text):

            self._clear_paragraph(paragraph)

            self.stats.numbers_removed += 1

            return True


        self._normalize_spaces(paragraph)


        if paragraph.text.strip() == "":

            if previous_blank:
                self.stats.blank_lines_removed += 1

            return True


                return False

def _clean_dates(self, paragraph: Paragraph) -> None:
        """
        Remove date/time patterns from every run.
        """
        """
        Remove date/time patterns from every run.
        """

        for run in paragraph.runs:

            if not run.text:
                continue

            matches = DATE_PATTERN.findall(run.text)

            if matches:
                self.stats.dates_removed += len(matches)
                run.text = DATE_PATTERN.sub("", run.text)


    def _normalize_spaces(self, paragraph: Paragraph) -> None:
        """
        Normalize multiple spaces while preserving runs.
        """

        changed = False

        for run in paragraph.runs:

            if not run.text:
                continue

            new_text = MULTIPLE_SPACE_PATTERN.sub(" ", run.text)

            if new_text != run.text:
                run.text = new_text
                changed = True

        if changed:
            self.stats.spaces_fixed += 1


    def _clear_paragraph(self, paragraph: Paragraph) -> None:
        """
        Clear paragraph text but keep paragraph structure.
        """

        for run in paragraph.runs:
            run.text = ""

        if not paragraph.runs:
            paragraph.add_run("")


    def reset_statistics(self) -> None:
        """
        Reset statistics before processing another document.
        """

        self.stats = Statistics()


    def get_statistics(self) -> Statistics:
        """
        Return statistics object.
        """

        return self.stats


    @property
    def statistics(self) -> Statistics:
        return self.stats
