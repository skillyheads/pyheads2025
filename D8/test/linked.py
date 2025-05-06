def create_node(value):
    return {"data": value, "next": None}


def create_linked_list():
    return {"head": None}


def add(linked_list, value, index=-1):
    node = create_node(value)
    current = None
    if (linked_list["head"] is None):
        linked_list["head"] = node
    else:
        current = linked_list["head"]
        if (index != -1):
            for i in range(index-1):
                if (current["next"] is not None):
                    current = current["next"]
                else:
                    break
            node["next"] = current["next"]
            current["next"] = node
        else:
            while (current["next"] is not None):
                current = current["next"]
            current["next"] = node


def traverse(linked_list):
    current = linked_list["head"]
    while True:
        print(current["data"])
        current = current["next"]
        if (current is None):
            break


linked_list = create_linked_list()
add(linked_list, 10)
add(linked_list, 50)
add(linked_list, 70)
add(linked_list, 30)
add(linked_list, 20, 2)

traverse(linked_list)
