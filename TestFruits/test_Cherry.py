from Fruits.Cherry import Cherry

# Test setup: create an instance of Cherry
cherry = Cherry("USA","Golden-red","Light sour","June to August")

# tests are written as functions that start with the word "test"
def test_cherry_season():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert cherry.season() == "It grows in spring and summer months"

def test_cherry_price():
    assert cherry.price() == "It costs around $50"

