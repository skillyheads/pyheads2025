def create_stack(max_depth=150):
    return {"head": None, "max_depth": max_depth, "current_depth": 0}


def create_node(value):
    return {"prev": None, "data": value, "next": None}


def push(stack, number):
    new_node = create_node(number)
    if (stack["head"] is None):
        stack["head"] = new_node
    else:
        current_node = stack["head"]
        while (current_node["next"] is not None):
            current_node = current_node["next"]
        new_node["prev"] = current_node
        current_node["next"] = new_node


def pop(stack):
    if (stack["head"] is None):
        return None
    else:
        current_node = stack["head"]
        while (current_node["next"] is not None):
            current_node = current_node["next"]
        last_but_one = current_node["prev"]
        if (last_but_one is not None):
            last_but_one["next"] = None
        else:
            stack["head"] = None
        current_node["prev"] = None
        return current_node["data"]


stack = create_stack()

push(stack, 10)
push(stack, 5)
push(stack, 15)

print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))
