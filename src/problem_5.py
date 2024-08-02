# Represents a single node in the Trie
class TrieNode:
    """
    Represents a single node in a Trie data structure.

    Implements the basic functionality of a Trie node,
    including character insertion and end-of-word marking.

    Attributes:
        children (dict): A dictionary of child nodes, where keys are characters
                         and values are TrieNode objects.
        is_end_of_word (bool): Flag indicating if this node represents
                               the end of a word.

    Time complexity:
        - Initialization: O(1)
        - Node insertion: O(1) average case
    """

    def __init__(self):
        """
        Initialise a new TrieNode.

        Creates an empty dictionary for child nodes and sets the
        end-of-word flag to False.
        """
        # Initialize this node in the Trie
        self.children = {}
        self.is_end_of_word = False

    def insert(self, char: str) -> "TrieNode":
        """
        Adds a child node to this TrieNode.

        If the character doesn't exist, creates a new TrieNode for it.
        Returns the child node for the given character.

        Args:
            char (str): The character to insert.

        Returns:
            TrieNode: The child node corresponding to the inserted character.
        """
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def suffixes(self, suffix=""):
        """
        Recursive function that collects the suffix for all complete words below this point.

        Args:
            suffix (str): The current suffix being built (default '').

        Returns:
            list: A list of all suffixes of complete words starting from this node.

        Time complexity: O(n), where n is the total number of characters in all suffixes.
        Space complexity: O(n) for storing all suffixes.
        """
        results = []

        if self.is_end_of_word:
            results.append(suffix)

        for char, child_node in self.children.items():
            results.extend(child_node.suffixes(suffix + char))

        return results


# The Trie itself containing the root node and insert/find functions
class Trie:
    """
    Implements a Trie data structure.

    This class provides methods to insert words and find prefixes in the Trie.

    Attributes:
        root (TrieNode): The root node of the Trie.
    """

    def __init__(self):
        """
        Initialize this Trie (add a root node).
        """
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Add a word to the Trie.

        Args:
            word (str): The word to be inserted into the Trie.

        Time complexity: O(n), where n is the length of the word.
        Space complexity: O(n) in the worst case, if all characters are new.
        """
        # Add a word to the Trie
        node = self.root
        for char in word:
            node = node.insert(char)
        node.is_end_of_word = True

    def find(self, prefix: str) -> TrieNode:
        """
        Find the Trie node that represents this prefix.

        Args:
            prefix (str): The prefix to search for in the Trie.

        Returns:
            TrieNode: The node at the end of the prefix, or None if the prefix is not in the Trie.

        Time complexity: O(m), where m is the length of the prefix.
        """
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


def main():
    MyTrie = Trie()
    wordList = [
        "ant",
        "anthology",
        "antagonist",
        "antonym",
        "fun",
        "function",
        "factory",
        "trie",
        "trigger",
        "trigonometry",
        "tripod",
    ]

    for word in wordList:
        MyTrie.insert(word)

    while True:
        prefix = input("Enter a prefix (or press Enter to quit): ")
        if prefix == "":
            break

        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            suffixes = prefixNode.suffixes()
            if suffixes:
                print("Suffixes for '{}':".format(prefix))
                print("\n".join(suffixes))
            else:
                print("'{}' is a complete word with no suffixes.".format(prefix))
        else:
            print("'{}' not found".format(prefix))
        print()


if __name__ == "__main__":
    main()
