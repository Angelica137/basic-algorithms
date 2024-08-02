import pytest
from src.problem_7 import *


@pytest.fixture
def router():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")
    return router


def test_root_path(router):
    assert router.lookup("/") == "root handler"


def test_not_found_path(router):
    assert router.lookup("/home") == "not found handler"


def test_existing_path(router):
    assert router.lookup("/home/about") == "about handler"


def test_existing_path_with_trailing_slash(router):
    assert router.lookup("/home/about/") == "about handler"


def test_non_existing_nested_path(router):
    assert router.lookup("/home/about/me") == "not found handler"


# Additional test to check behavior when adding a handler
def test_add_handler(router):
    router.add_handler("/new/path", "new handler")
    assert router.lookup("/new/path") == "new handler"


# Test to check behavior with empty path
def test_empty_path(router):
    assert router.lookup("") == "root handler"


# Test to check behavior with very nested path
def test_deeply_nested_path(router):
    router.add_handler("/a/b/c/d/e", "nested handler")
    assert router.lookup("/a/b/c/d/e") == "nested handler"
    assert router.lookup("/a/b/c/d") == "not found handler"


# Test to check behavior with similar paths
def test_similar_paths(router):
    router.add_handler("/home/about/me", "about me handler")
    assert router.lookup("/home/about") == "about handler"
    assert router.lookup("/home/about/me") == "about me handler"
