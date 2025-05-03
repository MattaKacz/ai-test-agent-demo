import pytest
from django.http import JsonResponse
from django.test.client import RequestFactory
from example.views import hello # Import the view
import json # Import the json module

@pytest.mark.django_db
def test_hello():
    # Create a request object
    factory = RequestFactory()
    request = factory.get('/hello/')
    # Call the hello function with the request
    response = hello(request)
    # Define the expected response
    expected_response = {"message": "Hello, world!"}
    # Check if the response is a JsonResponse
    assert isinstance(response, JsonResponse)
    # Check the content of the response
    assert json.loads(response.content) == expected_response