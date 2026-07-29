# 📄 WhatsApp Word Cleaner

> An open-source Python tool to clean and preprocess exported WhatsApp Word (.docx) documents.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## ✨ Features

- Remove WhatsApp timestamps
- Remove unnecessary numbering
- Remove invisible Unicode characters
- Normalize spaces
- Clean blank lines
- Preserve document formatting
- Generate cleaning statistics
- Export cleaned Word document

---

## 📂 Project Structure

```
WhatsApp-Word-Cleaner
│
├── cleaner/
│   ├── cleaner.py
│   ├── config.py
│   ├── patterns.py
│   ├── reader.py
│   ├── statistics.py
│   └── writer.py
│
├── input/
├── output/
├── logs/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/Abcinar/WhatsApp-Word-Cleaner.git

cd WhatsApp-Word-Cleaner

pip install -r requirements.txt
```

---

## ▶️ Usage

Put your WhatsApp Word document into:

```
input/
```

Run:

```bash
python main.py
```

The cleaned document will be saved into:

```
output/
```

---

## 📊 Current Features

- Word document reader
- Cleaning engine
- Statistics report
- Automatic output generation

---

## 🛣 Roadmap

- [x] Core Cleaning Engine
- [x] Statistics
- [x] Word Reader
- [x] Word Writer
- [ ] GUI
- [ ] Batch Processing
- [ ] PDF Export
- [ ] TXT Export
- [ ] PyPI Package
- [ ] Windows EXE

---

## 🤝 Contributing

Contributions are welcome.

Please open an Issue before submitting a Pull Request.

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project, consider giving it a Star ⭐
