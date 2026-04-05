class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap_holder = {}
        
        for num in nums:
            if num in hashmap_holder:
                hashmap_holder[num]+= 1
            else:
                hashmap_holder[num]= 1
        
        output_list = []
        
        for i in range(k):
            top_frequent = None
            frequency = 0
            
            for num, freq in hashmap_holder.items():
                if num not in output_list and freq > frequency:
                    frequency = freq
                    top_frequent = num
            output_list.append(top_frequent)

        return output_list