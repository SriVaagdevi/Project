from Fruits.Apple import Apple

# Test setup: create an instance of Apple
apple = Apple("Kashmir-India","Red","Sweet","Crisp")

# tests are written as functions that start with the word "test"
def test_apple_season():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert apple.season() == "It grows in Winter seaason"

def test_apple_price():
    assert apple.price() == "It costs around $80"


