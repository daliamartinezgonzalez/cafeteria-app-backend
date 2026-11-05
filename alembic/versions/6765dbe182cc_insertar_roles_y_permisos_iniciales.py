from alembic import op
import sqlalchemy as sa

revision = '6765dbe182cc'
down_revision = '33d731bd6534'
branch_labels = None
depends_on = None


def upgrade() -> None:
    roles = sa.table(
        'roles',
        sa.column('id', sa.Integer),
        sa.column('nombre', sa.String)
    )

    permisos = sa.table(
        'permisos',
        sa.column('id', sa.Integer),
        sa.column('nombre', sa.String)
    )

    rol_permiso = sa.table(
        'rol_permiso',
        sa.column('id_rol', sa.Integer),
        sa.column('id_permiso', sa.Integer)
    )

    # Crear roles
    op.bulk_insert(roles, [
        {'id': 1, 'nombre': 'Admin'},
        {'id': 2, 'nombre': 'User'}
    ])

    # Crear permisos
    nombres_permisos = [
        'categorias.ver',
        'categorias.crear',
        'categorias.editar',
        'categorias.eliminar',
        'bebidas.ver',
        'bebidas.crear',
        'bebidas.editar',
        'bebidas.eliminar',
        'usuarios.ver',
        'usuarios.crear',
        'usuarios.editar',
        'usuarios.eliminar',
        'roles.ver',
        'roles.gestionar'
    ]

    op.bulk_insert(permisos, [
        {'id': i + 1, 'nombre': nombre}
        for i, nombre in enumerate(nombres_permisos)
    ])

    # Admin: todos los permisos
    asignaciones = [
        {'id_rol': 1, 'id_permiso': i}
        for i in range(1, 15)
    ]

    # User: consultar, crear y editar categorías y bebidas
    asignaciones += [
        {'id_rol': 2, 'id_permiso': i}
        for i in [1, 2, 3, 5, 6, 7]
    ]

    op.bulk_insert(rol_permiso, asignaciones)


def downgrade() -> None:
    op.execute("DELETE FROM rol_permiso")
    op.execute("DELETE FROM permisos")
    op.execute("DELETE FROM roles")