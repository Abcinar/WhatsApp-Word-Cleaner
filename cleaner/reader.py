from pathlib import Path
from docx import Document


class WordReader:
    """
    Word (.docx) dosyasını okur.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def exists(self) -> bool:
        return self.file_path.exists()

    def load(self) -> Document:
        if not self.exists():
            raise FileNotFoundError(
                f"Dosya bulunamadı: {self.file_path}"
            )

        return Document(str(self.file_path))
