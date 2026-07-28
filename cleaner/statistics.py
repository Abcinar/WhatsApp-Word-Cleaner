from dataclasses import dataclass


@dataclass
class Statistics:
    dates_removed: int = 0
    numbers_removed: int = 0
    blank_lines_removed: int = 0
    spaces_fixed: int = 0
    paragraphs_processed: int = 0

    def report(self) -> str:
        return f"""
=====================================
 WhatsApp Word Cleaner Pro
=====================================

İşlenen Paragraf : {self.paragraphs_processed}

Silinen Tarih    : {self.dates_removed}

Silinen Numara   : {self.numbers_removed}

Boş Satır        : {self.blank_lines_removed}

Boşluk Düzeltme  : {self.spaces_fixed}

=====================================
"""
