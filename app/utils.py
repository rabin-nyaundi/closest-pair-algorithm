import math


# Utility function to format received comma separetd coodinates
def clean_data(data):
    data = list(data.split(';'))
    li = [[int(point) for point in item.split(',')] for item in data]

    return li


#  Algorithm to find the clossest pair given semi-colon separated points
class ClosestPair:
    def __init__(self, points):
        self.points = points

    # Calculats the distsnce between two points using Euclidean, pythagoras theorem
    def distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    
    def brute_force(self, points):
        min_distance = math.inf
        closest_pair = None
        size = len(points)

        for i in range(size):
            for j in range(i + 1, size):
                dist = self.distance(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    closest_pair = (points[i], points[j])

        return closest_pair

    # Points accross to the midpoint to left and right, Find the closest pair
    def strip_closest(self, strip, min_distance):
        strip_distance = min_distance
        closest_pair = None

        strip = sorted(strip, key=lambda point: point[1])
        size = len(strip)

        for i in range(size):
            for j in range(i + 1, size):
                if abs(strip[i][1] - strip[j][1]) < strip_distance:
                    dist = self.distance(strip[i], strip[j])
                    if dist < strip_distance:
                        strip_distance = dist
                        closest_pair = (strip[i], strip[j])
                else:
                    break

        return closest_pair

    def divide_and_conquer(self, points):
        points = sorted(points)

        size = len(points)
        if size <= 3:
            return self.brute_force(points)

        mid = size // 2
        mid_point = points[mid]
        left = points[:mid]
        right = points[mid:]

        min_left = self.divide_and_conquer(left)
        min_right = self.divide_and_conquer(right)

        min_distance = min(self.distance(min_left[0], min_left[1]), self.distance(min_right[0], min_right[1]))

        strip = [point for point in points if abs(point[0] - mid_point[0]) < min_distance]
        strip_closest_pair = self.strip_closest(strip, min_distance)

        if strip_closest_pair:
            return strip_closest_pair

        elif min_distance == self.distance(min_left[0], min_left[1]):
            return min_left
        else:
            return min_right

# points = [[2, 2], [1, 30], [20, 11], [4, 5]]
# closest_pair = ClosestPair(points)
# closest_distance = closest_pair.divide_and_conquer(points)
# print(closest_distance)

# cs = closest_pair.strip_closest([[2, 2], [3, 4], [4, 5], [5, 6]], math.sqrt(2))
# print(cs, "as ccc")


