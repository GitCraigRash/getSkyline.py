class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Approch one:
        #Left to Right
        #Case Omega: No buildings
        # Case One: One building
        # Case two : two seperate buildings
        # Case three: two prefectly overlapping buidlings
        # Case four : two overlapping with one higher than another
        # Case five : two overlapping with one wider than the other
        # Case six : three seperate buildings
        # Case seven : three prefectly overlapping buildings
        # Case eight : two overlaping and one seperate building
        # Case nine : three overlaping buildings the second is lower than first, third overlaps second and is taller. 
        # Case ten :
        # Approch two: 
        # Shortest to tallest.
        # Problem: What if a huge building completely covers all other smaller buildings? Won't you have to reduce the number of nodes?
