import pytest

from greetings import *

def test_greeting():
    name = "name"
    result = greet("name")

    assert result == "Hello, name."

def test_stand_in():
    result = greet(None)
    assert result == "Hello, my friend."

def test_shouting():
    shout_name = "TEST"
    unshout_name_1 = "test"
    unshout_name_2 = "Test"

    assert greet(shout_name) == "HELLO, TEST!"
    assert greet(unshout_name_1) == "Hello, test."
    assert greet(unshout_name_2) == "Hello, Test."

def test_two_names():
    name_1 = "test1"
    name_2 = "test2"

    assert greet([name_1, name_2]) == "Hello, test1, and test2."

def test_multiple_names():
    assert greet(["test1", "test2", "test3", "test4"]) == "Hello, test1, test2, test3, and test4."

def test_multiple_shout():
    assert greet(["test1", "test2", "TEST3"]) == "Hello, test1, and test2. AND HELLO, TEST3!"

def test_comma_string():
    assert greet(["test1", "test2, TEST3"]) == "Hello, test1, and test2. AND HELLO, TEST3!"

def test_escaped_comma():
    assert greet("\"test1, test2\"") == "Hello, test1, test2."