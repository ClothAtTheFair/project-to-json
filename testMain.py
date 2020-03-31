import pytest
from main import *

class TestProjectListing:

    def test_file_can_be_loaded(self):
        test_file = "test.json"
        actual = load_JSON(test_file)
        assert type(actual) == dict

    def test_user_inputs_correctly_formatted(self):
        test_file = "test.json"
        inputs = dict(screenshots = "test.png", name="test", description="yikes", url="bradleycodes.dev")
        write_to_JSON(inputs, test_file)
        

    def test_wrong_screenshot_type_handled(self):
        screenshots = "test.csv"
        with pytest.raises(TypeError):
            type_checker(screenshots, "picture")

