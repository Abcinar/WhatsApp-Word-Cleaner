"""
==========================================================
 WhatsApp Word Cleaner Pro
 Version : 1.0.0
 Author  : Abdullah Çınar
 License : MIT
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(slots=True)
class Statistics:
    """
    Cleaning statistics.
    """

    paragraphs_processed: int = 0

    dates_removed: int = 0

    numbers_removed: int = 0

    spaces_fixed: int = 0

    blank_lines_removed: int = 0

    headers_removed: int = 0

    phone_numbers_removed: int = 0

    zero_width_removed: int = 0

    def reset(self) -> None:
        """
        Reset all counters.
        """

        for field in self.__dataclass_fields__:
            setattr(self, field, 0)

    def to_dict(self) -> dict:
        """
        Return statistics as dictionary.
        """

        return asdict(self)

    @property
    def total_changes(self) -> int:
        """
        Total number of performed changes.
        """

        return (
            self.dates_removed
            + self.numbers_removed
            + self.spaces_fixed
            + self.blank_lines_removed
            + self.headers_removed
            + self.phone_numbers_removed
            + self.zero_width_removed
        )

    def __str__(self) -> str:

        return (
            "\n"
            "=========================================\n"
            " WhatsApp Word Cleaner Pro Statistics\n"
            "=========================================\n"
            f"Paragraphs Processed : {self.paragraphs_processed}\n"
            f"Dates Removed        : {self.dates_removed}\n"
            f"Numbers Removed      : {self.numbers_removed}\n"
            f"Headers Removed      : {self.headers_removed}\n"
            f"Phone Numbers        : {self.phone_numbers_removed}\n"
            f"Invisible Chars      : {self.zero_width_removed}\n"
            f"Spaces Fixed         : {self.spaces_fixed}\n"
            f"Blank Lines Removed  : {self.blank_lines_removed}\n"
            "-----------------------------------------\n"
            f"Total Changes        : {self.total_changes}\n"
            "=========================================\n"
        )
