class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        depart = set([x[0] for x in edges])
        destination = set([x[1] for x in edges])
        intersection = depart & destination
        start_only = depart - intersection
        return list(start_only)
