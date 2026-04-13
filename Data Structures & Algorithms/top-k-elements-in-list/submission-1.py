class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+ 1)]

        counts = dict()

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for num, cnt in counts.items():
            freq[cnt].append(num)

        results = []
        index = len(nums)

        while index>0 and len(results) < k:
            results.extend(freq[index])
            index -= 1

        return results
