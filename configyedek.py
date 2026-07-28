"""
WhatsApp Word Cleaner Pro
Production Configuration Module
"""

from __future__ import annotations

import logging
import multiprocessing
import os
import platform
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Final


APP_NAME: Final[str] = "WhatsApp Word Cleaner Pro"
APP_VERSION: Final[str] = "1.0.0"
APP_AUTHOR: Final[str] = "Abdullah Çınar"


def _bool_env(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
        "enabled",
    }


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default

    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _path_env(name: str, default: Path) -> Path:
    value = os.getenv(name)
    if value:
        return Path(value).expanduser().resolve()
    return default


def _default_data_dir() -> Path:
    system = platform.system().lower()

    if system == "windows":
        root = Path(os.getenv("LOCALAPPDATA", Path.home()))
        return root / "WhatsAppWordCleanerPro"

    if system == "darwin":
        return (
            Path.home()
            / "Library"
            / "Application Support"
            / "WhatsAppWordCleanerPro"
        )

    root = Path(os.getenv("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return root / "WhatsAppWordCleanerPro"


@dataclass(slots=True, frozen=True)
class PathsConfig:
    app_dir: Path = field(
        default_factory=lambda: _path_env(
            "WWCP_APP_DIR",
            _default_data_dir(),
        )
    )

    @property
    def logs_dir(self) -> Path:
        return self.app_dir / "logs"

    @property
    def temp_dir(self) -> Path:
        return self.app_dir / "temp"

    @property
    def backup_dir(self) -> Path:
        return self.app_dir / "backup"

    @property
    def cache_dir(self) -> Path:
        return self.app_dir / "cache"

    @property
    def output_dir(self) -> Path:
        return self.app_dir / "output"


@dataclass(slots=True, frozen=True)
class ProcessingConfig:
    max_workers: int = max(1, multiprocessing.cpu_count() - 1)
    chunk_size: int = 500
    autosave_every: int = 100
    max_file_size_mb: int = 250
    memory_buffer_mb: int = 256
    preserve_tables: bool = True
    preserve_images: bool = True
    preserve_headers: bool = True
    preserve_footers: bool = True
    preserve_hyperlinks: bool = True
    remove_hidden_text: bool = False
    remove_comments: bool = False
    remove_revisions: bool = False


@dataclass(slots=True, frozen=True)
class LoggingConfig:
    level: int = logging.INFO
    max_log_size_mb: int = 20
    backup_count: int = 10
    console_logging: bool = True
    file_logging: bool = True


@dataclass(slots=True, frozen=True)
class SecurityConfig:
    create_backup: bool = True
    verify_after_save: bool = True
    overwrite_output: bool = False
    safe_write: bool = True
    secure_temp_cleanup: bool = True


@dataclass(slots=True, frozen=True)
class UIConfig:
    language: str = "tr"
    theme: str = "system"
    remember_last_directory: bool = True
    confirm_before_exit: bool = True
    show_processing_time: bool = True
    show_statistics: bool = True


@dataclass(slots=True, frozen=True)
class AppConfig:
    debug: bool = _bool_env("WWCP_DEBUG", False)
    development: bool = _bool_env("WWCP_DEV", False)

    paths: PathsConfig = field(default_factory=PathsConfig)
    processing: ProcessingConfig = field(default_factory=ProcessingConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    security: SecurityConfig = field(default_factory=SecurityConfig)
    ui: UIConfig = field(default_factory=UIConfig)

    temp_root: Path = field(
        default_factory=lambda: Path(tempfile.gettempdir()) / "WWCP"
    )

    default_encoding: str = "utf-8"

    timeout_seconds: int = _int_env("WWCP_TIMEOUT", 600)


CONFIG = AppConfig()


SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = (
    ".docx",
)

SUPPORTED_MIME_TYPES: Final[tuple[str, ...]] = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
)

DEFAULT_OUTPUT_SUFFIX: Final[str] = "_cleaned"

LOG_FORMAT: Final[str] = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"


def ensure_directories() -> None:
    dirs = (
        CONFIG.paths.app_dir,
        CONFIG.paths.logs_dir,
        CONFIG.paths.temp_dir,
        CONFIG.paths.backup_dir,
        CONFIG.paths.cache_dir,
        CONFIG.paths.output_dir,
        CONFIG.temp_root,
    )

    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)


ensure_directories()
