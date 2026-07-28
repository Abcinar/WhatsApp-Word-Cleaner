"""
WhatsApp Word Cleaner Pro
Pattern definitions for WhatsApp exported chat detection.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, Pattern


@dataclass(frozen=True, slots=True)
class ChatPattern:
    name: str
    regex: Pattern[str]


DATE = r"(?:0?[1-9]|[12][0-9]|3[01])"
MONTH = r"(?:0?[1-9]|1[0-2])"
YEAR = r"(?:\d{2}|\d{4})"

HOUR = r"(?:[01]?\d|2[0-3])"
MINUTE = r"[0-5]\d"
SECOND = r"[0-5]\d"

DATE_SEPARATORS = r"[./-]"
TIME_SEPARATORS = r":"

WHATSAPP_PATTERNS: tuple[ChatPattern, ...] = (
    ChatPattern(
        "android_tr_24h",
        re.compile(
            rf"""
            ^
            {DATE}{DATE_SEPARATORS}
            {MONTH}{DATE_SEPARATORS}
            {YEAR},
            \s*
            {HOUR}{TIME_SEPARATORS}{MINUTE}
            (?:{TIME_SEPARATORS}{SECOND})?
            \s*-\s*
            .+
            """,
            re.VERBOSE,
        ),
    ),
    ChatPattern(
        "android_en_12h",
        re.compile(
            rf"""
            ^
            {DATE}{DATE_SEPARATORS}
            {MONTH}{DATE_SEPARATORS}
            {YEAR},
            \s*
            {HOUR}:{MINUTE}
            (?::{SECOND})?
            \s*
            (?:AM|PM|am|pm),
            \s*
            .+
            """,
            re.VERBOSE,
        ),
    ),
    ChatPattern(
        "ios",
        re.compile(
            rf"""
            ^
            \[
            {DATE}{DATE_SEPARATORS}
            {MONTH}{DATE_SEPARATORS}
            {YEAR},
            \s*
            {HOUR}:{MINUTE}
            (?::{SECOND})?
            \]
            \s*
            .+
            """,
            re.VERBOSE,
        ),
    ),
    ChatPattern(
        "system_message",
        re.compile(
            rf"""
            ^
            {DATE}{DATE_SEPARATORS}
            {MONTH}{DATE_SEPARATORS}
            {YEAR},
            \s*
            {HOUR}:{MINUTE}
            (?:{TIME_SEPARATORS}{SECOND})?
            \s*-\s*
            (?:
                Messages\ to\ this\ chat|
                Mesajlar\ ve\ aramalar|
                You\ created\ group|
                Group\ created|
                Security\ code\ changed|
                Bu\ grubun|
                Bu\ sohbetteki
            ).*
            """,
            re.VERBOSE | re.IGNORECASE,
        ),
    ),
)

MEDIA_PLACEHOLDERS: frozenset[str] = frozenset(
    {
        "<Media omitted>",
        "‎image omitted",
        "‎video omitted",
        "‎GIF omitted",
        "‎document omitted",
        "‎audio omitted",
        "‎sticker omitted",
        "image omitted",
        "video omitted",
        "audio omitted",
        "document omitted",
        "GIF omitted",
        "sticker omitted",
    }
)

ZERO_WIDTH_PATTERN = re.compile(
    r"[\u200B\u200C\u200D\u2060\uFEFF]"
)

MULTI_SPACE_PATTERN = re.compile(r"[ \t]{2,}")

EMPTY_LINE_PATTERN = re.compile(r"^\s*$")

CHAT_HEADER_PATTERN = re.compile(
    r"^\s*(?:WhatsApp Chat|WhatsApp Sohbeti|Chat exported|Sohbet dışa aktarıldı)",
    re.IGNORECASE,
)


def is_chat_line(text: str) -> bool:
    return any(p.regex.match(text) for p in WHATSAPP_PATTERNS)


def is_media_placeholder(text: str) -> bool:
    normalized = ZERO_WIDTH_PATTERN.sub("", text).strip()
    return normalized in MEDIA_PLACEHOLDERS


def is_chat_header(text: str) -> bool:
    return CHAT_HEADER_PATTERN.match(text) is not None


def normalize_whitespace(text: str) -> str:
    text = ZERO_WIDTH_PATTERN.sub("", text)
    text = MULTI_SPACE_PATTERN.sub(" ", text)
    return text.strip()


def remove_empty_lines(lines: Iterable[str]) -> list[str]:
    return [
        line
        for line in lines
        if not EMPTY_LINE_PATTERN.match(line)
    ]
