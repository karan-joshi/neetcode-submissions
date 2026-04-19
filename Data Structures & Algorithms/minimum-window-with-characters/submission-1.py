class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        count_t = {}
        count_w = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
            count_w[char] = 0
        
        i=0
        j=0
        shortest_str = ""
        curr = 0
        need = len(count_t)

        while i<=j and j < len(s):
            # print("i:", i, "j:", j, "s[i]:", s[i], "s[j]:", s[j])
            if s[j] in count_t:
                # print("s[j] in count_t")
                count_w[s[j]] += 1
                if count_w[s[j]] == count_t[s[j]]:
                    curr += 1
                    # print(curr)
            
            while curr == need:
                # print("curr = need", curr, need)
                if shortest_str == "" or len(shortest_str) > j-i+1:
                    shortest_str = s[i:j+1]
                    # print(shortest_str)
                if s[i] in count_w:
                    count_w[s[i]] -= 1
                    if count_w[s[i]] < count_t[s[i]]:
                        curr -= 1
                i += 1

            j += 1
            # print(count_w)

        
        return shortest_str


            
                

