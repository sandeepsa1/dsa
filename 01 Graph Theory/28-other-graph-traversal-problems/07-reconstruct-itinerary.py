from collections import defaultdict

def find_itinerary(tickets: list[list[str]]) -> list[str]:
    # Step 1: Build the graph (adjacency list)
    flight_map = defaultdict(list)
    for departure, arrival in tickets:
        flight_map[departure].append(arrival)

    # Step 2: Sort the destinations for each departure lexicographically
    for departure in flight_map:
        flight_map[departure].sort(reverse=True)

    # Step 3: Perform DFS to build the itinerary
    result = []
    
    def dfs(airport):
        while flight_map[airport]:
            next_destination = flight_map[airport].pop()
            dfs(next_destination)
        result.append(airport)
    
    dfs("JFK")
    
    return result[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], 
           ["ATL", "JFK"], ["ATL", "SFO"]]

itinerary = find_itinerary(tickets)
print("Reconstructed Itinerary:", itinerary) # ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']