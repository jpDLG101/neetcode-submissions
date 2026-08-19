class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: 
            return [strs]
        
        strs_dic = {}

        for s in strs:
            temp_lst = "".join(sorted(s))
            if temp_lst in strs_dic:
                strs_dic[temp_lst].append(s)
            else:
                strs_dic[temp_lst] = [s]
        return list(strs_dic.values())
