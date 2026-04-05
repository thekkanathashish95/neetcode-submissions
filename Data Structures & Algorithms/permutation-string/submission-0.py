class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def _get_hashmap(list1):
            hashmap = {}
            for elem in list1:
                if elem not in hashmap:
                    hashmap[elem]=1
                else:
                    hashmap[elem]+=1
            return hashmap
        
        s1_hashmap = _get_hashmap(s1)

        for left in range(len(s2)):
            right = left+len(s1)
            str_hashmap = _get_hashmap(s2[left:right])
            if str_hashmap == s1_hashmap:
                return True
            left+=1; right+=1
        return False


        