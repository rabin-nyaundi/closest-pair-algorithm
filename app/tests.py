import math
from django.test import TestCase


from .utils import ClosestPair, clean_data

class ClossestPairTests(TestCase):
    def setUp(self):
        self.closest_pair = ClosestPair([])
        self.clean_data = clean_data

    def test_distance(self):
        p1 = [1, 2]
        p2 = [4, 6]
        expected_distance = math.sqrt(25)
        actual_distance = self.closest_pair.distance(p1, p2)
        self.assertEqual(actual_distance, expected_distance)

    def test_brute_force(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8], [2, 2]]
        expected_closest_pair = ([1, 2], [2, 2])
        actual_closest_pair = self.closest_pair.brute_force(points)
        self.assertEqual(actual_closest_pair, expected_closest_pair)

    def test_strip_closest(self):
        strip = [[2, 2], [3, 4], [4, 5], [5, 6]]
        min_distance = math.sqrt(2)
        expected_closest_pair = None
        actual_closest_pair = self.closest_pair.strip_closest(strip, min_distance)
        self.assertEqual(actual_closest_pair, expected_closest_pair)

        strip2 = [[2,1],[2, 2], [3, 4], [4, 5], [5, 6]]
        min_distance2 = math.sqrt(2)
        expected_closest_pair2 = ([2, 1], [2, 2])
        actual_closest_pair2 = self.closest_pair.strip_closest(strip2, min_distance2)
        self.assertEqual(actual_closest_pair2, expected_closest_pair2)

    def test_divide_and_conquer(self):
        points1 = [[1, 2], [3, 4], [5, 6], [7, 8], [2, 2]]
        expected_closest_pair1 = ([1, 2], [2, 2])
        actual_closest_pair1 = self.closest_pair.divide_and_conquer(points1)
        self.assertEqual(actual_closest_pair1, expected_closest_pair1)

        points2 = [[2, 3], [1, 1], [5, 6], [7, 8], [4, 5],[0,9]]
        expected_closest_pair2 = ([4, 5], [5, 6])
        actual_closest_pair2 = self.closest_pair.divide_and_conquer(points2)
        self.assertEqual(actual_closest_pair2, expected_closest_pair2)


    def test_clean_data(self):
        points = '1,2;3,4;5,6;7,8;9,0'
        expected_cleaned_data = [[1,2],[3,4],[5,6],[7,8],[9,0]]
        actual_cleaned_data = self.clean_data(points)
        self.assertEqual(actual_cleaned_data, expected_cleaned_data)
