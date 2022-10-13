def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # empty set to hold number from last iteration
    already_visited = set()

    for i in nums:
        # the number needed to satisfy condition
        difference = goal - i
        # check if number needed is the last number
        if difference in already_visited:
            # if so, return the number needed and the current number as a tuple
            return(difference, i)
        # if not, add current number to set for next iteration
        already_visited.add(i)
    # if number needed is not found, return empty tuple
    return ()
