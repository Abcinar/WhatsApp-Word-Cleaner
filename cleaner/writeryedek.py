from pathlib import Path
from docx.document import Document


class WordWriter:
    """
    Temizlenmiş Word belgesini kaydeder.
    """

    def __init__(self, output_path: str):
        self.output_path = Path(output_path)

    def save(self, document: Document) -> None:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        document.save(str(self.output_path))
