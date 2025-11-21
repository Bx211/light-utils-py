from light_utils.time_utils import to_hms


def test_to_hms():
assert to_hms(3600) == "01:00:00"
