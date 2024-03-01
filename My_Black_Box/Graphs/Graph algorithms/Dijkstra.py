"""
    this is an implementation f dijkstra's algorithm

"""


def dijkstra(graph, start):
            distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
            distances[start] = 0  # Distance from start to start is 0
            heap = [(0, start)]  # Priority queue to store nodes and their distances

            while heap:
                current_distance, current_node = heapq.heappop(heap)  # Get node with smallest distance
                if current_distance > distances[current_node]:
                    continue  # Skip if distance is already greater than the known distance

                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight  # Calculate tentative distance

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance  # Update distance if shorter
                        heapq.heappush(heap, (distance, neighbor))  # Add neighbor to the heap

            return distances