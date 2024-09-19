import pytest

from server.presentations.models import Creator, Presentation
from services.presentations_parser import PresentationsParser

pytestmark = pytest.mark.django_db


class TestPresentationParser:

    def test_presentation_parser_creates_objects(self):
        assert Presentation.objects.count() == 0
        assert Creator.objects.count() == 0

        parser = PresentationsParser("/app/server/presentations/tests/test_data/test_data.json")
        parser.parse_and_save(image_request=False)

        assert Presentation.objects.count() == 4
        assert Creator.objects.count() == 4

    @pytest.mark.parametrize(
        "row",
        [
            {"name": "Bilal Sajid", "profileUrl": "https://randomurl"},
            {"name": "John", "profileUrl": "https://randomurl"},
        ]
    )
    def test_parse_creator(self, row):
        creator = PresentationsParser.parse_creator(row)
        assert creator.name == row["name"]
        assert creator.profile_url == row["profileUrl"]

    def test_parse_creator_create_unique_objects(self):
        raw_creator = {"name": "Bilal Sajid", "profileUrl": "https://randomurl"}
        creator = PresentationsParser.parse_creator(raw_creator)
        assert Creator.objects.count() == 1
        assert creator.name == raw_creator["name"]

        _ = PresentationsParser.parse_creator(raw_creator)
        # The count should still remain the same
        assert Creator.objects.count() == 1

    def test_parse_date(self):
        test_date_string = "March 6, 2014"
        datetime_object = PresentationsParser.parse_date(test_date_string)
        assert datetime_object.year == 2014
        assert datetime_object.month == 3

