def top_n(items, n):
    """Return the top n items in an array, in descending Order.
    
    Args:
    Items(array): list or array-like object containing numerical 
    values.
    n (int): number of top items to retuen.
    
    Returns:
    array: top n items, in descending order.
    
    Examples:
    >>> top_n([8, 3, 2, 7, 4], 3)
    output [8, 7, 4]
    """ 
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j]>items[j+1]: # if this item is bigger than the next the item...
                items[j], items[j+1] = items[j+1], items[j] #swap the two!
    # Get last two items[-n:]
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]

#checkingfunction works
top_n([8, 3, 2, 7, 4], 3)