class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dictionary = {}

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
                
        # sort dic
        print(dictionary)
        sorted_dict = sorted(dictionary, key=lambda x: dictionary[x], reverse=True)

        return sorted_dict[:k]
