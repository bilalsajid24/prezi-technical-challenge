import pytest

from server.presentations.models import Presentation


@pytest.fixture
def presentation_data():
    return [
        {
            "title": "Test presentation 1",
            "thumbnail": "https://picsum.photos/400/400",
        },
        {
            "title": "Test presentation 2",
            "thumbnail": "https://picsum.photos/400/400",
        },
        {
            "title": "Test Presentation 3",
            "thumbnail": "https://picsum.photos/400/400",
        },
        {
            "title": "Test Presentation 4",
            "thumbnail": "https://picsum.photos/400/400",
        }
    ]


@pytest.fixture
def multiple_presentations(presentation_data):
    presentations = []
    for row in presentation_data:
        presentations.append(Presentation(**row))

    Presentation.objects.bulk_create(presentations)

    yield presentations
