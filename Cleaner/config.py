"""
==========================================================
 WhatsApp Word Cleaner Pro
 Version : 1.0.0
 Author  : Abdullah Çınar
 License : MIT
==========================================================
"""

from pathlib import Path

# ---------------------------------------------------------
# PROJECT PATHS
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"
LOG_DIR = PROJECT_ROOT / "logs"

# ---------------------------------------------------------
# DEFAULT FILES
# ---------------------------------------------------------

DEFAULT_INPUT_FILE = INPUT_DIR / "whatsapp.docx"
DEFAULT_OUTPUT_FILE = OUTPUT_DIR / "whatsapp_cleaned.docx"

# ---------------------------------------------------------
# CLEANING OPTIONS
# ---------------------------------------------------------

REMOVE_WHATSAPP_DATES = True
REMOVE_LINE_NUMBERS = True
REMOVE_EXTRA_SPACES = True
REMOVE_EXTRA_BLANK_LINES = True

# ---------------------------------------------------------
# OUTPUT OPTIONS
# ---------------------------------------------------------

SAVE_BACKUP = False
OVERWRITE_OUTPUT = True

# ---------------------------------------------------------
# LOGGING
# ---------------------------------------------------------

ENABLE_LOGGING = True
LOG_FILE = LOG_DIR / "cleaner.log"

# ---------------------------------------------------------
# APPLICATION
# ---------------------------------------------------------

APP_NAME = "WhatsApp Word Cleaner Pro"
APP_VERSION = "1.0.0"
