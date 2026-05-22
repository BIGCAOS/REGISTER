"""
Configuración general de la aplicación
"""

import os
from pathlib import Path
from enum import Enum

# Directorios base
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backups"
EXPORTS_DIR = BASE_DIR / "exports"
ASSETS_DIR = BASE_DIR / "assets"
QR_DIR = DATA_DIR / "qr"
LOGS_DIR = BASE_DIR / "logs"

# Crear directorios si no existen
DATA_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)
EXPORTS_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)
QR_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Base de datos
DATABASE_PATH = DATA_DIR / "database.json"

# Configuración de aplicación
APP_NAME = "REGISTER"
APP_VERSION = "1.0.0"
APP_AUTHOR = "BIGCAOS"
COMPANY_NAME = "Su Empresa"
COMPANY_LOGO = None

# Configuración de UI
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 600

# Temas
THEME_DARK = "dark"
THEME_LIGHT = "light"
DEFAULT_THEME = THEME_DARK

# Asistencia
TOLERANCE_MINUTES = 15  # Minutos de tolerancia para retardos
DUPLICATE_REGISTRATION_INTERVAL = 60  # Segundos para evitar duplicados

# Horarios predeterminados
DEFAULT_SCHEDULE_START = "07:00"
DEFAULT_SCHEDULE_END = "17:00"
DEFAULT_BREAK_MINUTES = 60
DEFAULT_WORK_HOURS = 8.0

# Seguridad
PASSWORD_MIN_LENGTH = 6
MAX_LOGIN_ATTEMPTS = 5
SESSION_TIMEOUT_MINUTES = 30

# QR
QR_BOX_SIZE = 10
QR_BORDER_SIZE = 4

# Base de datos predeterminada
DB_BACKUP_INTERVAL_HOURS = 24

# Configuración de exportación
EXCEL_HEADER_HEIGHT = 25
EXCEL_COLUMN_WIDTH = 15

# Métodos de registro
REGISTRATION_METHODS = {
    "QR": "qr",
    "MANUAL": "manual"
}

# Estados de asistencia
ATTENDANCE_STATUS = {
    "PUNTUAL": "puntual",
    "RETARDO": "retardo",
    "AUSENCIA": "ausencia",
    "JUSTIFICADO": "justificado"
}

class SystemConfig:
    """Clase para acceder a configuraciones del sistema"""
    
    @staticmethod
    def get_database_path() -> Path:
        """Obtener ruta de base de datos"""
        return DATABASE_PATH
    
    @staticmethod
    def get_qr_directory() -> Path:
        """Obtener directorio de QR"""
        return QR_DIR
    
    @staticmethod
    def get_exports_directory() -> Path:
        """Obtener directorio de exportaciones"""
        return EXPORTS_DIR
    
    @staticmethod
    def get_backups_directory() -> Path:
        """Obtener directorio de respaldos"""
        return BACKUP_DIR
    
    @staticmethod
    def get_assets_directory() -> Path:
        """Obtener directorio de assets"""
        return ASSETS_DIR
