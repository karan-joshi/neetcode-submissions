class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "%" + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1
            str_len = int(s[i:j])
            decoded_list.append(s[j+1:j+1+str_len])
            i = j + 1 + str_len

        return decoded_list
