class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(the_say: str, left: int) -> str:
            if left == 1:
                return the_say
        
            new_say = ""
            
            n = len(the_say)
            i = 0
            while i < n:
                current_char = the_say[i]
                j = i+1
                while j < n and the_say[j] == current_char:
                    j += 1
                new_say += f"{j-i}" + current_char
                i = j
            
            return say(new_say, left-1)
        
        return say("1", n)