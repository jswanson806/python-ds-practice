def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    count1 = {}

    # for each element in the number (after converted to string to make iterable)
    for x in str(num1):
        # value of each key in count1 is +1 for each occurence
        count1[x] = count1.get(x, 0) + 1
    
    count2 = {}

    for y in str(num2):
        count2[y] = count2.get(y, 0) + 1

    # compare the two dictionaries
    return count1 == count2

