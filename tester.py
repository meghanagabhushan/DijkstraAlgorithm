from dijkstra import *


def test_add_edge():
    graph.dijkstra("a", "e")
    # adding new edge changes the shortest path
    graph.add_edge("a", "e", 2)
    return graph.dijkstra("a", "e")


def test_remove_edge():
    graph.dijkstra("a", "f")
    graph.remove_edge("c","f")
    return graph.dijkstra("a","f")


def run_test_add_edge():
    actual_output = test_add_edge()
    expected_output = deque(['a', 'e'])
    if actual_output == expected_output:
        print("Success!")
    else:
        print("Test case for add edge failed!")

def run_test_remove_edge():
    actual_output = test_remove_edge()
    expected_output = deque(['a', 'e', 'f'])
    if actual_output == expected_output:
        print("Success!")
    else:
        print("Test case for remove edge failed!")

run_test_add_edge()
run_test_remove_edge()
