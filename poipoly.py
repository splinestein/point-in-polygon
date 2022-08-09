from typing import List


def ray_casting(point: List[int], polygon: List[List[int]]) -> bool:
    count = 0
    x = point[0]
    y = point[1]

    for c in range(len(polygon)-1):
        x1 = polygon[c][0]
        x2 = polygon[c+1][0]
        y1 = polygon[c][1]
        y2 = polygon[c+1][1]

        if (y < y1) != (y < y2) and x < (((x2 - x1) * (y - y1)) / (y2 - y1)) + x1:
            count += 1

    if count % 2 == 0:
        return False
    return True


if __name__ == '__main__':
    poi = [239779.070384, 6710937.361049]  # Your coordinates.
    poly = [
        [239737.161639, 6710964.032513],
        [239661.043577, 6711091.326975],
        [239785.826946, 6711162.754111],
        [239861.361902, 6711043.785487]
    ]  # Your polygon (area) marked clockwise.
    poly.append(poly[0])  # Must draw the final intersection back to origin.
    print(ray_casting(poi, poly))
