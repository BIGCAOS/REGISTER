"""
Modelos de datos - Empleado
Define la estructura de empleado en el sistema
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
from enum import Enum

class EmployeeStatus(Enum):
    """Estados posibles de un empleado"""
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    LICENCIA = "licencia"
    SUSPENDIDO = "suspendido"

class ScheduleType(Enum):
    """Tipos de horarios disponibles"""
    CONTINUA = "continua"
    PARTIDA = "partida"
    ROTATORIA = "rotatoria"
    PERSONALIZADO = "personalizado"

@dataclass
class Employee:
    """Modelo de empleado"""
    id: Optional[str] = None
    document: str = ""
    full_name: str = ""
    position: str = ""
    department: str = ""
    phone: str = ""
    email: str = ""
    status: str = EmployeeStatus.ACTIVO.value
    schedule_type: str = ScheduleType.CONTINUA.value
    hire_date: str = None
    qr_code: Optional[str] = None
    photo_path: Optional[str] = None
    created_at: str = None
    updated_at: str = None
    
    def __post_init__(self):
        """Inicializar valores por defecto"""
        if self.hire_date is None:
            self.hire_date = datetime.now().isoformat()
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.updated_at is None:
            self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convertir a diccionario"""
        return asdict(self)
    
    @property
    def display_name(self) -> str:
        """Obtener nombre completo formateado"""
        return self.full_name.upper()
