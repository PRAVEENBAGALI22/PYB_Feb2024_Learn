import pytest


# fixtures are aer used to start and tear down the methods before starting any test case
@pytest.fixture
def setUp():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    # to close the browser after executing the test case we use key word as yield
    yield
    print("Logoff")
    print("Close Browser")


# here we have setUp called where launch, login and browse happnes and then add product
def test_AddItemtoCart(setUp):
    "Item added successfully"


def test_RemoveFromCart(setUp):
    "Item removed successfully"
