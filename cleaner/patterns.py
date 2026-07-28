import re

# WhatsApp tarihleri
DATE_PATTERN = re.compile(
    r"\[\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}\]"
)

# Sadece rakamlardan oluşan satırlar (3070, 8451 ...)
LINE_NUMBER_PATTERN = re.compile(
    r"^\s*\d+\s*$"
)

# İki veya daha fazla boşluk
MULTIPLE_SPACE_PATTERN = re.compile(
    r"[ ]{2,}"
)

# Art arda boş satırlar
EMPTY_LINE_PATTERN = re.compile(
    r"\n{3,}"
)
