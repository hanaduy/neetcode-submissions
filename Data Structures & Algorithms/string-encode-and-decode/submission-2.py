class Solution:
    mapping = []

    def encode(self, strs: List[str]) -> str:
        self.mapping = []
        result = ""
        for word in strs:
            self.mapping.append(len(word))
            result += word
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        for i in range(len(self.mapping)):
            result.append(s[0:self.mapping[i]])
            s = s[self.mapping[i]:]
        print(result)
        return result