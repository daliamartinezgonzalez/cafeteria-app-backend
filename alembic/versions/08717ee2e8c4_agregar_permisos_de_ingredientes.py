"""agregar permisos de ingredientes

Revision ID: 08717ee2e8c4
Revises: 5848504109a9
Create Date: 2026-11-06 18:20:30.674335
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08717ee2e8c4'
down_revision: Union[str, Sequence[str], None] = '5848504109a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Agregar los permisos de ingredientes.
    op.execute("""
        INSERT INTO permisos (nombre)
        VALUES
            ('ingredientes.ver'),
            ('ingredientes.crear'),
            ('ingredientes.editar'),
            ('ingredientes.eliminar')
        ON CONFLICT (nombre) DO NOTHING;
    """)

    # Asignar todos los permisos al rol Admin.
    op.execute("""
        INSERT INTO rol_permiso (id_rol, id_permiso)
        SELECT 1, id
        FROM permisos
        WHERE nombre IN (
            'ingredientes.ver',
            'ingredientes.crear',
            'ingredientes.editar',
            'ingredientes.eliminar'
        )
        ON CONFLICT (id_rol, id_permiso) DO NOTHING;
    """)

    # Asignar permiso de consulta al rol User.
    op.execute("""
        INSERT INTO rol_permiso (id_rol, id_permiso)
        SELECT 2, id
        FROM permisos
        WHERE nombre = 'ingredientes.ver'
        ON CONFLICT (id_rol, id_permiso) DO NOTHING;
    """)


def downgrade() -> None:
    # Eliminar las asignaciones de los permisos de ingredientes.
    op.execute("""
        DELETE FROM rol_permiso
        WHERE id_permiso IN (
            SELECT id
            FROM permisos
            WHERE nombre IN (
                'ingredientes.ver',
                'ingredientes.crear',
                'ingredientes.editar',
                'ingredientes.eliminar'
            )
        );
    """)

    # Eliminar los permisos de ingredientes.
    op.execute("""
        DELETE FROM permisos
        WHERE nombre IN (
            'ingredientes.ver',
            'ingredientes.crear',
            'ingredientes.editar',
            'ingredientes.eliminar'
        );
    """)