from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val: int = val
        self.neighbors: List[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        cloned_nodes: dict[int, Node] = {}

        def dfs(node: Node, cloned_nodes: dict[int, Node]):
            cloned_node: Node = Node(val=node.val)
            cloned_nodes[node.val] = cloned_node
            cloned_list: List[Node] = [cloned_node] * len(node.neighbors)
            for i, neighbor in enumerate(node.neighbors):
                if neighbor.val in cloned_nodes:
                    cloned_list[i] = cloned_nodes[neighbor.val]
                else:
                    dfs(neighbor, cloned_nodes)
                    cloned_list[i] = cloned_nodes[neighbor.val]

            cloned_node.neighbors = cloned_list
            return cloned_node

        return dfs(node, cloned_nodes=cloned_nodes) if node else None
