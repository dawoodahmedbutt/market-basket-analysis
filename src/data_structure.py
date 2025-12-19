from collections import defaultdict
import itertools

class MarketBasketGraph:
    """
    A weighted undirected graph to represent supermarket item co-occurrences.
    
    Structure (Adjacency List):
    {
        'milk': {'bread': 2, 'eggs': 1},
        'bread': {'milk': 2},
        ...
    }
    """
    def __init__(self):
        # Defaultdict allows me to add edges without checking if the node exists first
        # Outer dict: node -> Inner dict: neighbor -> weight
        self.graph = defaultdict(lambda: defaultdict(int))
        self.nodes = set()
        self.node_counts = defaultdict(int)

    def add_transaction(self, items):
        """
        Processes a single transaction (list of items).
        Updates nodes and edge weights for all pairs in the list.
        """
        # Remove duplicates in the basket to avoid self-loops (e.g., buying 2 milks)
        # Sort to ensure consistent processing 
        unique_items = sorted(list(set(items)))
        
        # Add all items to the node set
        for item in unique_items:
            self.nodes.add(item)
            self.node_counts[item] += 1
        
        # Generate all possible pairs (clique) and update edges
        for item1, item2 in itertools.combinations(unique_items, 2):
            self._add_edge(item1, item2)

    def _add_edge(self, u, v):
        """Internal method to add undirected edge with weight increment."""
        self.graph[u][v] += 1
        self.graph[v][u] += 1 

    def has_edge(self, u, v):
        """Checks if an edge exists between u and v."""
        return v in self.graph[u]

    def get_edge_weight(self, u, v):
        """Returns the co-occurrence frequency of u and v."""
        return self.graph[u].get(v, 0)

    def get_neighbors(self, node):
        """Returns a dictionary of neighbors and their weights for a given item."""
        return dict(self.graph[node])

    def get_all_nodes(self):
        """Returns a list of all unique items in the graph."""
        return list(self.nodes)
    
    def get_node_frequency(self, node):
        """Returns the total number of transactions the item appeared in"""
        return self.node_counts.get(node,0)