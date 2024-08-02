# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    """
    Represents a node in the Route Trie.

    Uses a dictionary to store children, which allows for fast lookups
    (O(1) on average).

    Attributes:
        children (dict): A dictionary to store child nodes.
        handler: The handler associated with this node (if it's an endpoint).
    """

    def __init__(self, *args):
        """
        Initialises a new RouterTrieNode

        We use a dictionary for children to achieve O(1) average case for insertions
        and lookups.

        Time complexity:
            O(1)
        """
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, *args):
        """
        Inserts a new path part as a child of this node.

        Creates a new child node if it doesn't exist.

        Dictionary look up and insertion in O(1).

        Args:
            *args: Variable length argument list.
                args[0] (str): The path part to insert.

        Time complexity: O(1) average case
        """
        # Insert the node as before
        if len(args) > 0:
            path_part = args[0]
            if path_part not in self.children:
                self.children[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    """
    A trie-like data structure for storing routes.

    This class implements a trie for HTTP routing.

    We use a trie is used because it allows us to efficiently store
    and retrieve paths, taking advantage of common prefixes in URLs.

    Attributes:
        root (RouteTrieNode): The root node of the trie.
    """

    def __init__(self, *args):
        """
        Initialise the RouteTrie.

        We start with a root node, which can have a handler (usually for the home page).

        Args:
            *args: Variable length argument list.
                args[0]: The handler for the root path (optional).

        Time complexity: O(1)
        """
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        if len(args) > 0:
            self.root.handler = args[0]

    def insert(self, *args):
        """
        Inserts a path and its associated handler into the trie.

        Breaks down the path into parts and creates nodes as needed.
        We traverse or create a node for each part of the path, setting the handler
        on the last node.

        Args:
            *args: Variable length argument list.
                args[0] (str): The path to insert.
                args[1]: The handler for the path.

        Time complexity: O(n) where n is the number of parts in the path
        """
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if len(args) < 2:
            return

        path, handler = args[0], args[1]
        current_node = self.root
        path_parts = self.split_path(
            path
        )  # moved method here because I did not know how best to call it form outside

        for part in path_parts:
            current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, *args):
        """
        Finds the handler for a given path.

        Args:
            *args: Variable length argument list.
                args[0] (str): The path to find.

        Returns:
            The handler for the path if found, None otherwise.

        Time complexity: O(n) where n is the number of parts in the path
        """
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(args) < 1:
            return None

        path = args[0]
        current_node = self.root
        path_parts = self.split_path(path)

        for part in path_parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler

    def split_path(self, path):
        """
        Splits a path into its constituent parts.

        Breaks a path into parts, removing empty strings.
        We use this to standardize our path processing.

        Args:
            path (str): The path to split.

        Returns:
            list: A list of path parts.

        Time complexity: O(n), where n is the length of the path
        """
        # Private helper function to split the path into parts
        return [p for p in path.split("/") if p]


class Router:
    """
    Uses a RouteTrie to store routes and their handlers.

    Provides a higher-level interface for working with routes. It encapsulates
    the RouteTrie and provides methods for adding handlers and looking up paths.

    Attributes:
        route_trie (RouteTrie): The trie used to store routes.
        not_found_handler: The handler to use when a route is not found.
    """

    def __init__(self, *args):
        """
        Initialises the Router.

        We set up the RouteTrie and store a not found handler for invalid routes.

        Args:
            *args: Variable length argument list.
                args[0]: The handler for the root path.
                args[1]: The handler for not found routes.

        Time complexity: O(1)
        """
        if len(args) >= 2:
            root_handler, not_found_handler = args[0], args[1]
        else:
            root_handler, not_found_handler = None, None
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, *args):
        """
        Adds a new route and its associated handler to our RouteTrie.

        Args:
            *args: Variable length argument list.
                args[0] (str): The path for the route.
                args[1]: The handler for the route.

        Time complexity: O(n), where n is the number of parts in the path
        """
        if len(args) >= 2:
            path, handler = args[0], args[1]
            self.route_trie.insert(path, handler)

    def lookup(self, *args):
        """
        Looks up a path in the RouteTrie.

        Args:
            *args: Variable length argument list.
                args[0] (str): The path to look up.

        Returns:
            The handler for the path if found, otherwise the not_found_handler.

        Time complexity: O(n), where n is the number of parts in the path
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
