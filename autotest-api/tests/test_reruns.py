import random
import pytest

PLATFORM = "Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуски для маркировок flaky
def test_reruns():
    assert random.choice([True, False])  # Случайный выбор, для демонстранции нестабильного теста


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReRuns:
    def test_run_1(self):
        assert random.choice([True, False])

    def test_run_2(self):
        assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False])
