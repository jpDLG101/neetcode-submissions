class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            else:
                counts[n] = counts[n] + 1

        sorted_counts_keys = sorted(counts, key=lambda item: counts[item], reverse=True)
        final_lst = []
        for i in range(k):
            final_lst.append(sorted_counts_keys[i])
        return final_lst
        


        
            

