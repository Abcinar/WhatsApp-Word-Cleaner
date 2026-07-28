from docx import Document

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

        previous_blank = False

        for paragraph in document.paragraphs:

            self.stats.paragraphs_processed += 1

            text = paragraph.text

            # Tarihleri sil (run biçimlendirmesini korumak için run bazında)
            for run in paragraph.runs:
                matches = DATE_PATTERN.findall(run.text)

                if matches:
                    self.stats.dates_removed += len(matches)
                    run.text = DATE_PATTERN.sub("", run.text)

            # Paragraf metnini yeniden değerlendir
            text = paragraph.text.strip()

            # Tek başına duran numaraları sil
            if LINE_NUMBER_PATTERN.fullmatch(text):
                paragraph.clear()
                self.stats.numbers_removed += 1
                previous_blank = True
                continue

            # Fazla boşlukları düzelt
            new_text = MULTIPLE_SPACE_PATTERN.sub(" ", paragraph.text)

            if new_text != paragraph.text:
                self.stats.spaces_fixed += 1

                # Run'lar yerine paragrafı yeniden yazıyoruz.
                # (İçinde tarih olmayan normal metinlerde sorun oluşturmaz.)
                paragraph.clear()
                paragraph.add_run(new_text.strip())

            # Boş satır sayımı
            if paragraph.text.strip() == "":
                if previous_blank:
                    self.stats.blank_lines_removed += 1
                previous_blank = True
            else:
                previous_blank = False

        return document
