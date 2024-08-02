# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, *args):
        """
        Time complexity:
            O(1)
        """
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, *args):
        """
        Time complexity:
            O(1)
        """
        # Insert the node as before
        if len(args) > 0:
            path_part = args[0]
            if path_part not in self.children:
                self.children[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, *args):
        """
        Time complexity:
            O(1)
        """
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        if len(args) > 0:
            self.root.handler = args[0]

    def insert(self, *args):
        """
        Time complexity:
            O(n) where n is the number of parts in the path
        """
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if len(args) < 2:
            return

        path, handler = args[0], args[1]
        current_node = self.root
        path_parts = self._split_path(path)  # Changed from split_path to _split_path

        for part in path_parts:
            current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, *args):
        """
        Time complexity:
            O(n) where n is the number of parts in the path
        """
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(args) < 1:
            return None

        path = args[0]
        current_node = self.root
        path_parts = self._split_path(path)  # Changed from split_path to _split_path

        for part in path_parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler

    def _split_path(self, path):
        """
        Time complexity:
            O(n), where n is the length of the path
        """
        # Private helper function to split the path into parts
        return [p for p in path.split("/") if p]


class Router:
    def __init__(self, *args):
        """
        Time complexity:
            O(1)
        """
        if len(args) >= 2:
            root_handler, not_found_handler = args[0], args[1]
        else:
            root_handler, not_found_handler = None, None
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, *args):
        """
        Time complexity:
            O(n), n is the nuber of parts in the path
        """
        if len(args) >= 2:
            path, handler = args[0], args[1]
            self.route_trie.insert(path, handler)

    def lookup(self, *args):
        """
        Time complexity:
            O(n), the number of parts in the path
        """
        if len(args) < 1:
            return self.not_found_handler

        path = args[0]
        if path == "/":
            return self.route_trie.root.handler

        handler = self.route_trie.find(path)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, *args):
        """
        Time complexity:
            O(n), n is the length of the paths string
        """
        if len(args) < 1:
            return []
        return self.route_trie.split_path(args[0])
