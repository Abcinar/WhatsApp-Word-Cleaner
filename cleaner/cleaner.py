import re

from cleaner.patterns import (
    DATE_PATTERN,
    LINE_NUMBER_PATTERN,
    MULTIPLE_SPACE_PATTERN,
)


class Cleaner:

    def __init__(self):
        self.stats = {
            "dates_removed": 0,
            "numbers_removed": 0,
            "spaces_fixed": 0,
        }

    def clean_text(self, text: str) -> str:

        # WhatsApp tarihlerini sil
        dates = DATE_PATTERN.findall(text)

        if dates:
            self.stats["dates_removed"] += len(dates)
            text = DATE_PATTERN.sub("", text)

        # Tek başına duran sıra numaralarını sil
        if LINE_NUMBER_PATTERN.fullmatch(text.strip()):
            self.stats["numbers_removed"] += 1
            return ""

        # Fazla boşlukları düzelt
        fixed = MULTIPLE_SPACE_PATTERN.sub(" ", text)

        if fixed != text:
            self.stats["spaces_fixed"] += 1

        return fixed.strip()

    def get_stats(self):

        return self.stats
