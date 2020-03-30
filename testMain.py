import pytest
from main import *

class TestProjectListing:

    def test_file_can_be_loaded(self):
        test_file = "./test.json"
        good_file = check_for_JSON(test_file)
        load_JSON(good_file)
        # From this there should be a status code to make sure it is good

    def test_file_is_found(self):
        test_file = "./test.json"
        actual = check_for_JSON(test_file)
        assert actual == True

    def test_user_inputs_correctly_formatted(self):
        inputs = dict(file = "./test.json", screenshots = "test.png", name="test", description="yikes", url="bradleycodes.dev")
        ahh = take_in_user_inputs(inputs)
        

    def test_wrong_inputs_handled(self):
        options = dict(file="./test.csv", screenshots= "test.csv", name= "test", description="yikes forever", url ="www.yikes.org")
        take_in_user_inputs(options)
