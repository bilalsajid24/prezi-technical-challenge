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
        assert len(response.data["results"]) == 4
