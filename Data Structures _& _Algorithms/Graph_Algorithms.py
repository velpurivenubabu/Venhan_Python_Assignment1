from typing import Dict, List, Tuple
import heapq

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  
    # Priority queue to keep track of nodes to visit
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  
        # Skip if we've already found a shorter path to this node
        if current_distance > distances[current_node]:
            continue
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If we find a shorter path to the neighbor, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
# input:
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 1, 'B': 4, 'D': 3},
    'D': {'B': 1, 'C': 3}
}
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":", shortest_distances)
