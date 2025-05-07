def create_queue(max_depth=150):
    return {"head": None, "max_depth": max_depth, "current_depth": 0}


def create_node(value):
    return {"prev": None, "data": value, "next": None}


def push(queue, number):
    new_node = create_node(number)
    if (queue["head"] is None):
        queue["head"] = new_node
    else:
        current_node = queue["head"]
        while (current_node["next"] is not None):
            current_node = current_node["next"]
        new_node["prev"] = current_node
        current_node["next"] = new_node


def pull(queue):
    if (queue["head"] is None):
        return None
    else:
        current_node = queue["head"]
        queue["head"] = queue["head"]["next"]
        if (queue["head"] is not None):
            queue["head"]["prev"] = None
        current_node["next"] = None
        return current_node["data"]


queue = create_queue()

push(queue, 10)
push(queue, 5)
push(queue, 15)

print(pull(queue))
print(pull(queue))
print(pull(queue))
print(pull(queue))
