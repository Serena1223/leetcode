class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sorted_strs = []
        grouped = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            sorted_strs.append(sorted_string)
            
            if sorted_string in grouped:
                grouped[sorted_string] += [string]
            else:
                grouped[sorted_string] = [string]

        return (grouped.values())

