import pytest
from src.problem_5 import *


def test_trie_node_init():
    node = TrieNode()

    assert hasattr(node, "children"), "TrieNode should have a 'children' attribute"
    assert isinstance(node.children, dict), "TrieNode.children should be a dictionary"
    assert len(node.children) == 0, "TrieNode.children should be empty initially"

    assert hasattr(
        node, "is_end_of_word"
    ), "TrieNode should have an 'is_end_of_word' attribute"
    assert isinstance(
        node.is_end_of_word, bool
    ), "TrieNode.is_end_of_word should be a boolean"
    assert (
        node.is_end_of_word == False
    ), "TrieNode.is_end_of_word should be False initially"


def test_trie_node_insert():
    node = TrieNode()
    child = node.insert("a")

    assert "a" in node.children, "The inserted character should be a key in children"
    assert isinstance(child, TrieNode), "The insert method should return a TrieNode"
    assert (
        node.children["a"] is child
    ), "The returned child should be the same as the one in children"
