from light_utils.file_utils import read_json_safe


def test_read_json_safe():
assert read_json_safe("non_exist.json") is None
