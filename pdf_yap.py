import subprocess
import os
from docx import Document
# ESKİ HALİ (Hatalı olan):
from cleaner import DocumentCleaner

# YENİ HALİ (Bununla değiştir):
from cleaner.cleaner import DocumentCleaner
def convert_to_pdf_linux(docx_path, output_dir):
    """LibreOffice kullanarak docx'i pdf'e çevirir (Linux/Codespaces için)"""
    print(f"PDF'e dönüştürülüyor: {docx_path}")
    
    # LibreOffice komutunu çalıştır
    subprocess.run([
        "libreoffice", 
        "--headless", 
        "--convert-to", 
        "pdf", 
        docx_path, 
        "--outdir", 
        output_dir
    ])
    print("Dönüştürme tamamlandı!")

# 1. Dosyayı aç ve temizle (Dosya yollarını kendine göre düzelt)
input_docx = "input/whatsapp.docx"
output_docx = "output/whatsapp_cleaned.docx"
output_dir = "output"

print("Word dosyası temizleniyor...")
doc = Document(input_docx)
cleaner = DocumentCleaner()
cleaned_doc = cleaner.clean(doc)

# 2. Temizlenmiş Word dosyasını kaydet
cleaned_doc.save(output_docx)
print("Temizlenmiş dosya kaydedildi:", output_docx)

# 3. PDF'e Çevir
convert_to_pdf_linux(output_docx, output_dir)
