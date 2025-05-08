# Node representation using dictionary
def create_node(key):
    return {"key": key, "left": None, "right": None}

# Insert a node into BST


def insert(node, key):
    if node is None:
        return create_node(key)

    if key < node["key"]:
        node["left"] = insert(node["left"], key)
    elif key > node["key"]:
        node["right"] = insert(node["right"], key)

    return node

# Find minimum value node


def find_min_node(node):
    current = node
    while current and current["left"]:
        current = current["left"]
    return current

# Delete a node from BST


def delete(node, key):
    if node is None:
        return None

    if key < node["key"]:
        node["left"] = delete(node["left"], key)
    elif key > node["key"]:
        node["right"] = delete(node["right"], key)
    else:
        # Case 1: Leaf node
        if node["left"] is None and node["right"] is None:
            return None

        # Case 2: Node with only one child
        if node["left"] is None:
            return node["right"]
        if node["right"] is None:
            return node["left"]

        # Case 3: Node with two children
        temp = find_min_node(node["right"])
        node["key"] = temp["key"]
        node["right"] = delete(node["right"], temp["key"])

    return node

# Search for a key


def search(node, key):
    if node is None or node["key"] == key:
        return node

    if key < node["key"]:
        return search(node["left"], key)
    return search(node["right"], key)

# In-order traversal


def inorder(node):
    result = []

    def inorder_helper(node):
        if node:
            inorder_helper(node["left"])
            result.append(node["key"])
            inorder_helper(node["right"])

    inorder_helper(node)
    return result

# Pre-order traversal


def preorder(node):
    result = []

    def preorder_helper(node):
        if node:
            result.append(node["key"])
            preorder_helper(node["left"])
            preorder_helper(node["right"])

    preorder_helper(node)
    return result

# Post-order traversal


def postorder(node):
    result = []

    def postorder_helper(node):
        if node:
            postorder_helper(node["left"])
            postorder_helper(node["right"])
            result.append(node["key"])

    postorder_helper(node)
    return result

# Height of BST


def height(node):
    if node is None:
        return -1

    left_height = height(node["left"])
    right_height = height(node["right"])

    return max(left_height, right_height) + 1

# Count nodes


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node["left"]) + count_nodes(node["right"])

# Check if BST is balanced


def is_balanced(node):
    if node is None:
        return True

    left_height = height(node["left"])
    right_height = height(node["right"])

    if abs(left_height - right_height) <= 1 and is_balanced(node["left"]) and is_balanced(node["right"]):
        return True

    return False

# Find successor (next larger value)


def successor(node, key):
    succ = None

    while node:
        if key < node["key"]:
            succ = node
            node = node["left"]
        elif key > node["key"]:
            node = node["right"]
        else:
            if node["right"]:
                succ = find_min_node(node["right"])
            break

    return succ

# Find predecessor (next smaller value)


def predecessor(node, key):
    pred = None

    while node:
        if key > node["key"]:
            pred = node
            node = node["right"]
        elif key < node["key"]:
            node = node["left"]
        else:
            if node["left"]:
                # Find the maximum value in left subtree
                curr = node["left"]
                while curr and curr["right"]:
                    curr = curr["right"]
                pred = curr
            break

    return pred

# Level order traversal (BFS)


def level_order(node):
    if node is None:
        return []

    result = []
    queue = [node]

    while queue:
        node = queue.pop(0)
        result.append(node["key"])

        if node["left"]:
            queue.append(node["left"])
        if node["right"]:
            queue.append(node["right"])

    return result

# Check if tree is a valid BST


def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if node["key"] <= min_val or node["key"] >= max_val:
        return False

    return (is_bst(node["left"], min_val, node["key"]) and
            is_bst(node["right"], node["key"], max_val))

# Display BST (for visualization)


def display(node, space=0, increment=10):
    result = []

    def display_helper(node, space):
        if node is None:
            return

        space += increment
        display_helper(node["right"], space)

        result.append("\n" + " " * (space - increment) + str(node["key"]))
        display_helper(node["left"], space)

    display_helper(node, space)
    return "".join(result)

# Main test function


def test_bst():
    node = None

    # Insert nodes
    node = insert(node, 50)
    insert(node, 30)
    insert(node, 20)
    insert(node, 40)
    insert(node, 70)
    insert(node, 60)
    insert(node, 80)
    insert(node, 35)
    insert(node, 46)
    insert(node, 38)
    insert(node, 83)

    print("BST Display:")
    print(display(node))

    print("\nInorder traversal:", inorder(node))
    print("Preorder traversal:", preorder(node))
    print("Postorder traversal:", postorder(node))
    print("Level order traversal:", level_order(node))

    print("\nHeight of tree:", height(node))
    print("Number of nodes:", count_nodes(node))
    print("Is balanced:", is_balanced(node))
    print("Is valid BST:", is_bst(node))

    key = 40
    found = search(node, key)
    print(f"\nSearch for {key}:", "Found" if found else "Not found")

    succ = successor(node, key)
    print(f"Successor of {key}:", succ["key"] if succ else "None")

    pred = predecessor(node, key)
    print(f"Predecessor of {key}:", pred["key"] if pred else "None")

    print("\nDeleting 20 (leaf node)")
    node = delete(node, 20)
    print("Inorder after deletion:", inorder(node))

    print("\nDeleting 30 (node with one child)")
    node = delete(node, 30)
    print("Inorder after deletion:", inorder(node))

    print("\nDeleting 50 (node node with two children)")
    node = delete(node, 50)
    print("Inorder after deletion:", inorder(node))
    print("New node:", node["key"])


test_bst()
