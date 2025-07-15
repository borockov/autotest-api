import pytest
@pytest.mark.smoke
def test_user_exists():
    pass


@pytest.mark.regression
class TestUserFlow:
    @pytest.mark.smoke
    def test_user_can_login(self):
        pass

    def test_user_can_register(self):
        pass


@pytest.mark.feature_x
class TestFeatureX:
    @pytest.mark.smoke
    def test_feature_x_works(self):
        pass