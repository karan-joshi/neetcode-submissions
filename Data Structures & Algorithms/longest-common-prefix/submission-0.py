class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]

        for s in strs:
            comm = ""

            for i in range(min(len(s), len(pre))):
                if s[i] == pre[i]:
                    comm += s[i]
                else:
                    break

            if comm == "":
                return comm
            
            pre = comm


        return pre

        
