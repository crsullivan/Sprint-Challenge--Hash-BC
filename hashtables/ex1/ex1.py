#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):
        start = hash_table_retrieve(ht, (limit-weights[i]))
        print('i', i)
        print('first', start)
        if start is not None:
            pair = (i, start)
            # return the new 'starting point of the array insertion, as its index will by definition be greater than the other value found. 
            print('i start', i,start)
            print('pair', pair)
            return pair 
        else:
            # check values that have already been put in the array
            hash_table_insert(ht, weights[i], i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
