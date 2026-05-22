"""
Modelos de datos - Asistencia
Define la estructura de registro de asistencia
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
from enum import Enum

class AttendanceType(Enum):
    """Tipos de marcación"""
    ENTRADA = "entrada"
    SALIDA = "salida"

class AttendanceMethod(Enum):
    """Métodos de registro"""
    QR = "qr"
    MANUAL = "manual"

class AttendanceStatus(Enum):
    """Estados de asistencia"""
    PUNTUAL = "puntual"
    RETARDO = "retardo"
    AUSENCIA = "ausencia"
    JUSTIFICADO = "justificado"

@dataclass
class Attendance:
    """Modelo de registro de asistencia"""
    id: Optional[str] = None
    employee_id: str = ""
    employee_name: str = ""
    attendance_date: str = ""
    entry_time: Optional[str] = None
    exit_time: Optional[str] = None
    attendance_type: str = AttendanceType.ENTRADA.value
    method: str = AttendanceMethod.QR.value
    status: str = AttendanceStatus.PUNTUAL.value
    registered_by: str = ""
    observations: str = ""
    created_at: str = None
    
    def __post_init__(self):
        """Inicializar valores por defecto"""
        if self.attendance_date == "":
            self.attendance_date = datetime.now().date().isoformat()
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convertir a diccionario"""
        return asdict(self)
    
    @property
    def display_time(self) -> str:
        """Obtener hora formateada para mostrar"""
        if self.attendance_type == AttendanceType.ENTRADA.value:
            return self.entry_time.split('T')[1][:5] if self.entry_time else "--:--"
        else:
            return self.exit_time.split('T')[1][:5] if self.exit_time else "--:--"
