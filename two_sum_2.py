class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # First reduce list to unique elements,
        # then locate the first index of those elements
        # this reduces the number of iterations
        unique_numbers = sorted(set(numbers))
        
        # Build dict of where each number occurs
        numbers_indexes = {}
        for i, x in enumerate(numbers):
            if not(x in numbers_indexes):
                numbers_indexes[x] = []
            numbers_indexes[x].append(i)
        
        for i, x in enumerate(unique_numbers):
            for j, y in enumerate(unique_numbers):
                if x + y == target and (x != y or len(numbers_indexes[x]) > 1):
                    # Yay found a match,
                    # now look up the indexes
                    index1 = numbers_indexes[x][0]

                    if x == y:
                        # Edge case:
                        # if we need the same number twice,
                        # get it from different indexes
                        index2 = numbers_indexes[y][1]
                    else:
                        index2 = numbers_indexes[y][0]
                        
                    return [1 + index1, 1 + index2]