#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # initialize values
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
    # key of none represents starting location value, find it
    x = []
    start = hash_table_retrieve(hashtable, 'NONE')
# put in the value of the starting location, pass it in as key (ie starting location for next destination) until desination = none (ie youre there)
    while start != 'NONE':
        x.append(start)
        start = hash_table_retrieve(hashtable, start)
    return x
