from Fruits.Fruit import Fruits

def test_fruit_is_abstract():
    try:
        Fruits("USA", "Orange", "sweet-sour")
    except TypeError as e:
        assert "Can't instantiate abstract class Fruits" in str(e)
