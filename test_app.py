from app import add_numbers, multiply_numbers, greet_user


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_multiply_numbers():
    assert multiply_numbers(4, 5) == 20


def test_greet_user():
    assert greet_user("AWS") == "Hello, AWS!"
