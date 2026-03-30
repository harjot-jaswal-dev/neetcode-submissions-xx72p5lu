import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        results = []

        x2, y2 = 0, 0

        for point in points:
            x1 = point[0]
            y1 = point[1]

            current_distance = (x1 - x2)**2 + (y1 - y2)**2
            if len(results) < k:
                heapq.heappush(results, (-current_distance, point))
            else:
                heap_mini = results[0][0]
                if heap_mini < -current_distance:
                    heapq.heappop(results)
                    heapq.heappush(results, (-current_distance, point))
        
        final_results = []
        for distance, point in  results:
            final_results.append(point)
        return final_results



