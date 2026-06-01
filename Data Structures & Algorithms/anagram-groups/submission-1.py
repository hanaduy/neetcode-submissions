class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_count(word):
            result = [0]*26
            for i in word:
                result[ord(i)-ord("a")] = int(result[ord(i)-ord("a")]) + 1
            # print(result)
            return ",".join([str(num) for num in result])
            
        from collections import defaultdict
        
        word_dict = defaultdict(list)
        for word in strs:
            word_dict[get_count(word)].append(word)
        
        result = []
        for k,v in word_dict.items():
            result.append(v)
        return result


        