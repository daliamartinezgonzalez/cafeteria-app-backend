"""completar permisos de usuarios y roles

Revision ID: 2a1f70881449
Revises: 6765dbe182cc
Create Date: 2026-11-05 19:02:48.127962
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a1f70881449'
down_revision: Union[str, Sequence[str], None] = '6765dbe182cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Sincronizar la secuencia automática de permisos.
    op.execute("""
        SELECT setval(
            pg_get_serial_sequence('permisos', 'id'),
            COALESCE((SELECT MAX(id) FROM permisos), 1),
            true
        );
    """)

    # Agregar los permisos que faltan.
    op.execute("""
        INSERT INTO permisos (nombre)
        VALUES
            ('usuarios.ver'),
            ('usuarios.crear'),
            ('usuarios.editar'),
            ('usuarios.eliminar'),
            ('roles.ver'),
            ('roles.gestionar')
        ON CONFLICT (nombre) DO NOTHING;
    """)

    # Asignar todos los permisos al rol Admin.
    op.execute("""
        INSERT INTO rol_permiso (id_rol, id_permiso)
        SELECT 1, id
        FROM permisos
        ON CONFLICT (id_rol, id_permiso) DO NOTHING;
    """)

    # Asignar permisos de consulta, creación y edición al rol User.
    op.execute("""
        INSERT INTO rol_permiso (id_rol, id_permiso)
        SELECT 2, id
        FROM permisos
        WHERE nombre IN (
            'categorias.ver',
            'categorias.crear',
            'categorias.editar',
            'bebidas.ver',
            'bebidas.crear',
            'bebidas.editar'
        )
        ON CONFLICT (id_rol, id_permiso) DO NOTHING;
    """)


def downgrade() -> None:
    # Eliminar las asignaciones de los permisos nuevos.
    op.execute("""
        DELETE FROM rol_permiso
        WHERE id_permiso IN (
            SELECT id
            FROM permisos
            WHERE nombre IN (
                'usuarios.ver',
                'usuarios.crear',
                'usuarios.editar',
                'usuarios.eliminar',
                'roles.ver',
                'roles.gestionar'
            )
        );
    """)

    # Eliminar los permisos nuevos.
    op.execute("""
        DELETE FROM permisos
        WHERE nombre IN (
            'usuarios.ver',
            'usuarios.crear',
            'usuarios.editar',
            'usuarios.eliminar',
            'roles.ver',
            'roles.gestionar'
        );
    """)