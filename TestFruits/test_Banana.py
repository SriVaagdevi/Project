from Fruits.Banana import Banana

# Test setup: create an instance of Banana
banana = Banana("Kerala-India","Yellow","Light Sweet","110 calories")

# tests are written as functions that start with the word "test"
def test_banana_season():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert banana.season() == "It grows in all seasons"

def test_banana_price():
    assert banana.price() == "It costs around $10"

