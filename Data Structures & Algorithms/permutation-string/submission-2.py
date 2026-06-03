class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)

        for ch in s1:
            count[ch] += 1

        length = len(s1)

        for l in range(len(s2) - length + 1):
            temp = defaultdict(int)

            for r in range(l, l + length):
                temp[s2[r]] += 1

            if temp == count:
                return True

        return False