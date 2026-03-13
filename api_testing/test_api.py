import requests
from pprint import pprint
from playwright.sync_api import sync_playwright

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# assert response.status_code == 200
# resp_dict = response.json()
# pprint(resp_dict)

def test_api_using_playwright():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://jsonplaceholder.typicode.com/posts/1", headers={"Accept": "application/json"})
        response_post = request.post("https://jsonplaceholder.typicode.com/posts", headers={"Content-Type": "application/json"}, data='{"title": "foo", "body": "bar", "userId": 1}')
        assert response_post.status == 201
        pprint(response_post.__dict__)
        pprint(response_post.json())
        assert response_post.json()["title"] == "foo"
        assert response.status == 200
        resp_dict = response.json()
        pprint(resp_dict)
        request.dispose()  # Clean up the request context after use