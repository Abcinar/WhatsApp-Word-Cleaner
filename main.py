from cleaner.reader import WordReader
from cleaner.writer import WordWriter

INPUT_FILE = "input/Kuran.docx"
OUTPUT_FILE = "output/Kuran_Temizlenmis.docx"


def main():
    reader = WordReader(INPUT_FILE)
    document = reader.load()

    writer = WordWriter(OUTPUT_FILE)
    writer.save(document)

    print("✓ Belge başarıyla okundu ve kaydedildi.")
    print(f"Çıktı: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
