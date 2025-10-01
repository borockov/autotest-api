from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_user, assert_get_user_response
from tools.assertions.schema import validate_json_schema
import pytest
from http import HTTPStatus


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client: PrivateUsersClient, function_user):
    response = private_users_client.get_user_me_api()
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)

    actual_user = CreateUserResponseSchema.model_validate_json(response.text).user

    expected_user = function_user.response.user

    assert_user(actual_user, expected_user)

    assert_get_user_response(response_data, function_user.response)

    validate_json_schema(response.json(), response_data.model_json_schema())
