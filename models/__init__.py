"""
Modelos de datos - Usuario
Define la estructura de usuario en el sistema
"""

from enum import Enum
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

class UserRole(Enum):
    """Roles disponibles en el sistema"""
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    OPERADOR = "operador"

@dataclass
class User:
    """Modelo de usuario"""
    id: Optional[str] = None
    username: str = ""
    password_hash: str = ""
    full_name: str = ""
    email: str = ""
    role: str = UserRole.OPERADOR.value
    is_active: bool = True
    created_at: str = None
    updated_at: str = None
    last_login: Optional[str] = None
    
    def __post_init__(self):
        """Inicializar valores por defecto"""
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.updated_at is None:
            self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convertir a diccionario"""
        return asdict(self)
    
    def has_permission(self, permission: str) -> bool:
        """Verificar si el usuario tiene un permiso específico"""
        permissions = {
            UserRole.ADMIN.value: ["all"],
            UserRole.SUPERVISOR.value: ["view_employees", "register_attendance", "view_reports", "export_basic"],
            UserRole.OPERADOR.value: ["register_attendance", "view_basic"],
        }
        
        user_permissions = permissions.get(self.role, [])
        return "all" in user_permissions or permission in user_permissions
