# Node representation using dictionary
def create_node(value):
    return {
        "value": value,
        "children": []
    }

# Create a new tree with a root value


def create_tree(root_value):
    return create_node(root_value)

# Add a child to a given node


def add_child(parent, value):
    child = create_node(value)
    parent["children"].append(child)
    return child

# Find a node with a specific value (returns None if not found)


def find_node(root, value):
    if root["value"] == value:
        return root

    for child in root["children"]:
        result = find_node(child, value)
        if result:
            return result

    return None

# Add a child to a node with a specific value


def add_child_to_value(root, parent_value, child_value):
    parent = find_node(root, parent_value)
    if parent:
        return add_child(parent, child_value)
    return None

# Print the tree in a readable format


def print_tree(root, level=0):
    indentation = "  " * level
    print(f"{indentation}{root['value']}")

    for child in root["children"]:
        print_tree(child, level + 1)

# Count total number of nodes in the tree


def count_nodes(root):
    count = 1  # Count the root

    for child in root["children"]:
        count += count_nodes(child)

    return count

# Find height of the tree (maximum depth)


def height(root):
    if not root["children"]:
        return 0

    max_child_height = 0
    for child in root["children"]:
        child_height = height(child)
        max_child_height = max(max_child_height, child_height)

    return max_child_height + 1

# Check if a value exists in the tree


def contains(root, value):
    if root["value"] == value:
        return True

    for child in root["children"]:
        if contains(child, value):
            return True

    return False

# Pre-order traversal: Root, Left, Right


def preorder_traversal(root):
    result = []

    def preorder_helper(node):
        result.append(node["value"])
        for child in node["children"]:
            preorder_helper(child)

    preorder_helper(root)
    return result

# Post-order traversal: Left, Right, Root


def postorder_traversal(root):
    result = []

    def postorder_helper(node):
        for child in node["children"]:
            postorder_helper(child)
        result.append(node["value"])

    postorder_helper(root)
    return result

# Level-order traversal (breadth-first)


def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node["value"])

        for child in node["children"]:
            queue.append(child)

    return result

# Get all leaf nodes (nodes with no children)


def get_leaf_nodes(root):
    result = []

    def find_leafs(node):
        if not node["children"]:
            result.append(node["value"])

        for child in node["children"]:
            find_leafs(child)

    find_leafs(root)
    return result

# Get path from root to a specific node


def find_path(root, value):
    path = []

    def find_path_helper(node, target, current_path):
        current_path.append(node["value"])

        if node["value"] == target:
            # Copy the current path to our result
            path.extend(current_path)
            return True

        for child in node["children"]:
            if find_path_helper(child, target, current_path):
                return True

        # Backtrack if target not found in this path
        current_path.pop()
        return False

    find_path_helper(root, value, [])
    return path

# Remove a node and its subtree


def remove_node(root, value):
    # Special case if the root itself needs to be removed
    if root["value"] == value:
        return None

    for i, child in enumerate(root["children"]):
        if child["value"] == value:
            # Remove this child
            root["children"].pop(i)
            return True

        # Recursively try to remove from this child's subtree
        if remove_node(child, value):
            return True

    return False

# Check if two trees are identical


def are_identical(root1, root2):
    # Check if values are the same
    if root1["value"] != root2["value"]:
        return False

    # Check if number of children is the same
    if len(root1["children"]) != len(root2["children"]):
        return False

    # Check all children recursively
    for child1, child2 in zip(root1["children"], root2["children"]):
        if not are_identical(child1, child2):
            return False

    return True

# Example usage of the tree


def test_tree():
    # Create a tree
    root = create_tree("Aanad")

    # Build the tree
    kumar = add_child(root, "Kumar")
    praveen = add_child(root, "Praveen")

    raja = add_child(kumar, "Raja")
    ravi = add_child(kumar, "Ravi")

    seetha = add_child(raja, "Seetha")

    latha = add_child(seetha, "Latha")
    igeetha = add_child(ravi, "Geetha")

    # Print the tree
    print("Tree structure:")
    print_tree(raja)

    # # Various operations
    # print("\nTotal nodes:", count_nodes(root))
    # print("Tree height:", height(root))
    # print("Contains 'G':", contains(root, "G"))
    # print("Contains 'X':", contains(root, "X"))

    # print("\nPreorder traversal:", preorder_traversal(root))
    # print("Postorder traversal:", postorder_traversal(root))
    # print("Level-order traversal:", level_order_traversal(root))

    # print("\nLeaf nodes:", get_leaf_nodes(root))
    # print("Path to 'I':", find_path(root, "I"))

    # # Remove a subtree
    # print("\nRemoving node 'C'")
    # remove_node(root, "C")
    # print("Tree after removal:")
    # print_tree(root)


test_tree()
