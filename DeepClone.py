def deep_clone(obj, memo=None):
    if memo is None:
        memo = {}

    obj_id = id(obj)

    if obj_id in memo:
        return memo[obj_id]

    match obj:
        case dict():
            cloned_obj = {}
            memo[obj_id] = cloned_obj
            for key, value in obj.items():
                cloned_obj[deep_clone(key, memo)] = deep_clone(value, memo)
            return cloned_obj

        case list():
            cloned_obj = []
            memo[obj_id] = cloned_obj
            for item in obj:
                cloned_obj.append(deep_clone(item, memo))
            return cloned_obj

        case tuple():
            cloned_obj = tuple(deep_clone(item, memo) for item in obj)
            memo[obj_id] = cloned_obj
            return cloned_obj

        case set():
            cloned_obj = set()
            memo[obj_id] = cloned_obj
            for item in obj:
                cloned_obj.add(deep_clone(item, memo))
            return cloned_obj

        case _:
            return obj


x = {"a": "b", "a2": ["first", "second"]}
y = {"b": x, "b3": ["firtsY", x]}
z = deep_clone(y)
print(z)