"""
Modelos de datos - Horario
Define la estructura de horarios de trabajo
"""

from dataclasses import dataclass, asdict, field
from datetime import datetime, time
from typing import Optional, List
from enum import Enum

class ScheduleType(Enum):
    """Tipos de horarios"""
    CONTINUA = "continua"
    PARTIDA = "partida"
    ROTATORIA = "rotatoria"
    PERSONALIZADO = "personalizado"

@dataclass
class TimeSlot:
    """Representa un periodo de trabajo"""
    start_time: str = "07:00"  # HH:MM
    end_time: str = "17:00"    # HH:MM
    tolerance_minutes: int = 15  # Minutos de tolerancia

@dataclass
class Schedule:
    """Modelo de horario"""
    id: Optional[str] = None
    name: str = ""
    schedule_type: str = ScheduleType.CONTINUA.value
    time_slots: List[TimeSlot] = field(default_factory=lambda: [TimeSlot()])
    work_days: List[int] = field(default_factory=lambda: [0, 1, 2, 3, 4])  # 0=Lunes, 6=Domingo
    max_work_hours: float = 8.0
    break_minutes: int = 60
    created_at: str = None
    updated_at: str = None
    
    def __post_init__(self):
        """Inicializar valores por defecto"""
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.updated_at is None:
            self.updated_at = datetime.now().isoformat()
        
        # Convertir TimeSlot a diccionarios si es necesario
        if self.time_slots and isinstance(self.time_slots[0], dict):
            self.time_slots = [TimeSlot(**slot) for slot in self.time_slots]
    
    def to_dict(self):
        """Convertir a diccionario"""
        data = asdict(self)
        data['time_slots'] = [asdict(slot) for slot in self.time_slots]
        return data
    
    def get_display_name(self) -> str:
        """Obtener nombre para mostrar"""
        return self.name or self.schedule_type
    
    def is_work_day(self, day_of_week: int) -> bool:
        """Verificar si es día laboral"""
        return day_of_week in self.work_days
