from collections.abc import Iterable


def is_iter(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        pass
    return False


def is_iter_not_str(obj):
    return is_iter(obj) and not isinstance(obj, str)


def is_dict(obj):
    return (
        hasattr(obj, "__getitem__")
        and hasattr(obj, "__setitem__")
        and hasattr(obj, "items")
    )


def deep_update(
    target: dict | list | str | complex | None,
    source: dict | list | str | complex | None,
):
    """recursively updates two json like objects (dict, list, primitive)

    Args:
        target (dict | list | str | int | float | complex | None): the object to update into
        source (dict | list | str | int | float | complex | None): the object to "overlay"

    Returns:
        dict | list | str | int | float | complex | None: an updated target with source "overlayed" on top
    """
    if is_dict(target):
        if is_dict(source):
            for k, v in source.items():
                target[k] = deep_update(target[k], v) if k in target else v
            return target
        else:
            return source
    elif is_iter_not_str(target):
        if is_iter_not_str(source):
            len_target = len(target)
            for i, e in enumerate(source):
                if i <= len_target - 1:
                    target[i] = deep_update(target[i], e)
                else:
                    target.append(e)
            return target
        else:
            return source
    else:
        return source


def flatten(
    iterable: Iterable, depth: int | None = None, result: list | None = None
) -> list:
    """flattens a list

    Args:
        iterable (Iterable): the iterable to flatten. Characters that comprise a str are not iterated over; the str is taken as a whole element.
        depth (Optional[int], optional): recursion depth. Defaults to None. Use None to recurse infinitely.
        result (Optional[list], optional): a curried output to mutate

    Returns:
        list: a flattened list
    """
    if result is None:
        result = []

    for item in iterable:
        if is_iter_not_str(item) and (depth is None or depth > 0):
            flatten(item, None if depth is None else depth - 1, result)
        else:
            result.append(item)

    return result
