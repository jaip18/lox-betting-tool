"""deleted odds table

Revision ID: 8e95c318dcb8
Revises: ce0ffa4c1ad6
Create Date: 2025-05-02 18:30:54.260385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e95c318dcb8'
down_revision: Union[str, None] = 'ce0ffa4c1ad6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_odds_id', table_name='odds')
    op.drop_table('odds')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('odds',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('market_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('stat_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('over_under', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('line', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('odds_value', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='odds_event_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='odds_pkey')
    )
    op.create_index('ix_odds_id', 'odds', ['id'], unique=False)
    # ### end Alembic commands ###
