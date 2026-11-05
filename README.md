
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

## Autor

Dalia Eunice Martínez González
