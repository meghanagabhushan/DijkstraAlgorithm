import unittest
from dijkstra import *


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_dijkstra(self):
        self.assertEqual(graph.dijkstra("a", "f"), deque(['a', 'c', 'f']))

    def test_add_edge(self):
        graph.add_edge("a", "e", 2)
        self.assertEqual(graph.dijkstra("a", "e"), deque(['a', 'e']))

    def test_remove_edge(self):
        graph.dijkstra("a", "f")
        self.assertEqual(graph.dijkstra("a", "f"), deque(['a', 'e', 'f']))


if __name__ == '__main__':
    unittest.main()
