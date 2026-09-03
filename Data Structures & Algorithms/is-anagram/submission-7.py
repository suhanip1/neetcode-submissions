class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # return dict_s == dict_t

        if len(dict_s) != len(dict_t):
            return False 
        
        for i in dict_s:
            if dict_s[i] != dict_t.get(i,0):
                return False

        return True 
        