# Graphs

"""
FIFO - first in first out --> Lists. Using the same approach for graphs.
LIFO - last in first out --> Stacks
"""
from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire", "sergii"]
graph["claire"] = ["thom", "jonny"]
graph["sergii"] = ["vanka", "nikitka", "merim"]
graph["alice"] = ["peggy"]
graph["peggy"] = []
graph["tom"] = []
graph["bob"] = []
print(graph)


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller.")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")

