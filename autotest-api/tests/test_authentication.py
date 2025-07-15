# autotests-api/tests/test_authentication.py

from http import HTTPStatus

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code

from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import get_authentication_client
import pytest

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    users_client = get_public_users_client()
    auth_client = get_authentication_client()

    user_data = CreateUserRequestSchema()
    users_client.create_user_api(user_data)

    login_request = LoginRequestSchema(
        email=user_data.email,
        password=user_data.password
    )

    login_response = auth_client.login_api(login_request)

    assert_status_code(login_response.status_code, HTTPStatus.OK)

    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_login_response(login_response_data)
