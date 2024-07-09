"""'Init'

Revision ID: baaca26f4a0f
Revises: 309844491a5f
Create Date: 2024-06-26 03:12:41.306791

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "baaca26f4a0f"
down_revision: Union[str, None] = "309844491a5f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_index("ix_users_email", table_name="users")


def downgrade():

    pass
