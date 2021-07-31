import copy


def extend_partitions(some_partitions, a_new_element):
    '''
    Preconditions:
    1. some_partitions consists of partition of a set S (which need
    not be specified!) in the form of a list of lists of the set's elements.
    Example: S = {0, 11}, some_partitions = [[[0, 11]], [[0], [11]]]
    2. a_new_element does not occur in some_partitions

    Returns: returned_partitions = all partitions of (S union {a_new_element})

    Example: for S = {0, 11} and a_new_element = 22, this returns the following
    list (containing 5 elements): [[[0, 11, 22]], [[0, 22], [11]],
    [[0], [11, 22]], [[0, 11], [22]], [[0], [11], [22]]]
    '''
    returned_partitions = []

    # (Excluding [a_new_element]): returned_partition includes all partitions
    # of (S union {a_new_element}) that don't contain the list [a_new_element]

    # Example: For S = {0, 11} and a_new_element = 22, returned_partitions would include
    # [[0, 11, 22]], [[0, 22], [11]], [[0], [11, 22]], and [[[0], [11]], 22]]]
    # (notice that none of these partitions contains [22])

    for _partition in some_partitions:  # e.g., _partition = [[0], [11]]
        for i in range(len(_partition)):  # e.g., i points to [0]
            new_partition = copy.deepcopy(_partition)
            new_partition[i].append(a_new_element)  # e.g., get [[0, 22], [11]]
            returned_partitions.append(new_partition)

    # (Including [a_new_element]): returned_partition includes all partitions
    # of S union {a_new_element} that contain [a_new_element]

    # e.g., For the example above, returned_partition includes
    # [[0, 11], [22]] and [[0], [11], [22]]]

    for _partition in some_partitions:  # e.g., [[0, 11]]
        appended_partition = copy.deepcopy(_partition)
        appended_partition.append([a_new_element])
        returned_partitions.append(appended_partition)
        # e.g., append [[0, 11], [22]] in the example

    return returned_partitions
