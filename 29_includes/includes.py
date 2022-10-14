def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # is collection is a dictionary
    if isinstance(collection, dict):
        # returns true if 'sought' is a value in 'collection'
        return sought in collection.values()
    # if no start provided or collection is a set
    if start is None or isinstance(collection, set):
        # returns true if 'sought' is in 'collection'
        return sought in collection
    # returns true if 'sought' is in 'collection' beginning with index 'start'
    return sought in collection[start:]