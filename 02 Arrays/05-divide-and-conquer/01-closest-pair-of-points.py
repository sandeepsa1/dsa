import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    def closest_pair_rec(pts):
        if len(pts) <= 3:
            # Base case: Use brute force and track closest pair
            min_dist = float('inf')
            pair = (None, None)
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    dist = distance(pts[i], pts[j])
                    if dist < min_dist:
                        min_dist = dist
                        pair = (pts[i], pts[j])
            return min_dist, pair
        
        mid = len(pts) // 2
        left_pts = pts[:mid]
        right_pts = pts[mid:]
        
        min_dist_left, pair_left = closest_pair_rec(left_pts)
        min_dist_right, pair_right = closest_pair_rec(right_pts)
        
        # Determine the smallest distance from the two halves
        if min_dist_left < min_dist_right:
            min_dist = min_dist_left
            pair = pair_left
        else:
            min_dist = min_dist_right
            pair = pair_right
        
        # Check for closest pairs that span the dividing line
        mid_x = left_pts[-1][0]
        in_strip = [p for p in pts if abs(p[0] - mid_x) < min_dist]
        
        in_strip.sort(key=lambda p: p[1])
        
        for i in range(len(in_strip)):
            for j in range(i + 1, len(in_strip)):
                if (in_strip[j][1] - in_strip[i][1]) >= min_dist:
                    break
                dist = distance(in_strip[i], in_strip[j])
                if dist < min_dist:
                    min_dist = dist
                    pair = (in_strip[i], in_strip[j])
        
        return min_dist, pair
    
    points.sort()
    return closest_pair_rec(points)


points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
distance, pair = closest_pair(points)
print(f"Closest pair distance: {distance}")
print(f"Closest pair of points: {pair}")