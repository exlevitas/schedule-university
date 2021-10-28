import pytest
from main.models import *


@pytest.mark.django_db
class TestEmailSend:
    def test_create_ticket(self, client) -> None:
        assert Email.objects.count() == 0
        response = client.post(
            "",
            {"author": "PyTest", "email":"asdjadsad@mail.ru"},
        )
        assert response.status_code == 201, response.data
        assert Email.objects.count() == 1
