from datetime import UTC
from uuid import UUID

import pytest
from pydantic import ValidationError

from projects_service.models import Project, ProjectStatus


def test_projects_has_expected_defaults() -> None:
    project = Project(name="Mosquera Soft")

    assert isinstance(project.id, UUID)
    assert project.status is ProjectStatus.DEVELOPMENT
    assert project.production_url is None
    assert project.created_at.tzinfo is UTC
    assert project.updated_at.tzinfo is UTC


def test_project_accepts_production_data() -> None:
    project = Project(
        name="Portfolio",
        status=ProjectStatus.PRODUCTION,
        production_url="http://example.com",
    )

    assert project.status is ProjectStatus.PRODUCTION
    assert project.production_url == "http://example.com"


def test_project_rejects_empty_name() -> None:
    with pytest.raises(ValidationError):
        Project.model_validate({"name": ""})
