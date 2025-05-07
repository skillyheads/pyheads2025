# Node representation using dictionary
def create_node(key):
    return {"key": key, "left": None, "right": None}

# Insert a node into BST


def insert(root, key):
    if root is None:
        return create_node(key)

    if key < root["key"]:
        root["left"] = insert(root["left"], key)
    elif key > root["key"]:
        root["right"] = insert(root["right"], key)

    return root

# Find minimum value node


def find_min_node(root):
    current = root
    while current and current["left"]:
        current = current["left"]
    return current

# Delete a node from BST


def delete(root, key):
    if root is None:
        return None

    if key < root["key"]:
        root["left"] = delete(root["left"], key)
    elif key > root["key"]:
        root["right"] = delete(root["right"], key)
    else:
        # Case 1: Leaf node
        if root["left"] is None and root["right"] is None:
            return None

        # Case 2: Node with only one child
        if root["left"] is None:
            return root["right"]
        if root["right"] is None:
            return root["left"]

        # Case 3: Node with two children
        temp = find_min_node(root["right"])
        root["key"] = temp["key"]
        root["right"] = delete(root["right"], temp["key"])

    return root

# Search for a key


def search(root, key):
    if root is None or root["key"] == key:
        return root

    if key < root["key"]:
        return search(root["left"], key)
    return search(root["right"], key)

# In-order traversal


def inorder(root):
    result = []

    def inorder_helper(node):
        if node:
            inorder_helper(node["left"])
            result.append(node["key"])
            inorder_helper(node["right"])

    inorder_helper(root)
    return result

# Pre-order traversal


def preorder(root):
    result = []

    def preorder_helper(node):
        if node:
            result.append(node["key"])
            preorder_helper(node["left"])
            preorder_helper(node["right"])

    preorder_helper(root)
    return result

# Post-order traversal


def postorder(root):
    result = []

    def postorder_helper(node):
        if node:
            postorder_helper(node["left"])
            postorder_helper(node["right"])
            result.append(node["key"])

    postorder_helper(root)
    return result

# Height of BST


def height(root):
    if root is None:
        return -1

    left_height = height(root["left"])
    right_height = height(root["right"])

    return max(left_height, right_height) + 1

# Count nodes


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root["left"]) + count_nodes(root["right"])

# Check if BST is balanced


def is_balanced(root):
    if root is None:
        return True

    left_height = height(root["left"])
    right_height = height(root["right"])

    if abs(left_height - right_height) <= 1 and is_balanced(root["left"]) and is_balanced(root["right"]):
        return True

    return False

# Find successor (next larger value)


def successor(root, key):
    succ = None

    while root:
        if key < root["key"]:
            succ = root
            root = root["left"]
        elif key > root["key"]:
            root = root["right"]
        else:
            if root["right"]:
                succ = find_min_node(root["right"])
            break

    return succ

# Find predecessor (next smaller value)


def predecessor(root, key):
    pred = None

    while root:
        if key > root["key"]:
            pred = root
            root = root["right"]
        elif key < root["key"]:
            root = root["left"]
        else:
            if root["left"]:
                # Find the maximum value in left subtree
                curr = root["left"]
                while curr and curr["right"]:
                    curr = curr["right"]
                pred = curr
            break

    return pred

# Level order traversal (BFS)


def level_order(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node["key"])

        if node["left"]:
            queue.append(node["left"])
        if node["right"]:
            queue.append(node["right"])

    return result

# Check if tree is a valid BST


def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if root["key"] <= min_val or root["key"] >= max_val:
        return False

    return (is_bst(root["left"], min_val, root["key"]) and
            is_bst(root["right"], root["key"], max_val))

# Display BST (for visualization)


def display(root, space=0, increment=10):
    result = []

    def display_helper(node, space):
        if node is None:
            return

        space += increment
        display_helper(node["right"], space)

        result.append("\n" + " " * (space - increment) + str(node["key"]))
        display_helper(node["left"], space)

    display_helper(root, space)
    return "".join(result)

# Main test function


def test_bst():
    root = None

    # Insert nodes
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print("BST Display:")
    print(display(root))

    print("\nInorder traversal:", inorder(root))
    print("Preorder traversal:", preorder(root))
    print("Postorder traversal:", postorder(root))
    print("Level order traversal:", level_order(root))

    print("\nHeight of tree:", height(root))
    print("Number of nodes:", count_nodes(root))
    print("Is balanced:", is_balanced(root))
    print("Is valid BST:", is_bst(root))

    key = 40
    found = search(root, key)
    print(f"\nSearch for {key}:", "Found" if found else "Not found")

    succ = successor(root, key)
    print(f"Successor of {key}:", succ["key"] if succ else "None")

    pred = predecessor(root, key)
    print(f"Predecessor of {key}:", pred["key"] if pred else "None")

    print("\nDeleting 20 (leaf node)")
    root = delete(root, 20)
    print("Inorder after deletion:", inorder(root))

    print("\nDeleting 30 (node with one child)")
    root = delete(root, 30)
    print("Inorder after deletion:", inorder(root))

    print("\nDeleting 50 (root node with two children)")
    root = delete(root, 50)
    print("Inorder after deletion:", inorder(root))
    print("New root:", root["key"])


if __name__ == "__main__":
    test_bst()
