from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    return datetime.now(UTC)


class ProjectStatus(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    ARCHIVED = "archived"


class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(min_length=1, max_length=200, index=True)
    status: ProjectStatus = Field(
        default=ProjectStatus.DEVELOPMENT,
        sa_column=sa.Column(
            sa.Enum(
                ProjectStatus,
                name="project_status",
                values_callable=lambda enum_class: [
                    member.value for member in enum_class
                ],
            ),
            nullable=False,
            index=True,
        ),
    )
    production_url: str | None = Field(default=None, max_length=2048)
    created_at: datetime = Field(
        default_factory=utc_now,
        sa_column=sa.Column(
            sa.DateTime(timezone=True),
            nullable=False,
        ),
    )
    updated_at: datetime = Field(
        default_factory=utc_now,
        sa_column=sa.Column(
            sa.DateTime(timezone=True),
            nullable=False,
            onupdate=utc_now,
        ),
    )
