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


def test_trie_init():
    trie = Trie()
    assert isinstance(
        trie.root, TrieNode
    ), "Trie root should be an instance of TrieNode"
    assert len(trie.root.children) == 0, "Trie root should have no children initially"
    assert trie.root.is_end_of_word == False, "Trie root should not be end of word"


def test_trie_insert():
    trie = Trie()
    trie.insert("hello")

    # Check if each character is properly inserted
    node = trie.root
    for char in "hello":
        assert char in node.children, f"Character '{char}' should be in children"
        node = node.children[char]

    assert node.is_end_of_word == True, "Last node should be marked as end of word"

    # Insert another word with common prefix
    trie.insert("help")
    node = trie.root
    for char in "hel":
        assert char in node.children, f"Character '{char}' should be in children"
        node = node.children[char]
    assert "p" in node.children, "Character 'p' should be in children"
    assert (
        node.children["p"].is_end_of_word == True
    ), "Last node of 'help' should be marked as end of word"


def test_trie_find():
    trie = Trie()
    trie.insert("hello")
    trie.insert("help")

    # Test finding existing prefixes
    assert trie.find("he") is not None, "Should find prefix 'he'"
    assert trie.find("hello") is not None, "Should find word 'hello'"
    assert trie.find("help") is not None, "Should find word 'help'"

    # Test finding non-existent prefixes
    assert trie.find("hi") is None, "Should not find prefix 'hi'"
    assert trie.find("helping") is None, "Should not find word 'helping'"

    # Test that found nodes have correct properties
    hello_node = trie.find("hello")
    assert (
        hello_node.is_end_of_word == True
    ), "Node for 'hello' should be marked as end of word"

    he_node = trie.find("he")
    assert (
        he_node.is_end_of_word == False
    ), "Node for 'he' should not be marked as end of word"
    assert "l" in he_node.children, "Node for 'he' should have 'l' as a child"


# test suffixes
def test_trienode_suffixes():
    trie = Trie()
    words = ["hack", "hackerrank", "ham", "hammer", "hammock"]
    for word in words:
        trie.insert(word)

    # Test case 1: Suffixes from "hac" node
    hac_node = trie.find("hac")
    assert hac_node is not None, "Node 'hac' should exist"
    assert set(hac_node.suffixes()) == set(
        ["k", "kerrank"]
    ), "Incorrect suffixes for 'hac'"

    # Test case 2: Suffixes from "ham" node
    ham_node = trie.find("ham")
    assert ham_node is not None, "Node 'ham' should exist"
    assert set(ham_node.suffixes()) == set(
        ["", "mer", "mock"]
    ), "Incorrect suffixes for 'ham'"

    # Test case 3: Suffixes from root node
    assert set(trie.root.suffixes()) == set(words), "Incorrect suffixes from root"
