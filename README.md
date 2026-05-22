# SISTEMA DE CONTROL Y REGISTRO DE ASISTENCIA

Sistema profesional de escritorio para gestión de asistencia de empleados mediante códigos QR y registro manual.

## Características

- ✅ Autenticación segura con roles y permisos
- ✅ Gestión completa de empleados
- ✅ Registro de asistencia por QR y manual
- ✅ Múltiples tipos de horarios
- ✅ Dashboard con estadísticas en tiempo real
- ✅ Exportación de reportes en Excel
- ✅ Base de datos NoSQL local
- ✅ Interfaz moderna con PySide6
- ✅ Diseño oscuro/claro

## Requisitos del Sistema

- Python 3.12+
- Windows/Linux/macOS
- Cámara web (para escaneo QR)

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/BIGCAOS/REGISTER.git
cd REGISTER

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Ejecutar aplicación
python main.py
```

### Credenciales de prueba

**Administrador:**
- Usuario: `admin`
- Contraseña: `admin123`

**Supervisor:**
- Usuario: `supervisor`
- Contraseña: `supervisor123`

**Operador:**
- Usuario: `operador`
- Contraseña: `operador123`

## Estructura del Proyecto

```
REGISTER/
├── main.py                 # Punto de entrada
├── requirements.txt        # Dependencias
├── README.md              # Este archivo
├── config/                # Configuración
│   ├── __init__.py
│   ├── config.py          # Valores de configuración
│   └── database_init.py   # Inicialización de BD
├── database/              # Gestión de datos
│   ├── __init__.py
│   └── db_manager.py      # Manager de base de datos
├── ui/                    # Interfaces gráficas
│   ├── __init__.py
│   ├── main_window.py     # Ventana principal
│   ├── dialogs/
│   │   ├── __init__.py
│   │   ├── login_dialog.py
│   │   ├── employee_dialog.py
│   │   ├── attendance_dialog.py
│   │   ├── schedule_dialog.py
│   │   └── export_dialog.py
│   ├── widgets/
│   │   ├── __init__.py
│   │   ├── dashboard_widget.py
│   │   ├── employee_widget.py
│   │   ├── attendance_widget.py
│   │   ├── schedule_widget.py
│   │   └── qr_widget.py
│   └── styles/
│       ├── __init__.py
│       ├── stylesheet.qss
│       └── theme_manager.py
├── controllers/           # Lógica de negocio
│   ├── __init__.py
│   ├── auth_controller.py
│   ├── employee_controller.py
│   ├── attendance_controller.py
│   ├── schedule_controller.py
│   └── export_controller.py
├── services/              # Servicios
│   ├── __init__.py
│   ├── qr_service.py      # Generación/lectura QR
│   ├── camera_service.py  # Captura de cámara
│   ├── export_service.py  # Exportación Excel
│   └── security_service.py # Seguridad
├── models/                # Modelos de datos
│   ├── __init__.py
│   ├── user.py
│   ├── employee.py
│   ├── attendance.py
│   ├── schedule.py
│   └── role.py
├── utils/                 # Utilidades
│   ├── __init__.py
│   ├── validators.py
│   ├── formatters.py
│   ├── constants.py
│   └── logger.py
├── assets/                # Recursos
│   ├── icons/
│   ├── qr/
│   ├── images/
│   └── fonts/
├── exports/               # Reportes generados
├── backups/               # Respaldos
└── logs/                  # Archivos de log
```

## Funcionalidades

### 1. Autenticación
- Login con usuario y contraseña
- Roles: Administrador, Supervisor, Operador
- Control de permisos por módulo
- Sesiones seguras

### 2. Gestión de Empleados
- Crear, editar, eliminar empleados
- Búsqueda y filtrado
- Generación automática de QR
- Foto de empleado

### 3. Registro de Asistencia
- Escaneo de QR en tiempo real
- Registro manual
- Validación de duplicados
- Confirmación visual y sonora

### 4. Horarios
- Jornada continua
- Jornada partida
- Horarios rotativos
- Personalización

### 5. Reportes
- Reportes diarios/semanales/mensuales
- Exportación Excel
- Filtros personalizados
- Estadísticas

## Configuración

Editar `config/config.py` para personalizar:
- Nombre de empresa
- Logo
- Tolerancia de retardos
- Horarios por defecto
- Directorios de almacenamiento

## Base de Datos

Utiliza TinyDB con almacenamiento local en:
- `data/database.json`

Incluye backup automático en:
- `backups/`

## Seguridad

- Contraseñas cifradas con bcrypt
- Validación de sesión
- Control de acceso basado en roles
- Logs de auditoría
- Sanitización de entrada

## Compilación a Ejecutable

```bash
# Generar ejecutable con PyInstaller
pyinstaller --onefile --windowed --icon=assets/icons/app.ico main.py
```

## Troubleshooting

### Problemas con cámara
- Verificar permisos de cámara
- Instalar OpenCV: `pip install opencv-python`

### Errores de base de datos
- Eliminar `data/database.json`
- Ejecutar `python config/database_init.py`

### Problemas de renderizado
- Actualizar drivers de GPU
- Usar `--disable-gpu` si es necesario

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crear rama feature
3. Commit cambios
4. Push y crear Pull Request

## Licencia

Este proyecto está bajo licencia MIT.

## Soporte

Para reportar bugs o sugerencias:
- Abrir un Issue en GitHub
- Contactar al equipo de desarrollo

---

**Versión:** 1.0.0
**Última actualización:** 2026-05-22
**Desarrollador:** BIGCAOS
