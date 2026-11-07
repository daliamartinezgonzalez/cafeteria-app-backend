
# Cafeteria API

API REST para la administración de un catálogo de bebidas de una cafetería de especialidad. Permite gestionar usuarios, autenticación y permisos de acceso. Está desarrollada con FastAPI y PostgreSQL.

## Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker
- JWT (JSON Web Tokens)
- Pydantic

## Características

### Implementadas

- Conexión con PostgreSQL.
- Gestión de usuarios mediante operaciones CRUD.
- Autenticación mediante JWT.
- Consulta del perfil del usuario autenticado.
- Administración de roles y permisos.
- Validación de datos mediante esquemas.
- Documentación automática de endpoints con Swagger UI.
- Migraciones de base de datos mediante Alembic.

### En desarrollo

- Gestión de categorías de bebidas.
- Gestión del catálogo de bebidas.
- Administración de ingredientes y presentaciones.

## Requisitos previos

- Python 3.10 o superior.
- Docker y Docker Compose.
- Git.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/daliamartinezgonzalez/cafeteria-app-backend.git
```


### 2. Configurar las variables de entorno

### 3. Iniciar los contenedores

```bash
docker compose up -d --build
```

### 4. Ejecutar las migraciones

```bash
docker compose exec backend alembic upgrade head
```

### 5. Verificar el funcionamiento

La API estará disponible en:

```text
http://localhost:8000
```

## Documentación de la API

FastAPI genera documentación interactiva mediante Swagger UI.

```text
http://localhost:8000/docs
```

También está disponible la documentación alternativa:

```text
http://localhost:8000/redoc
```

## Autenticación

La API utiliza JWT para autenticar a los usuarios.

### Iniciar sesión

**POST** `/api/auth/login`

Permite iniciar sesión mediante correo electrónico y contraseña.

Ejemplo de solicitud:

```json
{
  "email": "admin@cafeteria.com",
  "password": "password123"
}
```

La respuesta incluye un token de acceso que se utiliza para consultar los endpoints protegidos.

### Consultar usuario autenticado

**GET** `/api/auth/me`

Requiere enviar el token JWT en el encabezado:

```text
Authorization: Bearer TOKEN
```

## Base de datos

Motor utilizado: PostgreSQL.

Se utiliza SQLAlchemy para la interacción con la base de datos y Alembic para gestionar las migraciones.

La estructura contempla la administración de usuarios, roles, permisos y el catálogo de bebidas.

## Control de versiones

El desarrollo se gestiona mediante Git y GitHub, utilizando commits descriptivos para identificar los cambios realizados.


## Autorización y permisos

La API utiliza autenticación mediante tokens JWT para identificar a los usuarios que acceden al sistema.

El acceso a las funcionalidades administrativas se controla mediante roles y permisos. Cada usuario tiene asignado un rol y cada rol puede tener diferentes permisos, lo que permite determinar qué operaciones puede realizar dentro de la aplicación.

Los permisos se verifican desde el backend antes de ejecutar las operaciones protegidas. De esta manera, no todos los usuarios tienen acceso a las mismas funcionalidades.

## Estructura del proyecto

El backend está organizado en diferentes carpetas para separar las responsabilidades de la aplicación:

- `app/`: configuración de la aplicación y conexión a la base de datos.
- `models/`: modelos de SQLAlchemy que representan las tablas de la base de datos.
- `schemas/`: esquemas de Pydantic para validar los datos de entrada y salida.
- `routers/`: definición de las rutas y endpoints de la API.
- `services/`: lógica de negocio y operaciones relacionadas con los datos.
- `alembic/`: configuración y archivos de migraciones de la base de datos.

Esta organización permite mantener el código ordenado y facilita su mantenimiento y ampliación.

## Endpoints de la API

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/auth/login` | Iniciar sesión y obtener un token de acceso |
| GET | `/api/auth/me` | Consultar la información del usuario autenticado |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/usuarios/` | Consultar todos los usuarios |
| GET | `/api/usuarios/{id}` | Consultar un usuario por su ID |
| POST | `/api/usuarios/` | Registrar un usuario |
| PUT | `/api/usuarios/{id}` | Reemplazar la información de un usuario |
| PATCH | `/api/usuarios/{id}` | Actualizar parcialmente la información de un usuario |
| DELETE | `/api/usuarios/{id}` | Eliminar un usuario |

### Categorías

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/categorias/` | Consultar todas las categorías |
| GET | `/api/categorias/{id}` | Consultar una categoría por su ID |
| POST | `/api/categorias/` | Registrar una categoría |
| PUT | `/api/categorias/{id}` | Reemplazar la información de una categoría |
| PATCH | `/api/categorias/{id}` | Actualizar parcialmente una categoría |
| DELETE | `/api/categorias/{id}` | Eliminar una categoría |

### Ingredientes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/ingredientes/` | Consultar todos los ingredientes |
| GET | `/api/ingredientes/{id}` | Consultar un ingrediente por su ID |
| POST | `/api/ingredientes/` | Registrar un ingrediente |
| PUT | `/api/ingredientes/{id}` | Reemplazar la información de un ingrediente |
| PATCH | `/api/ingredientes/{id}` | Actualizar parcialmente un ingrediente |
| DELETE | `/api/ingredientes/{id}` | Eliminar un ingrediente |

### Bebidas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/bebidas/` | Consultar todas las bebidas |
| GET | `/api/bebidas/{id}` | Consultar una bebida por su ID |
| POST | `/api/bebidas/` | Registrar una bebida |
| PUT | `/api/bebidas/{id}` | Reemplazar la información de una bebida |
| PATCH | `/api/bebidas/{id}` | Actualizar parcialmente una bebida |
| DELETE | `/api/bebidas/{id}` | Eliminar una bebida |