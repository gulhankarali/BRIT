from datetime import datetime
import pytest
import requests
from tests.utils.configuration_reader import get_api_url
from tests.utils.data_loader import load_json_data


@pytest.mark.api
def test_patch_request_happy_path(id):
    """
        Happy Path scenario for PATCH method    
    """
    api_url = f"{get_api_url()}objects/{id}"

    request_data = load_json_data("data/test_data_patch.json")
    expected_result_data = load_json_data("data/expected_result_patch.json")
    
    response = requests.patch(api_url, json=request_data)

    assert response.status_code == 200, f"Expected 200, got: {response.status_code}"

    response_data = response.json()

    assert response_data["name"] == expected_result_data["name"], "Name does not match"
    assert response_data["data"]["year"] == expected_result_data["data"]["year"], "Year does not match"
    assert response_data["data"]["price"] == expected_result_data["data"]["price"], "Price does not match"
    assert response_data["data"]["CPU model"] == expected_result_data["data"]["CPU model"], "CPU model does not match"
    assert response_data["data"]["Hard disk size"] == expected_result_data["data"]["Hard disk size"], "Hard disk size does not match"
    
    response_date = datetime.strptime(response_data["updatedAt"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
    expected_date = datetime.today()
    assert response_date.date() == expected_date.date(), f"Date mismatch. Actual: {response_date.date()}, Expected: {expected_date.date()}"

@pytest.mark.api
def test_patch_request_large_values(id):
    """
        Invalid values in the payload (large values) for PATCH method
    """
    api_url = f"{get_api_url()}objects/{id}"

    request_data = {
        "name": "Apple MacBook Pro 16" * 1000,
        "data": {
            "year": 2023,
            "price": 1e10,  # Large price
            "CPU model": "Intel Core i9" * 100,
            "Hard disk size": "1 TB"
        }
    }

    response = requests.patch(api_url, json=request_data)
    assert response.status_code == 500, f"Expected 500,  got {response.status_code}"

@pytest.mark.api
def test_patch_request_non_existent_id():
    """
        Validation of non existent ID for PATCH request   
    """
    non_existent_id = "nonexistent1"
    api_url = f"{get_api_url()}objects/{non_existent_id}"

    request_data = load_json_data("data/test_data_patch.json")
    response = requests.patch(api_url, json=request_data)

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
