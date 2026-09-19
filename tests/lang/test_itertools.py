from lang.itertools import deep_update, flatten


def test_insert_index_0():
    l = []
    try:
        l[0] = "abc"
        raise IndexError()
    except IndexError:
        pass

    l = ["abc"]
    l[0] = "def"


def test_flatten():
    l = [1, "string", 3]
    result = flatten(l)
    assert result == [1, "string", 3]

    l = [[1, 2, 3], 4, [5, 6, 7]]
    result = flatten(l)
    assert result == [1, 2, 3, 4, 5, 6, 7]

    l = [[[[[1, 2, 3]]], 4], [5, 6, 7]]

    result = flatten(l, -1)
    assert result == [[[[[1, 2, 3]]], 4], [5, 6, 7]]

    result = flatten(l, 0)
    assert result == [[[[[1, 2, 3]]], 4], [5, 6, 7]]

    result = flatten(l, 1)
    assert result == [[[[1, 2, 3]]], 4, 5, 6, 7]

    result = flatten(l, 2)
    assert result == [[[1, 2, 3]], 4, 5, 6, 7]

    result = flatten(l)
    assert result == [1, 2, 3, 4, 5, 6, 7]

    result = flatten(l, None)
    assert result == [1, 2, 3, 4, 5, 6, 7]


def test_deep_update_primitive():
    result = deep_update(1, 2)
    assert result == 2

    result = deep_update(1, "2")
    assert result == "2"

    result = deep_update(1, {})
    assert result == {}

    result = deep_update(1, [])
    assert result == []

    result = deep_update({}, "2")
    assert result == "2"

    result = deep_update([], "2")
    assert result == "2"

    result = deep_update(None, "2")
    assert result == "2"

    result = deep_update(None, {})
    assert result == {}

    result = deep_update(None, [])
    assert result == []

    result = deep_update(1, None)
    assert result == None

    result = deep_update({}, None)
    assert result == None

    result = deep_update([], None)
    assert result == None


def test_deep_update_dict():
    result = deep_update({}, {"1": "a"})
    assert result == {"1": "a"}

    result = deep_update({"2": "b"}, {"1": "a"})
    assert result == {"2": "b", "1": "a"}

    result = deep_update({"1": "b"}, {"1": "a"})
    assert result == {"1": "a"}

    result = deep_update({0: "b"}, ["a"])
    assert result == ["a"]

    result = deep_update({"1": "b"}, {"1": ["a"]})
    assert result == {"1": ["a"]}

    result = deep_update({"1": {"2": "b", "3": "d"}}, {"1": {"2": "c"}})
    assert result == {"1": {"2": "c", "3": "d"}}


def test_deep_update_list():
    result = deep_update([], [1, 2, 3])
    assert result == [1, 2, 3]

    result = deep_update([5], [1, 2, 3])
    assert result == [1, 2, 3]

    result = deep_update([5, 6, 7, 8], [1, 2, 3])
    assert result == [1, 2, 3, 8]
