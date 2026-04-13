class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()

        for i in range(len(nums)+1):
            count_map[i] = []

        counts = dict()

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for key, val in counts.items():
            if val in count_map:
                count_map[val].append(key)
            else:
                count_map[val] = [key]

        results = []
        index = len(nums)

        while index>0 and len(results) < k:
            results.extend(count_map[index])
            index -= 1

        return results
