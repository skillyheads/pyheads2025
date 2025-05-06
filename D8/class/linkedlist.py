# 10,20,4,56,78,98

def create_node(value):
    return {"data": value, "next": None}


def add(head_node, value):
    # append at the end of the linked list
    node = create_node(value)
    if (head_node is None):
        return node
    else:
        current_node = head_node
        while True:
            if (current_node["next"] is None):
                current_node["next"] = node
                break
            else:
                current_node = current_node["next"]


def insert(head_node, value, index):
    node = create_node(value)
    current_node = head_node
    if index == 0:
        node["next"] = head_node
        return node
    else:
        if (head_node is None):
            return node
        else:
            i = 0
            while i < index-1 and (current_node["next"] is not None):
                current_node = current_node["next"]
                i += 1
            node["next"] = current_node["next"]
            current_node["next"] = node
            return head_node


def tranverse(head_node):
    current_node = head_node
    while current_node is not None:
        print(current_node["data"])
        current_node = current_node["next"]


head_node = add(None, 10)
add(head_node, 20)
# head_node["next"]["next"] = create_node(4)
add(head_node, 4)
# head_node["next"]["next"]["next"] = create_node(56)
add(head_node, 56)

head_node = insert(head_node, 65, 0)
tranverse(head_node)
