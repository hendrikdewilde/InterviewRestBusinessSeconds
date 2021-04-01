import pytest

from Api.views import BusinessSecondsViewSet


@pytest.fixture(name="api_business_seconds")
def api_business_seconds():
    return BusinessSecondsViewSet
