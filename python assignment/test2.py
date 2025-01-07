class Solution(object):

    map_key = {
        2: ["a", "x"],
        3: ["b", "y"],
        4: ["c", "z"],
        5: ["d", "w"],
        6: ["e", "t", "u", "v"],
        7: ["f", "p", "q", "r", "s"],
        8: ["g", "m", "n", "o"],
        9: ["i", "h", "j", "k", "l"]
    }

    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Step 1: Precompute the push costs for each character
        char_cost = {}
        
        for key, characters in self.map_key.items():
            for i, char in enumerate(characters):
                char_cost[char] = i + 1  # The push count for the letter (i + 1)
        
        # Step 2: Calculate the total cost for the word based on its characters' frequencies
        minimum_cost = 0
        for char in word:
            minimum_cost += char_cost[char]
        
        return minimum_cost

test = Solution()
print(test.minimumPushes("xyzxyzxyzxyz"))