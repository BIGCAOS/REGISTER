"""
Inicialización de base de datos
Crea las tablas y datos iniciales
"""

from tinydb import TinyDB, Query
from pathlib import Path
import json
from datetime import datetime
from config.config import DATABASE_PATH
from utils.logger import setup_logger
from models import User, UserRole
import bcrypt

logger = setup_logger()

def hash_password(password: str) -> str:
    """Hashear contraseña"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def initialize_database():
    """Inicializar base de datos con estructura y datos predeterminados"""
    
    try:
        db = TinyDB(DATABASE_PATH)
        
        # Obtener tablas
        users_table = db.table('users')
        employees_table = db.table('employees')
        attendance_table = db.table('attendance')
        schedules_table = db.table('schedules')
        
        logger.info("Base de datos conectada")
        
        # Verificar si ya existen datos
        if len(users_table) == 0:
            logger.info("Creando usuarios predeterminados...")
            
            # Usuario administrador
            admin_user = {
                'id': 'usr_001',
                'username': 'admin',
                'password_hash': hash_password('admin123'),
                'full_name': 'Administrador',
                'email': 'admin@register.local',
                'role': UserRole.ADMIN.value,
                'is_active': True,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'last_login': None
            }
            
            # Usuario supervisor
            supervisor_user = {
                'id': 'usr_002',
                'username': 'supervisor',
                'password_hash': hash_password('supervisor123'),
                'full_name': 'Supervisor',
                'email': 'supervisor@register.local',
                'role': UserRole.SUPERVISOR.value,
                'is_active': True,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'last_login': None
            }
            
            # Usuario operador
            operador_user = {
                'id': 'usr_003',
                'username': 'operador',
                'password_hash': hash_password('operador123'),
                'full_name': 'Operador',
                'email': 'operador@register.local',
                'role': UserRole.OPERADOR.value,
                'is_active': True,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'last_login': None
            }
            
            users_table.insert(admin_user)
            users_table.insert(supervisor_user)
            users_table.insert(operador_user)
            
            logger.info("✓ Usuarios predeterminados creados")
        
        # Crear horarios predeterminados si no existen
        if len(schedules_table) == 0:
            logger.info("Creando horarios predeterminados...")
            
            # Jornada continua
            schedule_continua = {
                'id': 'sch_001',
                'name': 'Jornada Continua',
                'schedule_type': 'continua',
                'time_slots': [
                    {'start_time': '07:00', 'end_time': '17:00', 'tolerance_minutes': 15}
                ],
                'work_days': [0, 1, 2, 3, 4],  # Lunes a viernes
                'max_work_hours': 8.0,
                'break_minutes': 60,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            
            # Jornada partida
            schedule_partida = {
                'id': 'sch_002',
                'name': 'Jornada Partida',
                'schedule_type': 'partida',
                'time_slots': [
                    {'start_time': '07:00', 'end_time': '12:00', 'tolerance_minutes': 15},
                    {'start_time': '14:00', 'end_time': '18:00', 'tolerance_minutes': 15}
                ],
                'work_days': [0, 1, 2, 3, 4],
                'max_work_hours': 8.0,
                'break_minutes': 120,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            
            schedules_table.insert(schedule_continua)
            schedules_table.insert(schedule_partida)
            
            logger.info("✓ Horarios predeterminados creados")
        
        db.close()
        logger.info("Base de datos inicializada correctamente")
        
    except Exception as e:
        logger.error(f"Error al inicializar base de datos: {str(e)}", exc_info=True)
        raise

def get_database():
    """Obtener instancia de base de datos"""
    return TinyDB(DATABASE_PATH)

def reset_database():
    """Reiniciar base de datos (CUIDADO - Elimina todos los datos)"""
    try:
        if DATABASE_PATH.exists():
            DATABASE_PATH.unlink()
            logger.warning("Base de datos eliminada")
        initialize_database()
        logger.info("Base de datos reiniciada")
    except Exception as e:
        logger.error(f"Error al reiniciar base de datos: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    initialize_database()
    print("✓ Base de datos inicializada")
