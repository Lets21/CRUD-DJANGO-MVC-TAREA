
# CRUD-DJANGO-MVC-TAREA

Este proyecto es una aplicación web creada con Django que implementa un sistema de gestión de productos, incluyendo un CRUD (Crear, Leer, Actualizar, Eliminar) con autenticación de usuarios. Los usuarios pueden registrarse, iniciar sesión y gestionar productos que están asociados a su cuenta. La aplicación también utiliza Bootstrap para el diseño y un sistema de autenticación integrado con el decorador `@login_required` de Django para restringir el acceso a funciones específicas según el estado de autenticación.

## Contenido

- Requisitos
- Instalación
- Configuración
- Estructura del Proyecto
- Uso
  - Registro de Usuario
  - Inicio de Sesión
  - Gestión de Productos
- Migraciones de Base de Datos
- Dependencias
- Contribuciones

## Requisitos

- **Python 3.10 o superior**: Este proyecto requiere Python para ejecutar el entorno de Django.
- **Django 5.0.9**: La versión de Django utilizada en este proyecto es la 5.0.9.
- **Base de datos SQL Server**: La base de datos se conecta utilizando el controlador ODBC de Microsoft SQL Server.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/CRUD-DJANGO-MVC-TAREA.git
   ```

2. Crea un entorno virtual en tu máquina local:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - En Windows:
     ```bash
     venv\Scripts ctivate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. Configura la base de datos en el archivo `settings.py`. Asegúrate de modificar los campos de la base de datos para que coincidan con tu configuración de SQL Server:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'mssql',
           'NAME': 'nombre_de_tu_base_de_datos',
           'USER': 'tu_usuario',
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '1433',
       }
   }
   ```

2. Realiza las migraciones necesarias para crear las tablas en la base de datos:

   ```bash
   python manage.py migrate
   ```

3. Crea un superusuario para acceder al panel de administración de Django:

   ```bash
   python manage.py createsuperuser
   ```

4. Inicia el servidor local de desarrollo:

   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

El proyecto sigue el patrón MVC (Model-View-Controller) y está organizado de la siguiente manera:

```bash
myproject/
│
├── myapp/                 # Aplicación principal
│   ├── migrations/        # Migraciones de base de datos
│   ├── models.py          # Definición de los modelos (Producto, Usuario)
│   ├── views.py           # Vistas para manejar CRUD y autenticación
│   ├── forms.py           # Formularios de registro y creación de productos
│   ├── urls.py            # Definición de rutas
│   └── templates/         # Plantillas HTML
│       └── registration/  # Plantillas de login y registro
│
├── manage.py              # Script para ejecutar el proyecto
└── db.sqlite3             # Base de datos SQLite por defecto (puede ser SQL Server en tu caso)
```

## Uso

### Registro de Usuario

Para registrarte como nuevo usuario, navega a la ruta `/signup/`. Completa el formulario de registro con un nombre de usuario y contraseña. Una vez registrado, serás redirigido a la página de inicio de sesión.

### Inicio de Sesión

Una vez que hayas creado una cuenta, puedes iniciar sesión desde la página `/login/`. Tras iniciar sesión, tendrás acceso a todas las funcionalidades del sistema CRUD.

### Gestión de Productos

Los productos pueden ser gestionados (creados, editados y eliminados) desde la página principal `/productos/`. Las acciones de CRUD solo están disponibles para usuarios autenticados. Las rutas principales son:

- **Crear producto**: `/crear/`
- **Editar producto**: `/editar/<id>/`
- **Eliminar producto**: `/eliminar/<id>/`

Los productos están asociados al usuario que los crea, de manera que cada usuario tiene control sobre los productos que ha añadido.

## Migraciones de Base de Datos

Para aplicar las migraciones de la base de datos, usa el siguiente comando:

```bash
python manage.py makemigrations
python manage.py migrate
```

Este comando aplicará todas las migraciones pendientes y actualizará tu base de datos con los nuevos cambios.

## Dependencias

Las principales dependencias de este proyecto son:

- **Django**: El framework web principal.
- **pyodbc**: Para la conexión con SQL Server.
- **Bootstrap 5**: Para la estilización de la interfaz.
- **Microsoft ODBC Driver 17 for SQL Server**: Necesario para conectar la base de datos SQL Server.

Todas las dependencias están especificadas en el archivo `requirements.txt`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

¡Gracias por contribuir!
