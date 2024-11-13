import pytest
import requests
from tests.utils.configuration_reader import get_api_url, get_config_value
from tests.utils.data_loader import load_json_data
from pytest_selenium import webdriver

@pytest.fixture()
def id():
    """
        Create an object with POST to prepare for PATCH method
    """
    api_url = get_api_url() + "objects"
    request_data = load_json_data("data/test_data_post.json")
    
    response = requests.post(api_url, json=request_data)
    response_data = response.json()
    id = response_data.get("id")
    print(f"Newly created object ID: {id}/n")
    return id

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(get_config_value("BASE_URL"))
    yield driver

    driver.quit()