import datetime
import pytest

from rest_framework import status

from server.presentations.api.views import PresentationListAPIView

pytestmark = pytest.mark.django_db


class TestPresentationAPIView:

    @staticmethod
    def _get_response(rf, param=""):
        request = rf.get(f'/api/v1/presentations/{param}')
        return PresentationListAPIView.as_view()(request)

    def test_list_presentation(self, rf, multiple_presentations):
        response = self._get_response(rf)
        assert response.status_code == status.HTTP_200_OK

        # Since the page size is two, the API should return only two results
        assert len(response.data["results"]) == 2

    def test_pagination_for_api(self, rf, multiple_presentations):
        response = self._get_response(rf, "?page=2")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 2

    def test_full_text_search_function(self, rf, multiple_presentations):
        response = self._get_response(rf, "?search=Test presentation 1")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1

        presentation = response.data["results"][0]
        assert presentation["title"] == "Test presentation 1"
        assert presentation["thumbnail"] == "https://picsum.photos/400/400"

    def test_incomplete_text_search_function(self, rf, multiple_presentations):
        response = self._get_response(rf, "?search=Test")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 2

        for index, presentation in enumerate(response.data["results"]):
            assert presentation["title"] == f"Test presentation {index + 1}"
            assert presentation["thumbnail"] == "https://picsum.photos/400/400"

    @pytest.mark.parametrize("order", ["asc", "desc"])
    def test_order_by_created_date(self, rf, multiple_presentations, order):
        expected_first_obj = multiple_presentations[0]
        if order == "asc":
            expected_first_obj.created_at = datetime.datetime.now() - datetime.timedelta(days=2)
            param = "created_at"
        else:
            expected_first_obj.created_at = datetime.datetime.now() + datetime.timedelta(days=2)
            param = "-created_at"

        expected_first_obj.save()

        response = self._get_response(rf, f"?ordering={param}")
        assert response.status_code == status.HTTP_200_OK

        first_obj = response.data["results"][0]
        assert first_obj["title"] == expected_first_obj.title
