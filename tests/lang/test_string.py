def test_string_is_iter():
    """demonstrate a common gotcha of iterating without knowing types.
    Sometimes you think you are iterating a list, but you receive a string, e.g.
    ["a", "b", "c"], vs "a, b, c"; and they will both iterate"""
    string = "string"

    assert hasattr(string, "__iter__") == True
    assert hasattr(string, "__getitem__") == True

    is_iter = True
    try:
        iter(string)
    except TypeError:
        is_iter = False

    assert is_iter is True
