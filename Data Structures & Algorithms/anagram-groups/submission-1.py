class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary:
        # key   = character frequency tuple
        # value = list of words having that frequency
        res = defaultdict(list)

        # print("Initial res:", res)

        for s in strs:

            # print("\n==============================")
            # print("Current word:", s)

            # Create 26 counters:
            # index 0 = a
            # index 1 = b
            # ...
            # index 25 = z
            count = [0] * 26

            # print("Initial count:", count)

            for c in s:

                # print("\nCharacter:", c)

                # Find the index of the character
                index = ord(c) - ord('a')

                # print("Index:", index)

                # Increase frequency
                count[index] += 1

                # print("Updated count:", count)

            # Convert list to tuple because
            # tuples can be dictionary keys
            key = tuple(count)

            # print("Key:", key)

            # Add the word to the appropriate group
            res[key].append(s)

            # print("Updated res:", res)

        return list(res.values())