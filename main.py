"""
Sistema de Control y Registro de Asistencia
Punto de entrada principal de la aplicación
"""

import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from ui.main_window import MainWindow
from config.database_init import initialize_database
from utils.logger import setup_logger
import logging

# Configurar logger
logger = setup_logger()

def main():
    """Punto de entrada de la aplicación"""
    try:
        # Inicializar base de datos
        logger.info("Inicializando base de datos...")
        initialize_database()
        
        # Crear aplicación
        app = QApplication(sys.argv)
        
        # Configurar aplicación
        app.setApplicationName("REGISTER - Sistema de Asistencia")
        app.setApplicationVersion("1.0.0")
        
        # Crear ventana principal
        logger.info("Creando ventana principal...")
        window = MainWindow()
        window.show()
        
        logger.info("Aplicación iniciada correctamente")
        
        # Ejecutar aplicación
        sys.exit(app.exec())
        
    except Exception as e:
        logger.error(f"Error fatal en aplicación: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
