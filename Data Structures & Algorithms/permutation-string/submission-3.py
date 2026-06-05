class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        count = defaultdict(int)
        count_s1 = defaultdict(int)
        for i in s1:
            count_s1[i] += 1
        for i in range(len(s2)-window_size+1):
            if i == 0:
                for i in s2[0:window_size]:
                    count[i] += 1
                if count == count_s1:
                    return True
            else:
                count[s2[i-1]] -= 1
                if count[s2[i-1]] == 0:
                    del count[s2[i-1]]
                count[s2[i+window_size-1]] += 1
                if count == count_s1:
                    return True
        return False