from app.app import create_app
from app.fizzbuzz.fizzbuzz import fizzbuzz

flask_app = create_app()

def test_fizz():
    res = fizzbuzz(3)
    assert res == 'fizz'

def test_buzz():
    res = fizzbuzz(5)
    assert res == 'buzz'

def test_buzzfizz():
    res = fizzbuzz(15)
    assert res == 'fizzbuzz'

def test_number():
    res = fizzbuzz(2)
    assert res == 2
