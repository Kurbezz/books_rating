"""empty message

Revision ID: 3f2d20b8fb01
Revises: 
Create Date: 2022-04-09 17:11:46.022557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3f2d20b8fb01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ratings",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("book_id", sa.BigInteger(), nullable=False),
        sa.Column("rate", sa.SmallInteger(), nullable=False),
        sa.Column("updated", sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "book_id", name="uc_ratings_user_id_book_id"),
    )
    op.create_index(op.f("ix_ratings_user_id"), "ratings", ["user_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_ratings_user_id"), table_name="ratings")
    op.drop_table("ratings")
    # ### end Alembic commands ###