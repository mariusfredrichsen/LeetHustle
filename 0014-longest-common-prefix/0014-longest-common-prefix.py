class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ordered = strs
        ordered.sort()
        str_out = ""
        
        smallest = min(len(ordered[0]), len(ordered[-1]))

        for i in range(smallest):
            if ordered[0][i] == ordered[-1][i]:
                str_out += ordered[0][i]
                continue
            break

        return str_out    


