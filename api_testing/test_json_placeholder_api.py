import requests
from pprint import pprint
from playwright.sync_api import sync_playwright

def test_json_api():
    api = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(api)

    # pprint(response.__dict__)

    assert int(response.status_code) == 200
    pprint("\n")
    pprint(response.reason)
    response_json = response.json()

    print("\n")
    print(type(response_json))
    pprint(response_json)

    assert 'userId' in response_json.keys()
    assert response_json.get('userId') == 1, "Expected the userId to be 1"

def test_json_api_playwright():
    api = "https://jsonplaceholder.typicode.com/posts/1"
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get(api)
        pprint(response.status)
        pprint("\n")
        pprint(response.status_text)
        response_json = response.json()
        assert 'userId' in response_json.keys()
        assert response_json.get('userId') == 1, "Expected the userId to be 1"
